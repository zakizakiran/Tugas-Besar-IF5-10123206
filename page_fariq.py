import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 1</h2>
        """, unsafe_allow_html=True)
    st.write("Fariq Daffa D. - 10123204")
    st.write("Pada musim apa sepeda paling sering disewa?")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    st.write("Informasi tentang aplikasi ini.")


