# Sistem Rekomendasi Game Steam menggunakan Fuzzy Mamdani

## 1. Informasi Proyek

| Item | Deskripsi |
|------|-----------|
| Nama Proyek | Sistem Rekomendasi Game Steam |
| Metode | Fuzzy Mamdani |
| Platform | Aplikasi Web |
| Bahasa Pemrograman | Python |
| Kerangka Kerja (Framework) | Flask |
| Basis Data (Database) | MySQL |
| Frontend | HTML, Bootstrap 5, JavaScript |
| Jenis Pengembangan | Proyek AI Akademik |

---

## 2. Ringkasan Proyek

Proyek ini adalah sistem rekomendasi berbasis web yang membantu pengguna menemukan game Steam yang cocok berdasarkan preferensi dan spesifikasi komputer mereka.

Proses rekomendasi menggunakan metode **Fuzzy Mamdani** untuk mengevaluasi berbagai kriteria dan menghasilkan skor rekomendasi untuk setiap game.

Sistem ini dirancang untuk tujuan pendidikan guna mendemonstrasikan implementasi logika fuzzy dalam sistem pendukung keputusan.

---

## 3. Tujuan

Proyek ini bertujuan untuk:

- Mengimplementasikan algoritma **Fuzzy Mamdani** dalam sistem rekomendasi dunia nyata.
- Merekomendasikan game Steam berdasarkan berbagai preferensi pengguna.
- Memeringkat game yang direkomendasikan menggunakan inferensi fuzzy.
- Memberikan skor rekomendasi beserta penjelasan yang mudah dipahami.
- Mendemonstrasikan keseluruhan proses penalaran fuzzy dari masukan pengguna hingga keluaran rekomendasi.

---

## 4. Ruang Lingkup Proyek

Sistem ini mencakup:

- Halaman Beranda (Home)
- Formulir Rekomendasi
- Halaman Hasil Rekomendasi
- Halaman Detail Game
- Mesin Inferensi Fuzzy Mamdani
- Dataset game yang disimpan di MySQL
- Perhitungan Skor Rekomendasi
- Peringkat 10 Besar Rekomendasi (Top 10)

---

## 5. Di Luar Cakupan (Non-Goals)

Proyek ini **TIDAK** mencakup:

- Pendaftaran pengguna (Registrasi)
- Proses masuk pengguna (Login)
- Dasbor administrator
- Antarmuka manajemen CRUD
- Integrasi akun Steam
- Integrasi Steam API
- Pembelian game
- Pembayaran daring (Online payment)
- Fitur multipemain (Multiplayer)
- Sistem obrolan (Chat)
- Sistem daftar keinginan (Wishlist)
- Pembelajaran Mesin (Machine Learning)
- Pembelajaran Mendalam (Deep Learning)
- Pengikisan web otomatis (Web scraping)

Proyek ini hanya berfokus pada implementasi algoritma rekomendasi **Fuzzy Mamdani**.

---

## 6. Target Pengguna

Target penggunanya adalah siapa saja yang ingin menemukan game Steam yang sesuai dengan preferensi dan spesifikasi komputer mereka.

Tidak diperlukan akun atau autentikasi.

---

## 7. Tumpukan Teknologi (Technology Stack)

### Backend

- Python 3.12+
- Flask

### Frontend

- HTML5
- Bootstrap 5
- JavaScript

### Basis Data (Database)

- MySQL

### Alat Pengembangan

- Visual Studio Code
- Git
- GitHub

---

## 8. Alur Kerja Sistem

```text
Pengguna membuka situs web
        ↓
Mengisi formulir rekomendasi
        ↓
Memilih genre, tipe gamer, budget, rating, playtime
        ↓
Masukkan preferensi
        ↓
Menyaring game berdasarkan genre + budget
        ↓
Menjalankan inferensi Fuzzy Mamdani (243 aturan)
        ↓
Menghitung skor rekomendasi
        ↓
Mengurutkan game berdasarkan skor
        ↓
Menampilkan 10 besar rekomendasi + skor
        ↓
Melihat informasi detail game + alasan rekomendasi
```

---

## 9. Modul Proyek

### Modul Beranda

Menampilkan informasi proyek dan menyediakan akses ke sistem rekomendasi.

### Modul Input Rekomendasi

Mengumpulkan preferensi pengguna melalui formulir input.

### Modul Mesin Fuzzy

Memproses input pengguna menggunakan algoritma **Fuzzy Mamdani**.

### Modul Mesin Rekomendasi

Menghitung skor rekomendasi untuk semua kandidat game.

### Modul Hasil

Menampilkan 10 besar game yang direkomendasikan, diurutkan berdasarkan skor.

### Modul Detail

Menampilkan informasi lengkap tentang game yang dipilih beserta penjelasan rekomendasinya.

---

## 10. Kriteria Keberhasilan

Proyek dianggap selesai apabila:

- Situs web berjalan tanpa galat (runtime errors).
- Pengguna dapat mengirimkan preferensi rekomendasi.
- Algoritma **Fuzzy Mamdani** dieksekusi dengan sukses.
- Skor rekomendasi dihasilkan dengan benar.
- Sistem menampilkan 10 besar game yang direkomendasikan.
- Pengguna dapat membuka halaman detail game.
- Hasil rekomendasi konsisten dengan aturan fuzzy yang telah ditentukan.

---

## 11. Pengembangan Masa Depan

Kemungkinan perbaikan di masa depan meliputi:

- Integrasi API Steam
- Sistem akun pengguna
- Riwayat rekomendasi yang dipersonalisasi
- Daftar game favorit
- Menambah variabel rekomendasi
- Metode rekomendasi hibrida (Hybrid)
- Versi aplikasi seluler
- Sinkronisasi data Steam secara langsung (real-time)

---

## 12. Filosofi Proyek

Fokus utama proyek ini adalah penerapan algoritma **Fuzzy Mamdani**.

Situs web hanya berfungsi sebagai antarmuka pengguna untuk berinteraksi dengan mesin rekomendasi.

Algoritma rekomendasi, basis aturan fuzzy, dan proses inferensi adalah komponen inti dari sistem ini.