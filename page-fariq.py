import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.title("Pertanyaan 1")
    st.write("Fariq Daffa D. - 10123204")
    st.write("Pada musim apa sepeda paling sering disewa?")

with tab2:
    st.title("Hasil Analisis")
    st.write("Informasi tentang aplikasi ini.")


