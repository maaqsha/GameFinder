# Sistem Rekomendasi Game Steam

Sistem rekomendasi game Steam berbasis web menggunakan inferensi **Fuzzy Mamdani**. Dibangun dengan Flask, MySQL, dan 243-aturan mesin fuzzy.

## Arsitektur

```
Input Pengguna ──▶ Fuzzifikasi ──▶ Inferensi (243 aturan) ──▶ Agregasi ──▶ Defuzzifikasi ──▶ Hasil Peringkat
```

Lima dimensi input: anggaran, level PC, tipe gamer, rating yang disukai, waktu bermain yang disukai. Setiap game diberi skor berdasarkan profil pengguna, kemudian diurutkan berdasarkan skor secara menurun.

## Persyaratan

- Python 3.12+
- MySQL 8+
- Dependensi tercantum di `requirements.txt`

## Persiapan

### 1. Basis Data (Database)

```bash
mysql -u root < dataset/import.sql
```

Ini akan membuat basis data `gamefinder` dan tabel `games`, kemudian mengimpor 600+ judul game Steam yang telah dikurasi.

### 2. Lingkungan Python

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Jalankan

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

- `01_Project_Overview.md` — Ringkasan dan tujuan proyek
- `02_Functional_Requirements.md` — Kebutuhan fungsional
- `03_Database_Design.md` — Skema dan sumber data
- `04_Fuzzy_Design.md` — Arsitektur Fuzzy Mamdani
- `05_Membership_Function.md` — Definisi fungsi keanggotaan
- `06_Rule_Strategy.md` — Strategi basis aturan
- `08_Project_Structure.md` — Referensi struktur file
