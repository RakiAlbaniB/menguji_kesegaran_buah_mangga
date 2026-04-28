# 🥭 Mango Freshness Detection (KNN Method)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-red?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-black?style=for-the-badge&logo=opencv&logoColor=white&border=red" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
</div>

---

## 📌 Deskripsi Proyek
Proyek ini dikembangkan untuk mengklasifikasi tingkat kesegaran buah mangga secara otomatis. Menggunakan pendekatan **Informatics Engineering**, program ini mengekstraksi fitur warna untuk menentukan apakah mangga dalam kondisi **Segar** atau **Busuk**.

## 🚀 Fitur Utama
* **Ekstraksi Fitur HSV**: Mengonversi gambar dari BGR ke ruang warna *Hue, Saturation,* dan *Value* untuk akurasi deteksi warna yang lebih baik.
* **Klasifikasi KNN**: Mengimplementasikan algoritma *K-Nearest Neighbors* ($k=3$) untuk pengambilan keputusan.
* **Visualisasi Informatif**: Menampilkan gambar hasil uji dengan overlay status dan persentase akurasi model.

## 🛠️ Tech Stack
Proyek ini mengintegrasikan beberapa teknologi utama yang relevan dengan pengembangan perangkat lunak dan analisis data:
* **Bahasa Pemrograman**: `Python`.
* **Pengolahan Citra**: `OpenCV`.
* **Analisis Data**: `NumPy` & `Scikit-Learn`.
* **Visualisasi**: `Matplotlib`.

## ⚙️ Cara Instalasi
Pastikan library berikut sudah terpasang di lingkungan Python Anda:
```bash
pip install opencv-python numpy scikit-learn matplotlib
```

##📂 Cara Penggunaan
1. Letakkan gambar mangga (dataset pelatihan dan uji) di direktori yang sama dengan file script.

2. Jalankan perintah berikut :
```bash
python menguji_kesegaran_buah_mangga_menggunakan_metode_KNN.py
```
