import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Muhamad Dimas Hergi P. - 10123211")
    st.write("Faktor-faktor apa yang paling berkorelasi dengan jumlah peminjaman sepeda?")

with tab2:
    # Buat kategori waktu berdasarkan jam
    def categorize_hour(hour):
        if 0 <= hour <= 5:
            return "Dini Hari (00-05)"
        elif 6 <= hour <= 11:
            return "Pagi (06-11)"
        elif 12 <= hour <= 17:
            return "Siang (12-17)"
        else:
            return "Malam (18-23)"

    # Tambahkan kolom baru untuk kategori waktu
    cleaned_data["time_category"] = cleaned_data["hr"].apply(categorize_hour)

    # Judul Aplikasi
    st.title("Analisis Penyewaan Sepeda Berdasarkan Waktu")

    # Plot baru dengan kelompok waktu
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=cleaned_data, x="time_category", y="cnt", estimator=sum, ax=ax, palette="coolwarm")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Waktu dalam Sehari")
    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Total Penyewaan")

    # Tampilkan Plot di Streamlit
    st.pyplot(fig)


