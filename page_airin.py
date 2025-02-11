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
                <h2 style="color: #55AD9B;">Pertanyaan 3</h2>
        """, unsafe_allow_html=True)
    st.write("Airin Ristiana - 10123194")
    st.write("Bagaimana peminjaman sepeda pada bulan tertentu dipengaruhi oleh musim? ")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
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
        tile = container.container(border=True)
        tile.write(m)

    container2 = st.container(border=True)
    container2.caption("Peminjaman sepeda cenderung dipengaruhi oleh musim. Terlihat puncak peminjaman terjadi pada bulan-bulan musim panas, seperti Juni, Juli dan Agustus, yang menandakan cuaca cerah mendorong aktivitas luar ruangan. Sebaliknya, jumlah peminjaman menurun drastis pada bulan Desember, yang kemungkinan besar karena kondisi musim dingin yang kurang mendukung aktivitas luar ruangan. Data ini menunjukkan perlunya strategi operasional yang menyesuaikan dengan pola musiman.")

   


