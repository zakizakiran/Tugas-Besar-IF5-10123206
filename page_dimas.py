import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Muhamad Dimas Hergi P. - 10123211")
    st.write("Faktor-faktor apa yang paling berkorelasi dengan jumlah peminjaman sepeda?")

with tab2:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=cleaned_data, x='hr', y='cnt', ax=ax)
    ax.set_title("Distribusi Penyewaan Sepeda per Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)



