import streamlit as st
import matplotlib.pyplot as plt
from variable import cleaned_data

# Membuat tab sebagai navbar
tab1, tab2 = st.tabs(["Pertanyaan", "Hasil"])

with tab1:
    st.markdown("""
                <h2 style="color: #55AD9B;">Pertanyaan 5</h2>
        """, unsafe_allow_html=True)
    st.write("Zaqi Satriya - 10123205")
    st.write("Bagaimana pola peminjaman sepeda antara pengguna casual dan registered setiap hari dalam satu minggu?")

with tab2:
    st.markdown("""
                <h2 style="color: #55AD9B;">Hasil Analisis</h2>
        """, unsafe_allow_html=True)
    
    # Mapping untuk nama hari
    weekday_map = {
        0: 'Minggu',
        1: 'Senin',
        2: 'Selasa',
        3: 'Rabu',
        4: 'Kamis',
        5: 'Jumat',
        6: 'Sabtu'
    }

    # Menghitung rata-rata pengguna per hari
    weekday_patterns = cleaned_data.groupby('weekday').agg({
        'casual': 'mean',
        'registered': 'mean'
    }).round(2)

    # Menambahkan nama hari
    weekday_patterns.index = weekday_patterns.index.map(weekday_map)

    # Membuat plot
    st.title("Pola Penggunaan Sepeda berdasarkan Hari")
    fig, ax = plt.subplots()
    weekday_patterns.plot(kind='bar', width=0.8, color=['red', 'blue'], ax=ax)

    ax.set_title('Pola Penggunaan Sepeda berdasarkan Hari', pad=20)
    ax.set_xlabel('Hari')
    ax.set_ylabel('Rata-rata Jumlah Pengguna')
    ax.legend(['Casual', 'Registered'], title='Tipe Pengguna')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_xticklabels(weekday_patterns.index, rotation=45)

    # Menambahkan nilai di atas bar
    for i in range(len(weekday_patterns)):
        for j, col in enumerate(weekday_patterns.columns):
            ax.text(i + (j-0.5)*0.4, weekday_patterns.iloc[i][col],
                    f'{weekday_patterns.iloc[i][col]:.0f}',
                    ha='center', va='bottom')

    st.pyplot(fig)

    st.write("Pola penggunaan harian juga menunjukkan bahwa pengguna registered cenderung stabil sepanjang minggu, sementara pengguna casual meningkat signifikan pada akhir pekan, terutama pada hari Minggu. Perusahaan dapat memanfaatkan peningkatan pengguna casual pada akhir pekan dengan menawarkan diskon khusus atau event promosi.")