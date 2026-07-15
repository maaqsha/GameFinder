# 02_Functional_Requirements.md

# Persyaratan Fungsional (Functional Requirements)

## Tinjauan

Dokumen ini mendefinisikan semua persyaratan fungsional untuk Sistem Rekomendasi Game Steam.

Sistem ini hanya memiliki satu aktor:

-   Pengguna Tamu (Guest User)

Tidak ada modul autentikasi atau administrator yang disertakan.

------------------------------------------------------------------------

# Modul Fungsional

## FR-01 Halaman Beranda

### Deskripsi

Sistem harus menyediakan halaman arahan (landing page) yang memperkenalkan proyek ini.

### Persyaratan

-   Menampilkan judul proyek.
-   Menampilkan deskripsi proyek.
-   Menjelaskan bagaimana sistem rekomendasi bekerja.
-   Menyediakan tombol **Mulai Rekomendasi**.

------------------------------------------------------------------------

## FR-02 Formulir Rekomendasi

### Bidang Input (Input Fields)

  ID   Bidang                           Wajib (Required)
  ---- -------------------------------- ----------
  F1   Anggaran (Budget)                Ya
  F2   Genre Pilihan                    Ya
  F3   Level PC (Rendah / Sedang / Tinggi) Ya
  F4   Rating Pilihan                   Ya
  F5   Waktu Bermain Pilihan            Ya
   F6   Gamer Type (Casual/Balanced/Hardcore) Ya            Ya

### Persyaratan

-   Memvalidasi semua masukan (input).
-   Mencegah pengiriman formulir kosong.
-   Menampilkan pesan validasi.

------------------------------------------------------------------------

## FR-03 Penyaringan Genre (Genre Filtering)

Genre hanya digunakan sebagai penyaring basis data (database filter).

Persyaratan:

-   Menyaring game berdasarkan genre yang dipilih.
-   Mengecualikan game yang berada di luar genre yang dipilih.
-   Mengirimkan game yang telah disaring ke mesin fuzzy.

------------------------------------------------------------------------

## FR-04 Mesin Fuzzy Mamdani

Proses:

1.  Membaca masukan pengguna.
2.  Melakukan fuzzifikasi.
3.  Menjalankan inferensi aturan.
4.  Mengagregasi keluaran (outputs).
5.  Melakukan defuzzifikasi sentroid (centroid).
6.  Menghasilkan skor rekomendasi.

------------------------------------------------------------------------

## FR-05 Peringkat Rekomendasi

Persyaratan:

-   Menghitung skor untuk semua game yang telah disaring.
-   Mengurutkan berdasarkan skor (tertinggi lebih dulu).
-   Menampilkan 10 rekomendasi teratas (Top 10).

------------------------------------------------------------------------

## FR-06 Hasil Rekomendasi

Tampilan:

-   Peringkat
-   Nama Game
-   Skor Rekomendasi
-   Kategori Rekomendasi
-   Tombol Lihat Detail (View Detail)

------------------------------------------------------------------------

## FR-07 Detail Game

Tampilan:

-   Gambar Sampul (Cover Image)
-   Nama Game
-   Genre
-   Harga
-   Rating Steam
-   Level PC Minimum
-   Perkiraan Waktu Bermain
-   Skor Rekomendasi
-   Penjelasan Rekomendasi
-   URL Toko Steam (Steam Store URL)

------------------------------------------------------------------------

## FR-08 Penjelasan Rekomendasi

Contoh penjelasan:

-   Anggaran sesuai dengan preferensi pengguna.
-   Level PC memadai.
-   Rating memenuhi persyaratan minimum.
-   Waktu bermain sesuai dengan preferensi.

------------------------------------------------------------------------

# Aturan Bisnis (Business Rules)

-   BR-01: Skor rekomendasi dihasilkan menggunakan Fuzzy Mamdani.
-   BR-02: Penyaringan genre terjadi sebelum perhitungan fuzzy.
-   BR-03: Hanya game yang telah disaring yang dievaluasi.
-   BR-04: Hasil diurutkan secara menurun (descending).
-   BR-05: Menampilkan maksimal 10 rekomendasi.
-   BR-06: Masukan kosong tidak diizinkan.

------------------------------------------------------------------------

# Persyaratan Non-Fungsional

## Kinerja (Performance)

-   Menghasilkan rekomendasi dalam waktu 3 detik untuk dataset hingga 1000 game.

## Kegunaan (Usability)

-   Antarmuka yang responsif.
-   Navigasi sederhana.
-   Tata letak ramah pemula (Beginner-friendly).

## Keandalan (Reliability)

-   Masukan yang tidak valid tidak boleh merusak (crash) aplikasi.

------------------------------------------------------------------------

# Kriteria Penerimaan (Acceptance Criteria)

-   Pengguna dapat mengirimkan semua masukan yang diperlukan.
-   Mesin fuzzy berhasil dieksekusi.
-   Skor rekomendasi berhasil dihasilkan.
-   10 game teratas berhasil ditampilkan.
-   Halaman detail menampilkan informasi yang lengkap.
-   Penjelasan rekomendasi ditampilkan dengan benar.

