import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from page_data import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Airin Ristiana - 10123194")
    st.write("Bagaimana peminjaman sepeda pada bulan tertentu dipengaruhi oleh musim? ")

with tab2:
    st.title("Hasil Analisis")
    month = {
        1: 'Januari',
        2: 'Februari',
        3: 'Maret',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Agustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Desember'
    }

    monthly_sn_data = cleaned_data.groupby(['mnth', 'season'])['cnt'].sum().reset_index()

    fig, ax = plt.subplots()
    ax.plot(monthly_sn_data['mnth'].map(month), monthly_sn_data['cnt'], color='skyblue')
    ax.set_title("'PEMINJAMAN DATA PER BULAN BERDASARKAN MUSIM")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-Rata Peminjaman")
    ax.set_xticks(monthly_sn_data['mnth']) 
    ax.set_xticklabels(monthly_sn_data['mnth'].map(month), rotation=70)

    st.pyplot(fig)
    # Membuat dua set kolom
    row1 = st.columns(2)
    row2 = st.columns(2)

    # Informasi musim di Portugal
    musim = [
        "Musim Semi (Primavera): Maret hingga Mei", 
        "Musim Panas (Verão): Juni hingga Agustus",
        "Musim Gugur (Outono): September hingga November", 
        "Musim Dingin (Inverno): Desember hingga Februari"
    ]

    container = st.container(border=True)
    container.title("Musim di Portugal")

    for m in musim:
        tile = container.container(height=50)
        tile.write(m)


