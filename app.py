"""Digital Twin Spektrofotometer UV-Vis Agilent Cary 100 - Streamlit + Three.js"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Digital Twin Cary 100 UV-Vis", page_icon="🔬", layout="wide")

st.title("🔬 Digital Twin Spektrofotometer UV-Vis (Agilent Cary 100)")
st.caption(
    "Simulasi edukasi: urutan menyalakan alat, jalur berkas cahaya, dan pengukuran absorbansi. "
    "Data spektrum bersifat ilustratif, bukan data kalibrasi alat."
)

with st.sidebar:
    st.header("Cara memakai")
    st.markdown(
        """
1. Klik **tombol power UPS** → **saklar instrumen** → **tombol power PC** → **tombol power monitor**.
2. Tunggu *warm-up* selesai (lihat checklist).
3. Klik layar monitor / **Buka Cary WinUV**.
4. Buka tutup kompartemen, pasang kuvet **blanko**, tutup, lalu **Baseline**.
5. Pilih larutan sampel, ganti kuvet, tutup, lalu **Start**.
6. Aktifkan **Transparan** untuk melihat optik dan berkas cahaya.
        """
    )
    height = st.slider("Tinggi tampilan (px)", 500, 1200, 820, 20)

html = (Path(__file__).parent / "viewer.html").read_text(encoding="utf-8")
components.html(html, height=height, scrolling=False)
