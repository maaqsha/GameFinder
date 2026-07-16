# Panduan Instalasi

## Prasyarat

- Python 3.12+
- MySQL 8.0+
- Git
- Visual Studio Code (direkomendasikan)

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

Buat database MySQL:

```sql
CREATE DATABASE gamefinder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Konfigurasi koneksi di file `.env` (buat dari `.env.example`):

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=gamefinder
```

### 5. Impor Data

```bash
mysql -u root -p gamefinder < dataset/import.sql
```

Atau jalankan skrip pra-pemrosesan Python (jika tersedia) untuk memuat CSV ke MySQL.

### 6. Jalankan Aplikasi

```bash
python run.py
```

Aplikasi akan tersedia di: `http://localhost:5000`

---

## Struktur Dependensi

| Paket | Tujuan |
|-------|--------|
| Flask | Framework web |
| mysql-connector-python | Driver MySQL |
| python-dotenv | Manajemen variabel lingkungan |
| pytest | Framework pengujian |

---

## Verifikasi Instalasi

1. Buka `http://localhost:5000`
2. Halaman beranda harus muncul
3. Klik "Mulai Rekomendasi"
4. Isi formulir dan kirim
5. Hasil Top 10 harus ditampilkan dengan skor
6. Klik "Lihat Detail" → halaman detail game muncul dengan penjelasan

---

## Penanganan Masalah (Troubleshooting)

| Masalah | Solusi |
|---------|--------|
| Galat koneksi MySQL | Periksa `.env`, pastikan MySQL berjalan, verifikasi kredensial |
| Modul tidak ditemukan | Jalankan `pip install -r requirements.txt` di virtual env yang aktif |
| Port 5000 digunakan | Ubah port di `run.py` atau hentikan proses yang menggunakan port 5000 |
| Data kosong | Pastikan `import.sql` sudah dijalankan, periksa tabel `games` |

---

## Perintah Berguna

```bash
# Jalankan pengujian
pytest

# Jalankan dengan mode debug
FLASK_DEBUG=1 python run.py

# Hapus virtual environment
rm -rf venv
```