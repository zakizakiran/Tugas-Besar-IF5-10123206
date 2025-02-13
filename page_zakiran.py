import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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
    st.write("Analisis klasterisasi ini bertujuan untuk mengelompokkan pengguna sepeda berdasarkan kesamaan pola penggunaan mereka. Dengan metode K-Means, pengguna dikelompokkan ke dalam tiga klaster berdasarkan suhu, kecepatan angin, dan jumlah penggunaan sepeda.")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    
    # Analisis Klasterisasi dengan K-Means berdasarkan kelembaban dan kecepatan angin
    st.subheader('Klasterisasi Penggunaan Sepeda Berdasarkan Kelembaban dan Kecepatan Angin')

    # Normalisasi data
    scaler = StandardScaler()
    day_scaled_env = scaler.fit_transform(cleaned_data[['hum', 'windspeed', 'cnt']])

    # K-Means clustering
    kmeans_env = KMeans(n_clusters=3, random_state=42)
    cleaned_data['cluster_env'] = kmeans_env.fit_predict(day_scaled_env)

    # Deskripsi klaster
    st.write("Analisis ini mengelompokkan pengguna sepeda berdasarkan kelembaban dan kecepatan angin. Berikut adalah karakteristik tiap klaster:")
    st.write("""
    - **Cluster 0:** Kelembaban rendah dan angin sedang.
    - **Cluster 1:** Kelembaban dan angin moderat.
    - **Cluster 2:** Kelembaban tinggi dan angin kencang.
    """)
    
    # Visualisasi hasil klasterisasi
    st.scatter_chart(
    data=cleaned_data[['hum', 'windspeed', 'cluster_env']],
    x='hum',
    y='windspeed',
    x_label='Kelembaban',
    y_label='Kecepatan Angin',
    color='cluster_env',  # Untuk pewarnaan berdasarkan klaster
    size=20,  # Ukuran titik
    use_container_width=True  # Menyesuaikan lebar dengan container
    )
    
    # Menampilkan jumlah data dalam setiap klaster
    cluster_counts_env = cleaned_data['cluster_env'].value_counts().reset_index()
    cluster_counts_env.columns = ['Cluster', 'Jumlah Data']
    st.subheader("Distribusi Data dalam Setiap Klaster")
    st.dataframe(cluster_counts_env, hide_index=True)
    st.container().caption("""
    - **Cluster 1:** Pengguna dengan pola penggunaan tinggi, sering terjadi pada kondisi kelembaban dan angin moderat.
    - **Cluster 0:** Pengguna dengan pola penggunaan sedang, umumnya ditemukan saat kelembaban rendah dan angin sedang.
    - **Cluster 2:** Pengguna dengan pola penggunaan rendah, cenderung muncul saat kelembaban tinggi dan angin kencang.
    """)

    # Kesimpulan
    st.write("Klasterisasi ini menunjukkan bahwa kelembaban dan kecepatan angin mempengaruhi pola penggunaan sepeda. Saat kelembaban tinggi dan angin kencang, jumlah pengguna cenderung lebih sedikit, sementara kondisi yang lebih nyaman meningkatkan jumlah pengguna.")
