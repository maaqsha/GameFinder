# Panduan Instalasi

## Prasyarat

- Python 3.12+
- MySQL 8.0+
- Git

---

## Instalasi Langkah demi Langkah

### 1. Kloning Repositori

```bash
git clone https://github.com/username/GameFinder.git
cd GameFinder
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Instal Dependensi

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Basis Data

Buat database MySQL terlebih dahulu:

```sql
CREATE DATABASE gamefinder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Buat file `.env` dari `.env.example`:

```bash
cp .env.example .env
```

Sesuaikan isi `.env` dengan kredensial MySQL Anda:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password_anda
MYSQL_DATABASE=gamefinder
```

### 5. Impor Dataset

Jalankan skrip pra-pemrosesan untuk membuat tabel dan mengimpor data:

```bash
python preprocessing/reimport_db.py
```

Skrip ini akan:
- Menghapus tabel `games` jika sudah ada
- Membuat ulang tabel `games` dengan skema yang benar
- Mengimpor data dari `dataset/steamgames_clean.csv`

Atau, jika ingin menggunakan MySQL CLI langsung:

```bash
mysql -u root -p gamefinder < dataset/import.sql
```

**Catatan:** `dataset/import.sql` menggunakan `LOAD DATA LOCAL INFILE`. Pastikan MySQL mengizinkan `local_infile` dengan menjalankan:

```sql
SET GLOBAL local_infile = 1;
```

### 6. Jalankan Aplikasi

```bash
python run.py
```

Aplikasi akan tersedia di: `http://localhost:5000`

---

## Verifikasi Instalasi

1. Buka `http://localhost:5000`
2. Halaman beranda harus muncul dengan judul proyek
3. Klik **Mulai Rekomendasi**
4. Isi formulir (anggarkan, genre, level PC, tipe gamer, rating, waktu bermain)
5. Klik kirim
6. Hasil Top 10 rekomendasi harus ditampilkan dengan skor
7. Klik nama game → halaman detail muncul dengan penjelasan rekomendasi

---

## Penanganan Masalah (Troubleshooting)

| Masalah | Solusi |
|---------|--------|
| Galat koneksi MySQL | Periksa file `.env`, pastikan MySQL berjalan, verifikasi kredensial |
| `mysql.connector.errors.DatabaseError: 1049 (42000): Unknown database` | Jalankan `CREATE DATABASE gamefinder` terlebih dahulu |
| `LOAD DATA LOCAL INFILE` error | Jalankan `SET GLOBAL local_infile = 1;` di MySQL |
| Modul tidak ditemukan | Jalankan `pip install -r requirements.txt` di virtual env yang aktif |
| Port 5000 digunakan | Ubah port di `run.py` atau hentikan proses lain yang menggunakan port 5000 |

---

## Perintah Berguna

```bash
# Jalankan pengujian unit (tanpa DB)
python tests/test_recommendation.py

# Jalankan pengujian integrasi (butuh DB)
python tests/test_integration.py

# Hapus virtual environment
rm -rf venv
```
