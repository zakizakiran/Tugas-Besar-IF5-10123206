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
    container = st.container(border=True)
    container.caption(""" 
                    Musim Semi (Springer): Data menunjukkan variabilitas yang cukup besar, dengan titik-titik yang tersebar di berbagai rentang temperatur. Ini mencerminkan karakteristik musim semi yang sering kali tidak stabil, dengan hari-hari yang bisa terasa hangat atau dingin.

                    Musim Panas (Summer): Titik-titik data cenderung berkumpul di area temperatur tinggi, menunjukkan bahwa baik temperatur aktual maupun yang dirasakan lebih tinggi. Namun, ada beberapa kasus di mana atemp terasa lebih ekstrem daripada temp, mungkin karena efek kelembaban yang tinggi.

                    Musim Gugur (Fall): Pola data mirip dengan musim semi, tetapi dengan sedikit pergeseran ke arah temperatur yang lebih rendah. Ini menunjukkan transisi dari cuaca panas ke dingin, dengan variasi yang masih cukup signifikan.

                    Musim Dingin (Winter): Data lebih terkonsentrasi di area temperatur rendah, dengan atemp yang sering kali lebih rendah daripada temp, menunjukkan bahwa udara dingin terasa lebih menusuk. Ini bisa disebabkan oleh faktor seperti angin dingin yang meningkatkan sensasi dingin.
                      """)

