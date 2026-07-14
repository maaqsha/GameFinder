# 04_Fuzzy_Design.md

# Desain Fuzzy Mamdani

## Tinjauan

Dokumen ini mendefinisikan sistem inferensi fuzzy yang digunakan oleh Sistem Rekomendasi Game Steam.

Metode: **Fuzzy Mamdani**

Defuzzifikasi: **Sentroid (Centroid)**

------------------------------------------------------------------------

# Variabel Masukan (Input Variables)

## 1. Anggaran (Budget)

Fungsi Keanggotaan (Memberships):

-   Rendah (Low)
-   Sedang (Medium)
-   Tinggi (High)

------------------------------------------------------------------------

## 2. Level PC (PC Level)

Fungsi Keanggotaan:

-   Rendah (Low)
-   Sedang (Medium)
-   Tinggi (High)

------------------------------------------------------------------------

## 3. Rating Pilihan (Preferred Rating)

Fungsi Keanggotaan:

-   Rendah (Low)
-   Sedang (Medium)
-   Tinggi (High)

------------------------------------------------------------------------

## 4. Waktu Bermain Pilihan (Preferred Playtime)

Fungsi Keanggotaan:

-   Singkat (Short)
-   Sedang (Medium)
-   Lama (Long)

------------------------------------------------------------------------

# Variabel Keluaran (Output Variable)

## Skor Rekomendasi

Fungsi Keanggotaan:

-   Tidak Direkomendasikan (Not Recommended)
-   Kurang Direkomendasikan (Less Recommended)
-   Direkomendasikan (Recommended)
-   Sangat Direkomendasikan (Highly Recommended)

Rentang Keluaran:

0 - 100

------------------------------------------------------------------------

# Proses Inferensi

``` text
Masukan Pengguna
      ↓
Fuzzifikasi
      ↓
Evaluasi Aturan
      ↓
Agregasi
      ↓
Defuzzifikasi Sentroid
      ↓
Skor Rekomendasi
```

------------------------------------------------------------------------

# Kategori Rekomendasi

        Skor Kategori
  ---------- --------------------
      0 - 25 Tidak Direkomendasikan
     26 - 50 Kurang Direkomendasikan
     51 - 75 Direkomendasikan
    76 - 100 Sangat Direkomendasikan

------------------------------------------------------------------------

# Basis Aturan (Rule Base)

Mesin fuzzy menggunakan:

-   4 variabel masukan
-   3 fungsi keanggotaan untuk setiap masukan
-   Total kombinasi yang mungkin:

    3^4 = 81 Aturan

Semua kombinasi dicakup dalam basis aturan.

------------------------------------------------------------------------

# Keputusan Desain

-   Genre **bukan** variabel fuzzy.
-   Genre digunakan hanya untuk menyaring kandidat game sebelum inferensi fuzzy.
-   Setiap game yang disaring dievaluasi secara independen.
-   Skor rekomendasi diurutkan secara menurun (descending).
-   10 game teratas (Top 10) dikembalikan ke pengguna.

------------------------------------------------------------------------

# Defuzzifikasi

Metode:

**Sentroid (Pusat Area / Center of Area)**

Metode sentroid mengubah keluaran fuzzy yang telah diagregasi menjadi skor rekomendasi tegas (crisp).

------------------------------------------------------------------------

# Kriteria Penerimaan

-   Semua variabel masukan berpartisipasi dalam inferensi.
-   Setiap kombinasi masukan cocok dengan setidaknya satu aturan.
-   Setiap game yang dievaluasi menerima skor rekomendasi.
-   Skor dihasilkan dalam rentang 0--100.
