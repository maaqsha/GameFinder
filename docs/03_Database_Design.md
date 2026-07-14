# 03_Database_Design.md

# Desain Basis Data (Database Design)

## Tinjauan

Sistem ini menggunakan desain basis data sederhana yang difokuskan untuk mendukung proses rekomendasi Fuzzy Mamdani.

Hanya diperlukan satu tabel.

------------------------------------------------------------------------

# Skema Basis Data

## Tabel: games

  Kolom               Tipe                          Deskripsi
  ------------------- ----------------------------- ------------------------------------
  app_id              BIGINT                        Steam App ID (Kunci Utama / Primary Key)
  name                VARCHAR(255)                  Nama game
  price               DECIMAL(10,2)                 Harga game
  positive            INT                           Ulasan positif
  negative            INT                           Ulasan negatif
  rating_percentage   DECIMAL(5,2)                  Persentase rating yang dihitung
  playtime_hours      DECIMAL(8,2)                  Rata-rata waktu bermain (jam)
  genre               VARCHAR(255)                  Genre game
  pc_level            TINYINT                       Level persyaratan PC (1=Rendah, 2=Sedang, 3=Tinggi)
  about               TEXT                          Deskripsi game
  header_image        TEXT                          URL gambar sampul (cover image)
  website             TEXT                          Situs web resmi

------------------------------------------------------------------------

# Kunci Utama (Primary Key)

-   app_id

------------------------------------------------------------------------

# Kolom Turunan (Derived Columns)

Nilai-nilai ini dihasilkan selama pra-pemrosesan (preprocessing).

## rating_percentage

Rumus:

    positive / (positive + negative) * 100

## pc_level

Ditetapkan selama pra-pemrosesan.

Nilai:

-   1 = Rendah (Low)
-   2 = Sedang (Medium)
-   3 = Tinggi (High)

------------------------------------------------------------------------

# Sumber Data

Dataset:

-   Dataset Game Steam (Steam Games Dataset)

Diimpor sebagai CSV selama pra-pemrosesan.

------------------------------------------------------------------------

# Pra-pemrosesan Data (Data Preprocessing)

Sebelum mengimpor:

-   Hapus duplikat App ID.
-   Ganti deskripsi yang hilang dengan string kosong.
-   Ganti URL situs web yang hilang dengan NULL.
-   Ubah harga dari USD ke IDR menggunakan nilai tukar yang dapat dikonfigurasi.
-   Ubah rata-rata waktu bermain dari menit ke jam.
-   Hitung rating_percentage.
-   Tetapkan pc_level sebagai INTEGER (1, 2, atau 3).
-   Normalisasi nilai genre.

------------------------------------------------------------------------

# Alur Kueri (Query Flow)

``` text
Muat game
      ↓
Saring berdasarkan genre
      ↓
Jalankan Fuzzy Mamdani
      ↓
Hitung skor
      ↓
Urutkan menurun (descending)
      ↓
Kembalikan 10 Teratas (Top 10)
```

------------------------------------------------------------------------

# Keputusan Desain (Design Decision)

Proyek ini sengaja menggunakan basis data tabel tunggal karena fokusnya adalah algoritma Fuzzy Mamdani, bukan kerumitan basis data relasional.
