import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from variable import cleaned_data

rata_lembap = cleaned_data['hum'].mean()

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Isi Data", "EDA"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Isi Data</h2>
        """, unsafe_allow_html=True)
    st.write(cleaned_data.head())
    st.caption("Data diatas merupakan data yang sudah di combined.")
    st.write(f"Jumlah data : {len(cleaned_data)}")
    st.write(f"Kelembapan rata-rata nya adalah {rata_lembap:.2f}")


with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">EDA</h2>
        """, unsafe_allow_html=True)
    st.write("Melihat hubungan variabel antara temperatur (temp) dan temperatur yang dirasakan (atemp), dengan warna berbeda untuk setiap musim (season)")
    # Scatter plot antara 'temp' dan 'atemp'
    st.scatter_chart(
        cleaned_data,
        x="temp",
        y="atemp",
        x_label="Normalized Temperature(temp)",
        y_label="Normalized Feeling Temperature(atemp)",
        color='season'
    )
