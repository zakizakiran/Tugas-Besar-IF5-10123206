import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 6</h2>
        """, unsafe_allow_html=True)
    st.write("Mohamad Zaki Zakiran - 10123206")
    st.write("Berapa persentase perbandingan antara pengguna Casual dan Registered? Serta bagaimana pola peminjaman sepeda antara pengguna casual dan registered setiap hari dalam satu minggu?")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    st.write("Informasi tentang aplikasi ini.")


