# Analisis Alur Sistem: Sistem Rekomendasi Game Steam (Fuzzy Mamdani)

Sistem ini dirancang untuk membaca input dari pengguna, menyaring data dari basis data (MySQL), melakukan perhitungan logika Fuzzy Mamdani, dan menampilkan 10 game terbaik yang paling direkomendasikan. 

Berikut adalah analisis langkah demi langkah dari alur sistem secara menyeluruh:

---

## 1. Input Pengguna (Frontend)
Proses dimulai ketika pengguna membuka halaman **Rekomendasi** (`recommend.html`). Di sini, pengguna diminta untuk mengisi formulir preferensi yang terdiri dari:
- **Genre** (misal: Action, RPG) - *Digunakan untuk penyaringan awal.*
- **Anggaran/Budget** (misal: Rp 200.000)
- **Spesifikasi PC** (Low / Medium / High)
- **Rating Pilihan** (misal: 80%)
- **Waktu Bermain Pilihan** (misal: 50 Jam)

Ketika tombol **"Cari Rekomendasi"** ditekan, data ini dikirim ke server (Backend) melalui rute `/recommend`.

---

## 2. Penyaringan Awal (Database)
Sebelum mesin Fuzzy bekerja, sistem melakukan optimasi (di dalam `recommendation.py` rute):
- Sistem mengambil data game dari basis data MySQL (tabel `games`).
- Sistem **menyaring** data berdasarkan **Genre** yang dipilih pengguna (menggunakan fungsi `LIKE`).
- Game yang tidak memiliki genre tersebut akan diabaikan. Hal ini membuat perhitungan fuzzy menjadi jauh lebih cepat dan terarah.

---

## 3. Proses Logika Fuzzy Mamdani (Backend)
Kumpulan game yang lolos penyaringan tadi kemudian dimasukkan ke dalam **Fuzzy Engine** (`app/services/fuzzy/`) satu per satu untuk dievaluasi kecocokannya dengan input pengguna. Proses ini terdiri dari 4 tahapan utama:

### A. Fuzzifikasi (`fuzzification.py`)
Sistem mengubah angka pasti (crisp) dari atribut game menjadi nilai *Fuzzy* (derajat keanggotaan antara 0 dan 1).
- **Harga Game:** Dibandingkan dengan **Anggaran** pengguna. Dikelompokkan menjadi *Rendah, Sedang, Tinggi*.
- **Rating Game:** Dibandingkan dengan **Rating Pilihan** pengguna. Dikelompokkan menjadi *Rendah, Sedang, Tinggi*.
- **Waktu Bermain Game:** Dibandingkan dengan preferensi pengguna. Dikelompokkan menjadi *Singkat, Sedang, Lama*.
- **Level PC:** Karena spesifikasi PC bersifat mutlak, sistem menggunakan himpunan tegas (singleton). Jika PC pengguna lebih tinggi atau sama dengan spesifikasi game, nilainya 1 (Lolos). Jika di bawahnya, nilainya 0 (Gagal).

### B. Inferensi Aturan (`inference.py`)
Nilai fuzzifikasi tadi dicocokkan dengan **81 Aturan Fuzzy (Rule Base)** yang telah dibuat.
Sistem menggunakan operator **MIN (AND)**. 
- *Contoh Aturan:* JIKA Harga Rendah DAN Rating Tinggi DAN Level PC Lolos DAN Waktu Bermain Sedang MAKA Rekomendasi = **Sangat Direkomendasikan**.
- Setiap aturan yang cocok akan menghasilkan nilai kekuatan (alfa) untuk kategori rekomendasi.

### C. Agregasi (`aggregation.py`)
Banyak aturan yang mungkin terpicu secara bersamaan. Sistem menggunakan operator **MAX (OR)** untuk menggabungkan (mengagregasi) semua kekuatan aturan menjadi kurva area untuk setiap kategori keluaran (Tidak Direkomendasikan, Kurang Direkomendasikan, Direkomendasikan, Sangat Direkomendasikan).

### D. Defuzzifikasi (`defuzzification.py`)
Sistem menggunakan metode **Sentroid (Center of Area)** untuk mencari titik tengah (pusat massa) dari area agregasi tersebut.
- Hasil dari defuzzifikasi ini adalah angka pasti (crisp) berupa **Skor Rekomendasi (0 - 100)** untuk setiap game.

---

## 4. Pengurutan dan Peringkat (Recommendation Engine)
Setelah setiap game mendapatkan **Skor Rekomendasi**, mesin akan:
1. **Mengurutkan** seluruh game dari skor yang paling tinggi hingga paling rendah (Descending).
2. **Memotong (Slicing)** hasilnya untuk hanya mengambil **10 Game Teratas (Top 10)**.
3. **Membuat Alasan Otomatis:** Sistem mengecek nilai input vs spesifikasi game untuk membuat kalimat bahasa Indonesia yang ramah bagi pengguna (misal: "Sangat sesuai dengan anggaran Anda", atau "Cerita panjang yang memuaskan").

---

## 5. Menampilkan Output (Frontend)
Daftar 10 game terbaik (beserta skor, alasan, dan datanya) dikirim kembali ke tampilan web (`results.html`).
- Pengguna melihat kartu-kartu game yang diurutkan dari Peringkat #1.
- Setiap kartu menampilkan **Skor %**, kategori rekomendasi, dan alasan mengapa game itu dipilih.
- Pengguna dapat mengklik tombol "Lihat di Steam" (atau mengklik kartu) untuk membuka halaman toko Steam game tersebut.

---

**Kesimpulan:** 
Alurnya sangat terstruktur: *Input -> Filter Database -> Fuzzifikasi -> Aturan (Inference) -> Agregasi -> Defuzzifikasi -> Peringkat -> Output UI.* Arsitektur ini memastikan logika matematika tetap terpisah dari tampilan web.
