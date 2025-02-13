import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 2</h2>
        """, unsafe_allow_html=True)
    st.write("Muhamad Dimas Hergi P. - 10123211")
    st.write("Jam berapa penyewaan sepeda paling tinggi dan rendah?")

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
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)

    # Plot baru dengan kelompok waktu
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=cleaned_data, x="time_category", y="cnt", estimator=sum, ax=ax, palette="coolwarm")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Waktu dalam Sehari")
    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Total Penyewaan")

    # Tampilkan Plot di Streamlit
    st.pyplot(fig)
    st.write("""Grafik menunjukkan total penyewaan sepeda berdasarkan waktu dalam sehari. Penyewaan tertinggi terjadi pada malam hari (18:00 - 23:00), sementara dini hari (00:00 - 05:00) memiliki jumlah terendah. Pagi dan siang hari menunjukkan peningkatan, dengan siang hari lebih tinggi. Tren ini mungkin dipengaruhi oleh waktu luang dan kenyamanan cuaca.""")

    

