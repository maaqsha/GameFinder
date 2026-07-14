# 06_Rule_Strategy.md

# Strategi Aturan (Rule Strategy)

## Tujuan

Dokumen ini mendefinisikan bagaimana 81 aturan fuzzy dirancang untuk memastikan konsistensi di seluruh basis aturan.

------------------------------------------------------------------------

# Rumus Aturan

Setiap aturan mengikuti format ini:

    JIKA (IF)
    Anggaran (Budget) ADALAH ...
    DAN Level_PC ADALAH ...
    DAN Rating ADALAH ...
    DAN Waktu Bermain ADALAH ...

    MAKA (THEN) Rekomendasi ADALAH ...

------------------------------------------------------------------------

# Variabel Masukan (Input Variables)

  Variabel       Fungsi Keanggotaan
  -------------- ----------------------
  Anggaran       Rendah, Sedang, Tinggi
  Level PC       Rendah, Sedang, Tinggi
  Rating         Rendah, Sedang, Tinggi
  Waktu Bermain  Singkat, Sedang, Lama

Total kombinasi:

    3 × 3 × 3 × 3 = 81 Aturan

------------------------------------------------------------------------

# Prioritas Keputusan

Prioritas rekomendasinya adalah:

1.  Level PC
2.  Rating
3.  Anggaran
4.  Waktu Bermain

Kompatibilitas PC memiliki dampak tertinggi karena sebuah game tidak boleh direkomendasikan jika PC pengguna tidak mampu menjalankannya dengan wajar.

------------------------------------------------------------------------

# Tingkat Keluaran

  Keluaran                   Arti
  -------------------------- -----------------------
  Tidak Direkomendasikan     Kecocokan buruk
  Kurang Direkomendasikan    Kecocokan di bawah rata-rata
  Direkomendasikan           Kecocokan bagus
  Sangat Direkomendasikan    Kecocokan sangat baik

------------------------------------------------------------------------

# Prinsip Aturan

## Sangat Direkomendasikan (Highly Recommended)

Kondisi tipikal:

-   Kompatibilitas PC tinggi
-   Rating tinggi
-   Anggaran sesuai
-   Waktu bermain sesuai dengan preferensi pengguna

------------------------------------------------------------------------

## Direkomendasikan (Recommended)

Kondisi tipikal:

-   Sebagian besar kondisi cocok
-   Satu variabel mungkin Sedang

------------------------------------------------------------------------

## Kurang Direkomendasikan (Less Recommended)

Kondisi tipikal:

-   Beberapa variabel bernilai Sedang atau Rendah
-   Masih mungkin direkomendasikan

------------------------------------------------------------------------

## Tidak Direkomendasikan (Not Recommended)

Kondisi tipikal:

-   Kompatibilitas PC buruk
-   Rating rendah
-   Beberapa kondisi penting tidak cocok

------------------------------------------------------------------------

# Aturan Konsistensi

-   Masukan yang serupa harus menghasilkan keluaran yang serupa.
-   Tidak ada aturan yang saling bertentangan.
-   Setiap kombinasi masukan harus memetakan ke tepat satu keluaran.
-   Semua 81 kombinasi harus tercakup.

------------------------------------------------------------------------

# Daftar Periksa Validasi (Validation Checklist)

Sebelum menerima basis aturan akhir:

-   Terdapat 81 aturan.
-   Tidak ada aturan ganda (duplikat).
-   Tidak ada kombinasi yang hilang.
-   Tidak ada keluaran yang bertentangan.
-   Format aturan konsisten.

------------------------------------------------------------------------

# Dokumen Selanjutnya

Dokumen selanjutnya (07_Knowledge_Base.md) akan berisi basis pengetahuan yang digunakan untuk menghasilkan keseluruhan 81 aturan fuzzy.
