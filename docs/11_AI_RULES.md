# 11_AI_RULES.md

# Aturan Pengodean AI (AI Coding Rules)

## Tujuan

Dokumen ini mendefinisikan bagaimana asisten pemrograman AI (AI coding assistant) harus bersikap dan bertindak selama mengembangkan proyek ini.

Aturan-aturan ini bersifat wajib.

------------------------------------------------------------------------

# Aturan 1

Bacalah setiap dokumen yang ada di dalam folder `docs/` sebelum menulis kode apa pun.

------------------------------------------------------------------------

# Aturan 2

Dilarang mengubah cakupan (scope) proyek kecuali secara eksplisit diinstruksikan demikian.

------------------------------------------------------------------------

# Aturan 3

Dilarang merancang ulang (redesign) arsitektur.

Ikuti struktur folder yang telah didokumentasikan.

------------------------------------------------------------------------

# Aturan 4

Dilarang menambahkan fitur-fitur yang berada di luar cakupan yang telah didokumentasikan.

Contoh:

-   Proses Masuk (Login)
-   Pendaftaran (Registration)
-   Dasbor Admin
-   Steam API
-   Sistem Pembayaran
-   Pembelajaran Mesin (Machine Learning)
-   Pembelajaran Mendalam (Deep Learning)

------------------------------------------------------------------------

# Aturan 5

Selalu ikuti urutan implementasi yang didefinisikan dalam `10_Task_List.md`.

------------------------------------------------------------------------

# Aturan 6

Selesaikan satu tugas besar (major task) pada satu waktu.

Dilarang mengerjakan beberapa fase besar secara bersamaan (simultan).

------------------------------------------------------------------------

# Aturan 7

Logika bisnis (business logic) hanya berada di dalam modul layanan (service) Fuzzy.

Rute (Routes) hanya boleh melakukan hal-hal berikut:

-   Menerima permintaan (requests)
-   Memvalidasi masukan (input)
-   Memanggil layanan (services)
-   Mengembalikan respons (responses)

------------------------------------------------------------------------

# Aturan 8

Dilarang menggunakan pustaka (library) logika fuzzy pihak ketiga.

Implementasikan keseluruhan algoritma Fuzzy Mamdani secara manual.

------------------------------------------------------------------------

# Aturan 9

Jika ditemukan konflik di dalam dokumentasi:

-   Hentikan implementasi.
-   Jelaskan konflik tersebut.
-   Mintalah klarifikasi.

Dilarang menebak-nebak (Never guess).

------------------------------------------------------------------------

# Aturan 10

Jika ada informasi yang kurang (missing):

-   Buatlah asumsi paling masuk akal yang terkecil.
-   Dokumentasikan asumsi tersebut secara jelas.
-   Lanjutkan hanya jika tidak memengaruhi arsitektur.

------------------------------------------------------------------------

# Aturan 11

Hasilkan kode Python yang bersih.

Persyaratan:

-   Mengikuti PEP 8
-   Fungsi-fungsi berukuran kecil
-   Kode dapat digunakan ulang (reusable)
-   Penamaan yang bermakna
-   Hindari duplikasi

------------------------------------------------------------------------

# Aturan 12

Sebelum menyelesaikan setiap fase:

Verifikasi:

-   Tidak ada galat sintaksis (syntax errors)
-   Tidak ada galat saat berjalan (runtime errors)
-   Tidak ada impor yang tertinggal (missing imports)
-   Tidak ada rute yang rusak (broken routes)

------------------------------------------------------------------------

# Aturan 13

Setelah menyelesaikan suatu fase:

Sediakan:

-   Tugas-tugas yang telah diselesaikan
-   Berkas-berkas yang telah dibuat
-   Catatan-catatan penting seputar implementasi
-   Sisa pekerjaan

Tunggu konfirmasi pengguna sebelum memulai fase besar selanjutnya.

------------------------------------------------------------------------

# Aturan 14

Saat menghasilkan basis aturan fuzzy:

-   Cakup seluruh kombinasi (81 aturan).
-   Tidak boleh ada aturan yang ganda (duplikat).
-   Tidak boleh ada keluaran yang bertentangan.
-   Ikuti:
    -   Fungsi Keanggotaan (Membership Function)
    -   Strategi Aturan (Rule Strategy)
    -   Basis Pengetahuan (Knowledge Base)

------------------------------------------------------------------------

# Aturan 15

Tujuan Proyek

Tujuannya bukanlah membangun situs web yang paling kompleks.

Tujuannya adalah mengimplementasikan algoritma rekomendasi Fuzzy Mamdani dengan benar di dalam aplikasi Flask yang bersih dan mudah dipelihara.

Selalu utamakan ketepatan, kesederhanaan, dan konsistensi alih-alih kerumitan yang tidak diperlukan.
