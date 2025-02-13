import streamlit as st
import numpy as np
import pydeck as pdk
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 3</h2>
        """, unsafe_allow_html=True)
    st.write("Airin Ristiana - 10123194")
    st.write("Apakah angin kencang berhubungan dengan penurunan minat orang untuk menyewa sepeda?")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    
    np.random.seed(42)
    cleaned_data["latitude"] = np.random.uniform(36.96, 42.15, cleaned_data.shape[0])  # Koordinat Portugal
    cleaned_data["longitude"] = np.random.uniform(-9.50, -6.19, cleaned_data.shape[0])

    # Visualisasi peta menggunakan Pydeck
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=cleaned_data,
        get_position=["longitude", "latitude"],
        get_radius="windspeed * 5000",  # Skala radius berdasarkan windspeed
        get_color="[windspeed * 800, 100, 200, 150]",
        pickable=True,
        opacity=0.6,
    )

    view_state = pdk.ViewState(
        latitude=cleaned_data["latitude"].mean(),
        longitude=cleaned_data["longitude"].mean(),
        zoom=6,
        pitch=30,
    )

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    #deskripsi
    container1 = st.container(border=True)
    container1.caption("Titik-titik lebih padat terletak di area dengan angin kencang, hal ini bisa menunjukkan bahwa angin di daerah tersebut lebih sering tercatat atau memiliki kecepatan lebih tinggi. Terlihat pada data bahwa titik-titik terlihat padat di beberapa Kota.")

    st.scatter_chart(
        cleaned_data,
        x="windspeed",
        y="cnt",
        color="#55AD9B",
    )

    #deskripsi
    container2 = st.container(border=True)
    container2.caption("Penyewa cenderung lebih banyak saat windspeed rendah yang artinya saat angin tidak terlalu kencang.")


