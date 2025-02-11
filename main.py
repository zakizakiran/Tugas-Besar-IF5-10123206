import streamlit as st

# Panggil file lain
def run_script(file_path):
    with open(file_path, "r") as file:
        script = file.read()
    exec(script)

# Inisialisasi session_state untuk halaman
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def switch_page(page_name):
    st.session_state.page = page_name

st.markdown("""
    <style>
        /* Style untuk tombol di sidebar */
        div.stButton > button:first-child {
            background-color: #309ab3; /* Warna default */
            color: white;
            padding: 10px 24px;
            border-radius: 10px;
            font-size: 16px;
            border: 2px solid transparent;
            transition: all 0.3s ease-in-out;
        }

        /* Warna saat hover */
        div.stButton > button:first-child:hover {
            background-color: #41CEEF;
            border-color: #41CEEF;  
        }

        /* Warna saat tombol aktif (clicked) */
        div.stButton > button:first-child:active, div.stButton > button:focus {
            background-color: #217a94 !important; /* Warna aktif */
            color: white !important; /* Warna teks aktif */
            border: 2px solid #ffffff !important; /* Warna border aktif */
        }

        /* Mengubah warna default sidebar */
        [data-testid=stSidebar] {
            background-color: #309ab3;
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar dengan tombol navigasi
st.sidebar.markdown("""
    <h1 style="color: white; text-align: center;">Main Menu</h1>
""", unsafe_allow_html=True)
col1 = st.sidebar.columns(1)[0]  # Kolom untuk tombol full-width

with col1:
    if st.button("🚴🏻‍♀️ Home", use_container_width=True):
        switch_page("Home")
    if st.button("🗂️ Data", use_container_width=True):
        switch_page("Data")
    if st.button("ℹ️ Pertanyaan 1", use_container_width=True):
        switch_page("Pertanyaan 1")
    if st.button("🔎 Pertanyaan 2", use_container_width=True):
        switch_page("Pertanyaan 2")
    if st.button("💡 Pertanyaan 3", use_container_width=True):
        switch_page("Pertanyaan 3")
    if st.button("📈 Pertanyaan 4", use_container_width=True):
        switch_page("Pertanyaan 4")
    if st.button("🤔💭 Pertanyaan 5", use_container_width=True):
        switch_page("Pertanyaan 5")
    if st.button("🌐 Pertanyaan 6", use_container_width=True):
        switch_page("Pertanyaan 6")


# Menampilkan halaman sesuai pilihan
if st.session_state.page == "Home":
    st.title('Selamat Datang!')
    st.write('Selamat datang di dashboard analisis peminjaman sepeda. Silakan pilih menu di sebelah kiri untuk melihat hasil analisis dari setiap anggota kelompok kami.')
    vert_space = '<div style="padding: 20px 5px;"></div>'
    st.markdown(vert_space, unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center;">
            <iframe src="https://lottie.host/embed/8294b855-cdd2-4f41-878b-55c0fde10851/cMF4EedwJW.lottie" 
                    width="400" height="400" style="border: none;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div style="margin-top: 20px;padding: 16px; border-radius: 10px;text-align: center; 
                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);border: 1px solid #ddd;">
                <h3 style="color: #55AD9B;">Anggota Kelompok</h3>
                <div>
                    <p>Mohamad Zaki Zakiran - 10123206</p>
                </div>
                <div>
                    <p>Muhammad Dimas Hergi - 10123211</p>
                </div>
                <div>
                    <p>Fathya Nurulhasanah - 10123190</p>
                </div>
                <div>
                    <p>Airin Ristiana - 10123194</p>
                </div>
                <div>
                    <p>Fariq Daffa Dinizar - 10123204</p>
                </div>
                <div>
                    <p>Zaqi Satriya Eka P. - 10123205</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

   
elif st.session_state.page == "Data":
    run_script("page_data.py")

elif st.session_state.page == "Pertanyaan 1":
    run_script("page_fariq.py")

elif st.session_state.page == "Pertanyaan 2":
    run_script("page_dimas.py")

elif st.session_state.page == "Pertanyaan 3":
    run_script("page_airin.py")

elif st.session_state.page == "Pertanyaan 4":
    run_script("page_fathya.py")

elif st.session_state.page == "Pertanyaan 5":
    run_script("page_zaqi.py")

elif st.session_state.page == "Pertanyaan 6":
    run_script("page_zakiran.py")
