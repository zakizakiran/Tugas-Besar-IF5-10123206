import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Zaqi Satriya - 10123205")
    st.write("Perlihatkan perbandingan penyewaan sepeda saat hari libur dan bukan hari libur!")

with tab2:
    st.title("Hasil Analisis")
    st.write("Informasi tentang aplikasi ini.")


