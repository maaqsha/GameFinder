# Arsitektur Sistem

## Tinjauan

Proyek mengikuti arsitektur Flask modular. Mesin **Fuzzy Mamdani** diisolasi dari lapisan web untuk kemudahan pemeliharaan dan pengujian.

---

## Struktur Direktori

```
GameFinder/
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
│   └── import.sql
│
├── tests/
│
├── docs/
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

---

## Tanggung Jawab Modul

### Routes (Rute)

Menangani permintaan dan respons HTTP saja.

- `home.py` — Halaman beranda (landing page)
- `recommendation.py` — Pengiriman formulir, orkestrasi evaluasi fuzzy, hasil
- `detail.py` — Halaman detail game dengan penjelasan rekomendasi

### Services / Fuzzy

Berisi implementasi lengkap **Fuzzy Mamdani**. Logika bisnis tetap di sini.

- `membership.py` — Definisi fungsi keanggotaan
- `fuzzification.py` — Konversi nilai input ke himpunan fuzzy
- `inference.py` — Generasi dan evaluasi 243 aturan
- `aggregation.py` — Agregasi output di seluruh aturan
- `defuzzification.py` — Defuzzifikasi sentroid
- `recommendation.py` — Mengorkestrasi pipeline rekomendasi ujung-ke-ujung

### Models (Model)

Representasi entitas basis data.

### Templates (Template)

Rendering Jinja2 untuk semua halaman UI.

### Static (Statis)

CSS, JavaScript, dan aset.

---

## Skema Basis Data

Desain tabel tunggal — sengaja. Fokus pada algoritma fuzzy, bukan kompleksitas relasional.

### Tabel: `games`

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| app_id | BIGINT | Steam App ID (Primary Key) |
| name | VARCHAR(255) | Nama game |
| price_idr | DECIMAL(10,2) | Harga dalam IDR |
| positive | INT | Ulasan positif |
| negative | INT | Ulasan negatif |
| rating_percentage | DECIMAL(5,2) | Persentase rating terhitung |
| playtime_hours | DECIMAL(8,2) | Rata-rata waktu bermain (jam) |
| genre | VARCHAR(255) | Genre game |
| tags | TEXT | Tag tambahan untuk penyaringan |
| pc_level | TINYINT | Level kebutuhan PC (1=Rendah, 2=Sedang, 3=Tinggi) |
| about | TEXT | Deskripsi game |
| header_image | TEXT | URL gambar sampul |
| website | TEXT | Situs web resmi |

### Kolom Turunan (Derived Columns)

**rating_percentage:**
```
positive / (positive + negative) * 100
```

**pc_level:**
- 1 = Rendah (Low)
- 2 = Sedang (Medium)
- 3 = Tinggi (High)

### Sumber Data

Steam Games Dataset, diimpor sebagai CSV setelah pra-pemrosesan.

### Langkah Pra-pemrosesan

Sebelum impor:

- Hapus duplikat App ID
- Ganti deskripsi kosong dengan string kosong
- Ganti URL website kosong dengan NULL
- Harga disimpan langsung dalam **IDR** (tanpa konversi USD)
- Konversi rata-rata waktu bermain dari menit ke jam
- Hitung `rating_percentage`
- Tetapkan `pc_level` sebagai INTEGER (1, 2, atau 3)
- Normalisasi nilai genre

### Alur Query

```text
Muat game
      ↓
Saring berdasarkan genre + anggaran
      ↓
Evaluasi Fuzzy Mamdani
      ↓
Hitung skor
      ↓
Urutkan menurun
      ↓
Kembalikan Top 10
```

---

## Prinsip Desain

- Logika bisnis **hanya** di `services/fuzzy`
- Rute hanya: terima input → validasi → panggil layanan → kembalikan respons
- Menambah game baru **tidak** memerlukan perubahan aturan fuzzy
- Tabel basis data tunggal menjaga fokus pada algoritma fuzzy