# 05_Membership_Function.md

# Spesifikasi Fungsi Keanggotaan (Membership Function)

## Tinjauan

Dokumen ini mendefinisikan semua fungsi keanggotaan yang digunakan oleh mesin inferensi Fuzzy Mamdani.

Bentuk Keanggotaan:

-   Segitiga (Triangular)
-   Tumpang tindih (Overlapping)
-   Transisi halus antara himpunan yang berdekatan

------------------------------------------------------------------------

# 1. Anggaran (IDR)

Rentang: 0 -- 1.000.000

  Keanggotaan  Rentang
  ------------ ----------------------
  Rendah       0 -- 300.000
  Sedang       200.000 -- 700.000
  Tinggi       600.000 -- 1.000.000

------------------------------------------------------------------------

# 2. Level PC

Rentang: 1 -- 3

    Nilai Arti
  ------- ---------
        1 Rendah
        2 Sedang
        3 Tinggi

Level PC menggunakan keanggotaan singleton yang tegas (crisp) — μ(x) = 1 jika nilainya cocok, 0 jika tidak. Tidak ada fungsi keanggotaan segitiga.

------------------------------------------------------------------------

# 3. Rating Pilihan (%)

Rentang: 0 -- 100

  Keanggotaan  Rentang
  ------------ -----------
  Rendah       0 -- 75
  Sedang       60 -- 90
  Tinggi       80 -- 100

------------------------------------------------------------------------

# 4. Waktu Bermain Pilihan (Jam)

Rentang: 0 -- 200

  Keanggotaan  Rentang
  ------------ -----------
  Singkat      0 -- 20
  Sedang       10 -- 80
  Lama         60 -- 200

------------------------------------------------------------------------

# Keluaran: Skor Rekomendasi

Rentang: 0 -- 100

  Keanggotaan                Rentang
  -------------------------- -----------
  Tidak Direkomendasikan     0 -- 25
  Kurang Direkomendasikan    20 -- 50
  Direkomendasikan           45 -- 75
  Sangat Direkomendasikan    70 -- 100

------------------------------------------------------------------------

# Aturan Desain

-   Setiap keanggotaan yang berdekatan saling tumpang tindih.
-   Semua variabel menggunakan metode inferensi yang sama.
-   Sentroid digunakan untuk defuzzifikasi.
-   Nilai keanggotaan dinormalisasi menjadi 0--1 selama perhitungan.

------------------------------------------------------------------------

# Catatan

Rentang-rentang ini adalah spesifikasi resmi untuk proyek ini. Implementasi apa pun harus mengikuti dokumen ini kecuali spesifikasinya diperbarui.
