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

# Sidebar dengan tombol navigasi
st.sidebar.title("Main Menu")
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
    st.title("🚴🏻‍♀️ Analisis Peminjaman Sepeda")
    st.write("Anggota Kelompok:")
    st.write("1. Mohamad Zaki Zakiran - 10123")
    st.write("2. Muhammad Dimas Hergi - 10123")
    st.write("3. Fathya Nurulhasanah - 10123190")
    st.write("4. Airin Ristiana - 10123194")
    st.write("5. Fariq Daffa Dinizar - 10123")
    st.write("6. Zaqi Satriya Eka P. - 10123")
        
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
