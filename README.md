# Sistem Rekomendasi Game Steam

Sistem rekomendasi game Steam berbasis web menggunakan inferensi **Fuzzy Mamdani**. Dibangun dengan Flask, MySQL, dan 243-aturan mesin fuzzy.

## Arsitektur

```
Input Pengguna ──▶ Fuzzifikasi ──▶ Inferensi (243 aturan) ──▶ Agregasi ──▶ Defuzzifikasi ──▶ Hasil Peringkat
```

Lima dimensi input: anggaran, level PC, tipe gamer, rating pilihan, waktu bermain pilihan. Setiap game diberi skor berdasarkan profil pengguna, kemudian diurutkan berdasarkan skor secara menurun.

## Persyaratan

- Python 3.12+
- MySQL 8+
- Dependensi tercantum di `requirements.txt`

## Persiapan

### 1. Buat Virtual Environment

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Konfigurasi Basis Data

Buat file `.env` dari `.env.example`:

```bash
cp .env.example .env
```

Sesuaikan isi `.env` dengan kredensial MySQL Anda.

Buat database MySQL:

```sql
CREATE DATABASE gamefinder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Impor Dataset

```bash
python preprocessing/reimport_db.py
```

Jika ingin menggunakan MySQL CLI langsung:

```bash
mysql -u root -p gamefinder < dataset/import.sql
```

### 4. Jalankan Aplikasi

```bash
python run.py
```

Buka http://127.0.0.1:5000

## Struktur Proyek

```
app/
├── routes/                   # Flask blueprints (home, recommend, detail)
├── services/fuzzy/           # Mesin Fuzzy Mamdani
│   ├── membership.py         # Fungsi keanggotaan
│   ├── fuzzification.py      # Input → himpunan fuzzy
│   ├── inference.py          # Evaluasi 243-aturan
│   ├── aggregation.py        # Agregasi output aturan
│   ├── defuzzification.py    # Defuzzifikasi centroid
│   └── recommendation.py     # Orkestrasi & penentuan skor
├── templates/                # Template Jinja2
├── static/                   # CSS, JS
tests/                        # Pengujian unit & integrasi
preprocessing/                # Skrip pra-pemrosesan dataset
docs/                         # Dokumentasi desain
```

## Pengujian (Tests)

```bash
# Pengujian unit (tidak memerlukan basis data)
python tests/test_recommendation.py

# Pengujian integrasi (memerlukan MySQL)
python tests/test_integration.py
```

## Dokumentasi

Dokumentasi desain terperinci ada di `docs/`:

- `01_PROJECT_OVERVIEW.md` — Ringkasan dan tujuan proyek
- `02_FUNCTIONAL_REQUIREMENTS.md` — Kebutuhan fungsional
- `03_FUZZY_LOGIC.md` — Desain Fuzzy Mamdani lengkap (MF, 243 aturan, inferensi)
- `04_SYSTEM_ARCHITECTURE.md` — Arsitektur sistem, skema DB, struktur folder
- `05_INSTALLATION.md` — Panduan instalasi
- `06_USER_GUIDE.md` — Panduan penggunaan
