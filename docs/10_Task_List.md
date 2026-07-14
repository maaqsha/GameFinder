# 10_Task_List.md

# Daftar Tugas Pengembangan AI (AI Development Task List)

## Tujuan

Dokumen ini mendefinisikan urutan implementasi untuk asisten pemrograman AI (AI coding assistant).

Selesaikan setiap tugas secara berurutan. Dilarang melewati (skip) tugas. Mintalah konfirmasi sebelum beralih ke fase utama berikutnya.

------------------------------------------------------------------------

# Fase 1 --- Inisialisasi Proyek

## Tugas 1

-   Buat proyek Flask.
-   Buat struktur folder.
-   Instal dependensi.
-   Verifikasi aplikasi berjalan dengan baik.

Hasil akhir (Deliverable): - Proyek Flask yang dapat dijalankan.

------------------------------------------------------------------------

# Fase 2 --- Persiapan Dataset

## Tugas 2

-   Muat `steamgamesdataset.csv`.
-   Simpan hanya kolom-kolom yang diperlukan.
-   Hapus duplikat App ID.
-   Tangani nilai yang hilang (missing values).
-   Hasilkan `rating_percentage`.
-   Hasilkan `pc_level`.

Hasil akhir: - Dataset yang bersih.

------------------------------------------------------------------------

# Fase 3 --- Basis Data (Database)

## Tugas 3

-   Buat basis data MySQL.
-   Buat tabel `games`.
-   Impor dataset yang telah dibersihkan.
-   Verifikasi rekam data (records) yang telah diimpor.

Hasil akhir: - Basis data yang berfungsi.

------------------------------------------------------------------------

# Fase 4 --- Mesin Fuzzy

## Tugas 4

Implementasikan: - Fungsi Keanggotaan (Membership Function) - Fuzzifikasi - Inferensi Aturan (Rule Inference) - Agregasi - Defuzzifikasi Sentroid (Centroid Defuzzification)

Hasil akhir: - Mesin Fuzzy Mamdani yang berfungsi.

------------------------------------------------------------------------

# Fase 5 --- Basis Aturan (Rule Base)

## Tugas 5

-   Hasilkan semua 243 aturan (3⁵ anggaran × pc_level × gamer_type × rating × playtime). *Catatan: Aturan asli menyebut 81 (3⁴) kombinasi, sesuaikan dengan aturan yang berlaku (misalnya 4 variabel = 81 aturan, jika 5 variabel = 243 aturan).*
-   Validasi seluruh kombinasi.
-   Pastikan tidak ada aturan yang ganda (duplikat) atau saling bertentangan.

Hasil akhir: - Basis aturan yang telah divalidasi.

------------------------------------------------------------------------

# Fase 6 --- Mesin Rekomendasi

## Tugas 6

-   Saring berdasarkan genre.
-   Evaluasi seluruh kandidat game.
-   Peringkatkan hasil.
-   Kembalikan 10 Teratas (Top 10).

Hasil akhir: - Mesin rekomendasi.

------------------------------------------------------------------------

# Fase 7 --- Antarmuka Pengguna (UI)

## Tugas 7

Buat: - Beranda (Home) - Formulir Rekomendasi - Hasil - Detail

Hasil akhir: - Antarmuka pengguna (UI) yang responsif.

------------------------------------------------------------------------

# Fase 8 --- Integrasi

## Tugas 8

Integrasikan: - Antarmuka pengguna (UI) - Basis Data (Database) - Mesin Fuzzy

Hasil akhir: - Aplikasi ujung-ke-ujung (End-to-end application).

------------------------------------------------------------------------

# Fase 9 --- Pengujian (Testing)

## Tugas 9

Uji: - Validasi - Perhitungan Fuzzy - Peringkat (Ranking) - Halaman Detail - Penanganan Galat (Error handling)

Hasil akhir: - Aplikasi yang stabil.

------------------------------------------------------------------------

# Fase 10 --- Peninjauan Akhir (Final Review)

## Tugas 10

-   Lakukan refaktorisasi (refactor) kode.
-   Hapus kode yang tidak terpakai.
-   Verifikasi akhir.
-   Perbarui dokumentasi.

Hasil akhir: - Proyek yang selesai sepenuhnya.

------------------------------------------------------------------------

# Aturan

-   Ikuti semua dokumen yang berada di dalam folder `docs/`.
-   Dilarang merancang ulang arsitektur.
-   Selesaikan satu fase pada satu waktu.
-   Laporkan penyelesaian setelah setiap fase berakhir.
