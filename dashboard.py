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
    if st.button("ℹ️ Pertanyaan 1", use_container_width=True):
        switch_page("Pertanyaan 1")
    if st.button("📞 Pertanyaan 2", use_container_width=True):
        switch_page("Pertanyaan 2")
    if st.button("📞 Pertanyaan 3", use_container_width=True):
        switch_page("Pertanyaan 3")
    if st.button("📞 Pertanyaan 4", use_container_width=True):
        switch_page("Pertanyaan 4")
    if st.button("📞 Pertanyaan 5", use_container_width=True):
        switch_page("Pertanyaan 5")
    if st.button("📞 Pertanyaan 6", use_container_width=True):
        switch_page("Pertanyaan 6")


# Menampilkan halaman sesuai pilihan
if st.session_state.page == "Home":
    st.title("🚴🏻‍♀️ Dashboard Analisis Peminjaman Sepeda")
    st.write("Anggota Kelompok:")
    st.write("1. Mohamad Zaki Zakiran ")
    st.write("2. Mohamad Zaki Zakiran ")
    st.write("3. Mohamad Zaki Zakiran ")
    st.write("4. Mohamad Zaki Zakiran ")
    st.write("5. Mohamad Zaki Zakiran ")
    st.write("6. Mohamad Zaki Zakiran ")

elif st.session_state.page == "Pertanyaan 1":
    run_script("page-fariq.py")
    

elif st.session_state.page == "Pertanyaan 2":
    run_script("page-dimas.py")

elif st.session_state.page == "Pertanyaan 3":
    run_script("page-airin.py")

elif st.session_state.page == "Pertanyaan 4":
    run_script("page-fathya.py")

elif st.session_state.page == "Pertanyaan 5":
    run_script("page-zaqi.py")

elif st.session_state.page == "Pertanyaan 6":
    run_script("page-zakiran.py")
