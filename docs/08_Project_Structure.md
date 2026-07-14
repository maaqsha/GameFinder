# 08_Project_Structure.md

# Struktur Proyek

## Tinjauan

Proyek ini mengikuti arsitektur modular Flask. Mesin Fuzzy Mamdani dipisahkan (diisolasi) dari lapisan web untuk meningkatkan kemudahan pemeliharaan (maintainability) dan pengujian.

------------------------------------------------------------------------

# Struktur Folder

``` text
steam-game-recommendation/
│
├── app/
│   ├── routes/
│   │   ├── home.py
│   │   ├── recommendation.py
│   │   └── detail.py
│   │
│   ├── services/
│   │   └── fuzzy/
│   │       ├── membership.py
│   │       ├── fuzzification.py
│   │       ├── inference.py
│   │       ├── aggregation.py
│   │       ├── defuzzification.py
│   │       └── recommendation.py
│   │
│   ├── models/
│   │   └── game.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── recommend.html
│   │   ├── results.html
│   │   ├── detail.html
│   │   ├── error.html
│   │   └── components/
│   │       ├── navbar.html
│   │       ├── footer.html
│   │       └── game_card.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── theme.js
│   │
│   └── utils/
│
├── dataset/
│   ├── steamgames_clean.csv
│   ├── steamgames_clean_v3.csv
│   ├── steam_games_2024-2026.csv
│   └── import.sql
│
├── preprocessing/
│   ├── clean_data.py
│   ├── import_to_mysql.py
│   ├── reimport_db.py
│   └── ...
│
├── docs/
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

------------------------------------------------------------------------

# Tanggung Jawab Modul

## Routes

Menangani permintaan (requests) dan respons (responses) HTTP.

## Models

Merepresentasikan entitas basis data (database).

## Services/Fuzzy

Berisi implementasi Fuzzy Mamdani secara keseluruhan.

## Templates

Melakukan proses render halaman antarmuka pengguna (UI).

## Static

Menyimpan CSS, JavaScript, dan gambar-gambar.

## Dataset

Menyimpan dataset orisinal dalam format CSV.

------------------------------------------------------------------------

# Prinsip Utama

Logika bisnis harus tetap berada di dalam modul `services/fuzzy`.

Routes hanya diperbolehkan untuk:
- Menerima masukan dari pengguna
- Memanggil layanan (service) rekomendasi
- Mengembalikan hasil

------------------------------------------------------------------------

# Ekspansi Masa Depan

Arsitektur ini memungkinkan untuk menambahkan hal-hal berikut:
- Integrasi Steam API
- Akun pengguna
- Metode rekomendasi tambahan

tanpa perlu mengubah sistem mesin fuzzy.
