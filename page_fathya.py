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
                <h2 style="color: #55AD9B;">Pertanyaan 4</h2>
        """, unsafe_allow_html=True)
    st.write("Fathya Nurulhasanah - 10123190")
    st.write("Apakah ada bulan dengan lonjakan peminjaman yang signifikan?")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    #data = {'mnth': list(range(1, 13)), 'cnt': [250000, 300000, 400000, 500000, 600000, 680000, 700000, 720000, 710000, 650000, 500000, 300000]}
    #cleaned_data = pd.DataFrame(data)
    monthly_data = cleaned_data .groupby('mnth')['cnt'].sum().reset_index()

    # fig, ax = plt.subplots()
    # ax.plot(monthly_data['mnth'], monthly_data['cnt'], marker='o', linestyle='-', color='pink', label='Jumlah Peminjaman Sepeda')

    # ax.set_title('LONJAKAN PEMINJAMAN PERBULAN')
    # ax.set_xlabel('Month')
    # ax.set_ylabel('Rata-Rata Peminjaman')
    # ax.legend()

    # st.pyplot(fig)

    st.line_chart(
        monthly_data, 
        x="mnth", 
        y="cnt", 
        x_label="Bulan",
        y_label="Jumlah Peminjaman Sepeda",
        color="#DE3163"
    )

    container = st.container(border=True)
    container.title("Kesimpulan : ")
    container.write("Berikut adalah analisis lonjakan peminjaman sepeda per-bulannya.")

   
    # Menampilkan poin-poin
    container.write("""
    - Januari - Maret       : Peminjaman rendah
    - April   - Juni        : Peminjaman meningkat
    - Juli                  : Peminjaman menurun sedikit
    - Agustus               : Peminjaman meningkat
    - September             : Peminjaman mulai menurun
    - Oktober - Desember    : Peminjaman menurun drastis
    """)
    container.write("Dapat disimpulkan bahwa lonjakan peminjaman sepeda meningkat secara signifikan pada rentang bulan April hingga Juni, sementara terjadi 			penurunan yang signifikan pada rentang bulan Oktober hingga Desember.")