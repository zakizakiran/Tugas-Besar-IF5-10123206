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

    month_order = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]

    monthly_sn_data = cleaned_data.groupby(['mnth', 'season'])['cnt'].sum().reset_index()

    monthly_sn_data["mnth"] = monthly_sn_data["mnth"].map(month)

    # Ubah menjadi kategori dengan urutan yang benar
    monthly_sn_data["mnth"] = pd.Categorical(monthly_sn_data["mnth"], categories=month_order, ordered=True)

    # Urutkan dataframe berdasarkan urutan bulan
    monthly_sn_data = monthly_sn_data.sort_values(by="mnth")
    

    st.line_chart(
        monthly_sn_data, 
        x="mnth", 
        y="cnt", 
        x_label="Bulan",
        y_label="Rata-Rata Peminjaman",
        color="#ffaa00")
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


