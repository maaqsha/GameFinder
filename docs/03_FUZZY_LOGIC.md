# Desain Logika Fuzzy (Fuzzy Logic Design)

## Tinjauan

Dokumen ini mendefinisikan sistem inferensi fuzzy yang digunakan oleh **Sistem Rekomendasi Game Steam**.

- **Metode:** Fuzzy Mamdani
- **Defuzzifikasi:** Sentroid (Centroid / Center of Area)

---

## Variabel Input

### 1. Anggaran (Budget) — IDR

Rentang: 0 – 1.000.000

Fungsi keanggotaan — segitiga (triangular):

| Kategori | Bentuk (a, b, c) |
|----------|------------------|
| Rendah (Low) | 0, 0, 300.000 |
| Sedang (Medium) | 50.000, 300.000, 700.000 |
| Tinggi (High) | 500.000, 1.000.000, 1.000.000 |

Tumpang tindih:  
- Rendah–Sedang: Rp50.000 – Rp300.000  
- Sedang–Tinggi: Rp500.000 – Rp700.000

---

### 2. Level PC (PC Level)

**Singleton crisp — tidak fuzzy.**  
μ(x) = 1 jika nilai cocok, 0 selain itu.

| Nilai | Makna |
|-------|-------|
| 1 | Rendah (Low) |
| 2 | Sedang (Medium) |
| 3 | Tinggi (High) |

---

### 3. Tipe Gamer (Gamer Type)

Mendefinisikan kombinasi ideal budget / rating / playtime preferensi.

| Tipe | Anggaran | Rating | Waktu Bermain |
|------|----------|--------|---------------|
| Casual | Rendah | Sedang | Sedang |
| Balanced | Sedang | Tinggi | Sedang |
| Hardcore | Tinggi | Tinggi | Sedang |

---

### 4. Rating Pilihan (Preferred Rating) — %

Fungsi keanggotaan segitiga **dinamis** relatif terhadap `preferred_rating` pengguna (p):

| Kategori | Bentuk (a, b, c) |
|----------|------------------|
| Rendah (Low) | 0, 0, p+20 |
| Sedang (Medium) | p-25, p-5, p+25 |
| Tinggi (High) | p-15, 100, 100 |

*Kategori Tinggi memiliki bahu kanan (right shoulder) di 100 (tidak turun ke 0).*

---

### 5. Waktu Bermain Pilihan (Preferred Playtime) — Jam

Waktu bermain dinetralkan — semua tipe gamer menggunakan **Sedang**. Tidak ada data playtime nyata dari dataset.

| Kategori | Bentuk (a, b, c) |
|----------|------------------|
| Pendek (Short) | 0, 0, 20 |
| Sedang (Medium) | 10, 40, 80 |
| Panjang (Long) | 60, 200, 200 |

---

## Variabel Output

### Skor Rekomendasi (Recommendation Score)

Rentang: 0 – 100

| Kategori | Rentang Skor |
|----------|--------------|
| Tidak Direkomendasikan (Not Recommended) | 0 – 25 |
| Kurang Direkomendasikan (Less Recommended) | 20 – 50 |
| Direkomendasikan (Recommended) | 45 – 75 |
| Sangat Direkomendasikan (Highly Recommended) | 70 – 100 |

---

## Proses Inferensi

```text
Masukan Pengguna
      ↓
Fuzzifikasi
      ↓
Evaluasi Aturan (243 aturan)
      ↓
Agregasi
      ↓
Defuzzifikasi Sentroid
      ↓
Skor Rekomendasi
```

---

## Basis Aturan (Rule Base)

- 5 variabel input
- 3 fungsi keanggotaan per input
- Total: **3⁵ = 243 aturan**
- Setiap kombinasi tertutup tepat sekali

### Format Aturan

```
IF Anggaran IS Rendah
AND Level_PC IS Rendah
AND Tipe_Gamer IS Casual
AND Rating IS Rendah
AND Waktu_Bermain IS Sedang
THEN Rekomendasi IS Kurang_Direkomendasikan
```

### Perhitungan Output

Setiap game dievaluasi secara independen. Skor diambil dari sentroid keluaran teragregasi di 4 kategori.

### Pemetaan Pencocokan (Match Counting → Kategori)

| Jumlah Cocok | Indeks Kategori |
|--------------|-----------------|
| 3/3 | 3 — Sangat Direkomendasikan |
| 2/3 | 2 — Direkomendasikan |
| 1/3 | 1 — Kurang Direkomendasikan |
| 0/3 | 0 — Tidak Direkomendasikan |

**3 dimensi yang dihitung:** kecocokan anggaran, kecocokan rating, kecocokan waktu bermain.  
*Level PC ada di antecedent (firing via `min()`) tapi dikecualikan dari penghitungan cocok — karena merepresentasikan kemampuan hardware, bukan preferensi.*

---

## Prioritas Keputusan

1. **Tipe Gamer** — menentukan profil ideal anggaran/rating/waktu bermain
2. **Rating** — game dengan rating lebih tinggi diprioritaskan
3. **Anggaran** — game dalam jangkauan anggaran diprioritaskan
4. **Waktu Bermain** — dinetralkan (semua profil menggunakan Sedang)

---

## Basis Pengetahuan (Knowledge Base)

### KB-01: Kesesuaian Tipe Gamer
Tipe gamer prioritas tertinggi — mendefinisikan kombinasi ideal anggaran/rating/waktu bermain.

### KB-02: Anggaran
Game dalam jangkauan anggaran pengguna diprioritaskan. Game melebihi anggaran mendapat skor lebih rendah.

### KB-03: Rating
Rating Steam yang lebih tinggi lebih disukai. Game berating rendah jarang mendapat rekomendasi tinggi.

### KB-04: Waktu Bermain
Waktu bermain yang cocok dengan preferensi mendapat skor lebih tinggi. Saat ini dinetralkan (tidak ada data playtime nyata).

### KB-05: Genre
Genre **BUKAN** variabel fuzzy. Hanya digunakan sebagai penyaring SQL sebelum inferensi fuzzy.

### KB-06: Urutan Prioritas
1. Tipe Gamer → 2. Rating → 3. Anggaran → 4. Waktu Bermain

### KB-07: Sangat Direkomendasikan
Hanya ketika hampir semua kriteria cocok dengan preferensi pengguna.

### KB-08: Direkomendasikan
Ketika sebagian besar kriteria cocok tanpa ketidakcocokan kritis.

### KB-09: Kurang Direkomendasikan
Ketika beberapa kriteria cocok parsial atau satu+ faktor penting mengurangi kecocokan.

### KB-10: Tidak Direkomendasikan
Ketidakcocokan mayor pada tipe gamer, rating rendah, atau banyak kriteria tidak terpenuhi.

### KB-11: Interpretasi Skor
Lihat tabel variabel output di atas.

### KB-12: Konsistensi Aturan
Masukan serupa menghasilkan keluaran serupa. Tidak ada aturan yang bertentangan. Setiap kombinasi masukan memetakan ke tepat satu keluaran.

### KB-13: Skalabilitas
Menambah game baru **tidak** memerlukan perubahan basis aturan fuzzy.

### KB-14: Dapat Dijelaskan (Explainability)
Setiap rekomendasi harus dapat dijelaskan menggunakan aturan pengetahuan ini, bukan penilaian sembarangan.

---

## Keputusan Desain

- Genre adalah penyaring basis data saja — bukan input fuzzy
- Level PC berada di antecedent tapi dikecualikan dari penghitungan cocok (hardware, bukan preferensi)
- Waktu bermain dinetralkan via `playtime_hours = preferred_playtime` — menjaga arsitektur 243-aturan utuh tanpa data buatan
- Tipe gamer mewakili preferensi pemain, bukan kemampuan hardware
- Fungsi keanggotaan input yang tumpang tindih menciptakan firing multi-kategori, menghasilkan sebaran skor kontinu via sentroid

---

## Kriteria Penerimaan

- Semua variabel input berpartisipasi dalam inferensi
- Setiap kombinasi masukan cocok dengan minimal satu aturan
- Setiap game yang dievaluasi menerima skor rekomendasi
- Skor dalam rentang 0–100
- Top 10 dikembalikan terurut menurun berdasarkan skor