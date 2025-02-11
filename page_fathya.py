import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.write("Informasi tentang aplikasi ini.")


