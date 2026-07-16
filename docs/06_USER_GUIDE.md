# Panduan Pengguna

## Cara Mendapatkan Rekomendasi Game

### 1. Buka Aplikasi

Akses `http://localhost:5000` di peramban (browser).

### 2. Klik "Mulai Rekomendasi"

Di halaman beranda, klik tombol untuk memulai proses rekomendasi.

### 3. Isi Formulir Rekomendasi

Berikan masukan berikut:

| Bidang | Deskripsi | Pilihan |
|--------|-----------|---------|
| Anggaran (Budget) | Jumlah maksimal yang ingin Anda belanjakan (IDR) | Angka positif apa saja |
| Genre | Preferensi genre game | Action, RPG, Strategy, dll. |
| Level PC | Kemampuan komputer Anda | Rendah / Sedang / Tinggi |
| Tipe Gamer | Profil preferensi bermain Anda | Casual / Balanced / Hardcore |
| Rating Pilihan | Rating Steam minimum yang Anda inginkan | 0 – 100% |
| Waktu Bermain | Durasi bermain per sesi yang diinginkan | Pendek / Sedang / Panjang |

### 4. Lihat Hasil

Halaman hasil menampilkan **10 besar game** yang direkomendasikan, diurutkan berdasarkan skor rekomendasi:

- **Peringkat** — Posisi dalam daftar
- **Nama Game** — Klik untuk melihat detail
- **Harga** — Harga game dalam IDR
- **Rating** — Persentase rating Steam
- **Skor** — Skor rekomendasi fuzzy (0–100)
- **Kategori** — Tidak Direkomendasikan / Kurang Direkomendasikan / Direkomendasikan / Sangat Direkomendasikan

### 5. Lihat Detail Game

Klik nama game untuk melihat:

- Gambar sampul
- Deskripsi lengkap
- Genre dan tag
- Harga
- Rating Steam dengan jumlah ulasan
- Level PC yang dibutuhkan
- **Penjelasan rekomendasi** (mengapa game ini cocok dengan profil Anda)
- Tautan ke Toko Steam

---

## Memahami Skor

| Rentang Skor | Kategori | Makna |
|--------------|----------|-------|
| 0 – 25 | Tidak Direkomendasikan | Kecocokan buruk dengan preferensi Anda |
| 26 – 50 | Kurang Direkomendasikan | Kecocokan di bawah rata-rata |
| 51 – 75 | Direkomendasikan | Kecocokan baik |
| 76 – 100 | Sangat Direkomendasikan | Kecocokan sangat baik dengan sebagian besar kriteria |

---

## Tips

- **Tidak punya batas anggaran?** Masukkan angka besar (mis. 1.000.000) untuk melihat semua game.
- **Ingin game gratis saja?** Atur anggaran ke 0.
- **Tidak yakin genre?** Kosongkan untuk melihat game dari semua genre.
- **Gamer Casual?** Pilih *Casual* — sistem memprioritaskan game berbudget rendah dengan rating layak.
- **Gamer Hardcore?** Pilih *Hardcore* — sistem memprioritaskan game berbudget tinggi, rating teratas.

---

## Tentang Metode Fuzzy Mamdani

Sistem ini menggunakan **Fuzzy Mamdani** dengan **defuzzifikasi sentroid**. Setiap game dievaluasi terhadap 5 kriteria (anggaran, level PC, tipe gamer, rating, waktu bermain) melalui **243 aturan fuzzy** untuk menghasilkan skor 0–100. Penjelasan di halaman detail menunjukkan kriteria mana yang mendukung rekomendasi.