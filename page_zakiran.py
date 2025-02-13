import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 6</h2>
        """, unsafe_allow_html=True)
    st.write("Mohamad Zaki Zakiran - 10123206")
    st.write("Analisis klasterisasi ini bertujuan untuk mengelompokkan pengguna sepeda berdasarkan kesamaan pola penggunaan mereka. Dengan metode K-Means, pengguna dikelompokkan ke dalam tiga klaster berdasarkan kelembaban, suhu, dan jumlah penggunaan sepeda.")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    
    # Analisis Klasterisasi dengan K-Means berdasarkan kelembaban dan suhu
    st.subheader('Klasterisasi Penggunaan Sepeda Berdasarkan Kelembaban dan Suhu')

    # Normalisasi data
    scaler = StandardScaler()
    day_scaled_env = scaler.fit_transform(cleaned_data[['hum', 'temp', 'cnt']])

    # K-Means clustering
    kmeans_env = KMeans(n_clusters=3, random_state=42)
    cleaned_data['cluster_env'] = kmeans_env.fit_predict(day_scaled_env)

    # Deskripsi klaster
    st.write("Analisis ini mengelompokkan pengguna sepeda berdasarkan kelembaban dan suhu. Berikut adalah karakteristik tiap klaster:")
    st.write("""
    - **Cluster 0:** Pengguna dengan pola penggunaan tinggi, sering terjadi saat suhu hangat dan kelembaban sedang.
    - **Cluster 1:** Pengguna dengan pola penggunaan sedang, ditemukan saat suhu moderat dengan kelembaban bervariasi.
    - **Cluster 2:** Pengguna dengan pola penggunaan rendah, cenderung muncul saat suhu rendah dan kelembaban tinggi.
    """)
    
    # Visualisasi hasil klasterisasi
    st.scatter_chart(
    data=cleaned_data[['hum', 'temp', 'cluster_env']],
    x='hum',
    y='temp',
    x_label='Kelembaban',
    y_label='Suhu',
    color='cluster_env',  # Pewarnaan berdasarkan klaster
    size=20,  # Ukuran titik
    use_container_width=True  # Menyesuaikan lebar dengan container
    )
    
    # Menampilkan jumlah data dalam setiap klaster
    cluster_counts_env = cleaned_data['cluster_env'].value_counts().reset_index()
    cluster_counts_env.columns = ['Cluster', 'Jumlah Data']
    st.subheader("Distribusi Data dalam Setiap Klaster")
    st.dataframe(cluster_counts_env, hide_index=True)
    st.container().caption("""
    - **Cluster 0:** Pengguna dengan pola penggunaan tinggi, sering terjadi saat suhu hangat dan kelembaban sedang.
    - **Cluster 1:** Pengguna dengan pola penggunaan sedang, ditemukan saat suhu moderat dengan kelembaban bervariasi.
    - **Cluster 2:** Pengguna dengan pola penggunaan rendah, cenderung muncul saat suhu rendah dan kelembaban tinggi.
    """)

    # Kesimpulan
    st.write("Klasterisasi ini menunjukkan bahwa suhu dan kelembaban mempengaruhi pola penggunaan sepeda. Saat suhu lebih hangat dengan kelembaban sedang, jumlah pengguna cenderung meningkat, sedangkan suhu rendah dengan kelembaban tinggi mengurangi penggunaan sepeda.")
