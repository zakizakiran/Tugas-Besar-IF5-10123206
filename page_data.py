import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1 = pd.read_csv('Datasepeda/day.csv')
data2 = pd.read_csv('Datasepeda/hour.csv')

combined = pd.concat([data1, data2], ignore_index=True)

combined.fillna({'hr': combined['hr'].mean()}, inplace=True)

cleaned_data = combined

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Isi Data", "EDA"])

with tab1:
    st.title("Isi Data")
    st.write(combined.head())
    st.caption("Data diatas merupakan data yang sudah di combined.")
    st.write(f"Jumlah data : {len(combined)}")

with tab2:
    st.title("EDA")
    st.write("Melihat hubungan variabel antara temperatur (temp) dan temperatur yang dirasakan (atemp), dengan warna berbeda untuk setiap musim (season)")
    # Scatter plot antara 'temp' dan 'atemp'
    cleaned_data = combined
    st.scatter_chart(
        cleaned_data,
        x="temp",
        y="atemp",
        x_label="Normalized Temperature(temp)",
        y_label="Normalized Feeling Temperature(atemp)",
        color='season'
    )
