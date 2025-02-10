import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Mohamad Zaki Zakiran - 10123206")
    st.write("Berapa persentase perbandingan antara pengguna Casual dan Registered? Serta bagaimana pola peminjaman sepeda antara pengguna casual dan registered setiap hari dalam satu minggu?")

with tab2:
    st.title("Hasil Analisis")
    st.write("Informasi tentang aplikasi ini.")


