# Digital Twin Spektrofotometer UV-Vis (Agilent Cary 100)

Aplikasi Streamlit yang menampilkan model 3D interaktif (Three.js) satu stasiun kerja lab:
Cary 100, komputer Dell, monitor, keyboard/mouse, UPS, dan kuvet.

## Fitur
- Orbit 360° (drag, scroll/pinch, klik kanan geser) + preset kamera
- Klik bagian mana pun untuk info nama & fungsi
- Mode **Transparan** (X-ray): lampu, cermin, celah, kisi, chopper, kompartemen sampel, detektor PMT
- **Berkas cahaya** animasi, warna sesuai panjang gelombang, meredup setelah kuvet (I = I0·10^-A)
- **Urutan menyalakan** dengan validasi: UPS → instrumen → komputer → monitor (mati: kebalikan)
- Simulasi **Cary WinUV**: Scan, Simple Reads, Baseline, ekspor CSV
- Syarat Start: warm-up selesai, baseline, tutup tertutup, kuvet terpasang

## Jalankan lokal
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)
1. Buat repo GitHub, upload `app.py`, `viewer.html`, `requirements.txt`, `README.md`.
2. Buka https://share.streamlit.io → New app → pilih repo, branch `main`, file `app.py` → Deploy.

Catatan: viewer memuat Three.js dari CDN (cdnjs & jsdelivr), jadi perlu internet.

## Disclaimer
Spektrum KMnO4 / K2Cr2O7 adalah data ilustratif. Spesifikasi teknis alat (jenis lampu, rentang, dll.)
perlu diverifikasi dengan manual alat. Urutan nyala sebaiknya disesuaikan SOP lab Anda.
