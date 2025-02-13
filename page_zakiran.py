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
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x=cleaned_data['hum'], y=cleaned_data['windspeed'], hue=cleaned_data['cluster_env'], palette='coolwarm', ax=ax)
    ax.set_title('Klasterisasi Penggunaan Sepeda Berdasarkan Kelembaban dan Kecepatan Angin')
    ax.set_xlabel('Kelembaban')
    ax.set_ylabel('Kecepatan Angin')
    st.pyplot(fig)

    # Menampilkan jumlah data dalam setiap klaster
    cluster_counts_env = cleaned_data['cluster_env'].value_counts().reset_index()
    cluster_counts_env.columns = ['Cluster', 'Jumlah Data']
    st.subheader("Distribusi Data dalam Setiap Klaster")
    st.dataframe(cluster_counts_env, hide_index=True)
    st.container().caption("""
    - **Cluster 0:** Pengguna dengan pola penggunaan tinggi, umumnya ditemukan saat kelembaban rendah dan angin sedang.
    - **Cluster 1:** Pengguna dengan pola penggunaan sedang, sering terjadi pada kondisi kelembaban dan angin moderat.
    - **Cluster 2:** Pengguna dengan pola penggunaan rendah, cenderung muncul saat kelembaban tinggi dan angin kencang.
    """)

    # Kesimpulan
    st.write("Klasterisasi ini menunjukkan bahwa kelembaban dan kecepatan angin mempengaruhi pola penggunaan sepeda. Saat kelembaban tinggi dan angin kencang, jumlah pengguna cenderung lebih sedikit, sementara kondisi yang lebih nyaman meningkatkan jumlah pengguna.")
