# 📊 Materi Presentasi: GameFinder
## Sistem Rekomendasi Game Steam Menggunakan Metode Fuzzy Mamdani

---

# 1. PERMASALAHAN YANG DIANGKAT (Latar Belakang)

## 1.1 Masalah Utama
Platform Steam memiliki **lebih dari 70.000+ judul game** yang tersedia. Pengguna (terutama gamer pemula) sering mengalami **information overload** — kebingungan dalam memilih game yang tepat karena banyaknya pilihan.

## 1.2 Tantangan Spesifik yang Dihadapi Pengguna
| No | Permasalahan | Penjelasan |
|----|-------------|-----------|
| 1 | **Keterbatasan Anggaran** | Mahasiswa/pelajar memiliki budget terbatas, tidak bisa asal beli game mahal |
| 2 | **Keterbatasan Spesifikasi PC** | Banyak game yang tidak bisa dijalankan di PC/Laptop spesifikasi rendah |
| 3 | **Rating yang Membingungkan** | Rating game di Steam bervariasi, pengguna sulit menilai mana yang benar-benar bagus |
| 4 | **Waktu Bermain Tidak Sesuai** | Pengguna kasual tidak ingin game 100+ jam, sementara gamer hardcore butuh game panjang |
| 5 | **Multi-Kriteria** | Manusia kesulitan mempertimbangkan 4–5 kriteria secara bersamaan dan objektif |

## 1.3 Mengapa Masalah Ini Penting?
- Membeli game yang salah = **uang terbuang** dan **waktu terbuang**
- Tidak ada sistem di Steam yang secara cerdas mencocokan **profil pengguna** (anggaran, spek PC, gaya bermain) dengan game secara bersamaan
- Sistem rekomendasi bawaan Steam hanya berbasis riwayat pembelian dan popularitas, bukan berdasarkan **analisis multi-kriteria**

---

# 2. PERMASALAHAN YANG DISELESAIKAN OLEH SISTEM

## 2.1 Solusi yang Ditawarkan
GameFinder adalah **Sistem Pendukung Keputusan (Decision Support System)** berbasis web yang menggunakan **Logika Fuzzy Mamdani** untuk merekomendasikan game Steam terbaik berdasarkan profil pengguna.

## 2.2 Apa yang Dilakukan Sistem
| Fitur | Penjelasan |
|-------|-----------|
| **Input Multi-Kriteria** | Pengguna memasukkan 5 kriteria sekaligus (Anggaran, Spek PC, Tipe Gamer, Rating, Waktu Bermain) |
| **Evaluasi Fuzzy** | Setiap game dievaluasi menggunakan 243 aturan Fuzzy Mamdani |
| **Skor Kecocokan** | Setiap game mendapat skor 0-100% yang menunjukkan tingkat kecocokan |
| **Explainable AI** | Sistem memberikan **alasan** mengapa game direkomendasikan (bukan black-box) |
| **Top 10 Ranking** | Menampilkan 10 game terbaik yang paling cocok untuk pengguna |

## 2.3 Keunggulan Dibandingkan Sistem Lain
- **Transparan:** Pengguna tahu *mengapa* game X direkomendasikan (karena harga cocok, spek PC cukup, dll.)
- **Tidak perlu akun/login:** Langsung pakai tanpa registrasi
- **Multi-kriteria sekaligus:** Tidak hanya berdasarkan 1 faktor, tapi 5 faktor bersamaan
- **Toleransi ketidakpastian:** Logika Fuzzy bisa menangani nilai "abu-abu" (misal: harga *agak* mahal, bukan cuma *mahal* atau *murah*)

---

# 3. TEORI METODE FUZZY MAMDANI

## 3.1 Apa Itu Logika Fuzzy?
Logika Fuzzy adalah cabang dari kecerdasan buatan yang memungkinkan sebuah nilai memiliki **derajat kebenaran antara 0 dan 1**, bukan hanya 0 (Salah) atau 1 (Benar) seperti logika klasik (Boolean).

**Contoh Sederhana:**
- Logika Klasik: Harga Rp 250.000 → **Murah** (Ya/Tidak?)
- Logika Fuzzy: Harga Rp 250.000 → **83% Murah** DAN **17% Sedang** (bisa keduanya secara bersamaan!)

## 3.2 Apa Itu Metode Mamdani?
Metode Mamdani (Mamdani Inference System) dikembangkan oleh **Ebrahim H. Mamdani** pada tahun 1975. Metode ini merupakan salah satu metode inferensi fuzzy yang paling populer dan paling banyak digunakan.

Ciri khas utama metode Mamdani:
- Menggunakan aturan **IF-THEN** berbasis linguistik (bahasa manusia)
- Operator **MIN** untuk implikasi (AND pada bagian IF)
- Operator **MAX** untuk agregasi (menggabungkan beberapa aturan)
- **Defuzzifikasi** menggunakan metode **Centroid (Pusat Area)**

## 3.3 Empat Tahapan Proses Fuzzy Mamdani

### Tahap 1: FUZZIFIKASI
> Mengubah nilai tegas (crisp) menjadi derajat keanggotaan fuzzy (0.0 - 1.0)

Pada tahap ini, angka pasti dari input dikonversi menjadi nilai keanggotaan menggunakan **Fungsi Keanggotaan (Membership Function)** berbentuk segitiga (triangular).

**Rumus Fungsi Segitiga:**

$$
\mu(x) = \begin{cases}
0, & \text{jika } x \leq a \text{ atau } x \geq c \\
\dfrac{x - a}{b - a}, & \text{jika } a < x < b \\
\dfrac{c - x}{c - b}, & \text{jika } b < x < c \\
1, & \text{jika } x = b
\end{cases}
$$

Dimana: $a$ = batas kiri, $b$ = titik puncak, $c$ = batas kanan

### Tahap 2: INFERENSI (Evaluasi Aturan)
> Mencocokkan nilai fuzzifikasi dengan basis aturan IF-THEN

Sistem menggunakan **243 aturan** yang mengkombinasikan 5 variabel input.

**Format Aturan:**
```
JIKA Budget ADALAH [Rendah/Sedang/Tinggi]
DAN  Level PC ADALAH [Rendah/Sedang/Tinggi]
DAN  Tipe Gamer ADALAH [Casual/Balanced/Hardcore]
DAN  Rating ADALAH [Rendah/Sedang/Tinggi]
DAN  Waktu Bermain ADALAH [Singkat/Sedang/Lama]
MAKA Rekomendasi ADALAH [Tidak Direkomendasikan / Kurang Direkomendasikan / Direkomendasikan / Sangat Direkomendasikan]
```

**Operator yang digunakan:** Fungsi **MIN** (nilai minimum) untuk operator AND.

$$
\alpha\text{-predikat} = \min(\mu_{\text{budget}},\ \mu_{\text{pc\_level}},\ \mu_{\text{gamer\_type}},\ \mu_{\text{rating}},\ \mu_{\text{playtime}})
$$

### Tahap 3: AGREGASI
> Menggabungkan semua aturan yang terpicu menjadi satu area kurva

Jika beberapa aturan menghasilkan kategori output yang sama, sistem mengambil nilai **MAX** (nilai tertinggi) dari kekuatan aturan tersebut.

$$
\mu_{\text{output}}(\text{kategori}) = \max(\alpha_1,\ \alpha_2,\ \alpha_3,\ \dots,\ \alpha_n)
$$

### Tahap 4: DEFUZZIFIKASI (Metode Centroid)
> Mengubah area fuzzy menjadi satu nilai tegas (crisp) sebagai output akhir

Metode **Centroid (Pusat Area / Center of Area)** menghitung titik pusat massa dari area di bawah kurva gabungan.

**Rumus Centroid (kontinu):**

$$
z^* = \frac{\displaystyle\int x \cdot \mu(x)\, dx}{\displaystyle\int \mu(x)\, dx}
$$

**Implementasi diskrit (pada kode, 1000 titik sampel pada rentang 0–100):**

$$
z^* = \frac{\displaystyle\sum_{i=0}^{1000} x_i \cdot \mu(x_i)}{\displaystyle\sum_{i=0}^{1000} \mu(x_i)}
$$

Hasil defuzzifikasi ini adalah **Skor Rekomendasi (0 - 100)**.

---

# 4. CARA KERJA CODINGAN (Arsitektur Sistem)

## 4.1 Struktur File Fuzzy Engine
```
app/services/fuzzy/
├── membership.py          ← Fungsi keanggotaan segitiga (kurva)
├── fuzzification.py       ← Mengubah angka crisp → derajat keanggotaan
├── inference.py           ← 243 aturan IF-THEN + evaluasi aturan
├── aggregation.py         ← Menggabungkan aturan (operator MAX)
├── defuzzification.py     ← Menghitung centroid → skor akhir (0-100)
└── recommendation.py      ← Orkestrasi keseluruhan + koneksi database
```

## 4.2 Alur Kode Program (Step-by-Step)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. PENGGUNA mengisi form (recommend.html)                   │
│    → Budget, PC Level, Tipe Gamer, Rating, Waktu Bermain,   │
│      Genre                                                  │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. FILTER DATABASE (recommendation.py)                      │
│    → Query MySQL: SELECT games WHERE genre LIKE '%Action%'  │
│    → Membuang game yang genre-nya tidak sesuai              │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. FUZZIFIKASI (fuzzification.py + membership.py)           │
│    → Setiap game dikonversi ke derajat keanggotaan          │
│    → Contoh: Harga Rp 200.000 → {Low: 0.33, Med: 0.23}     │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. INFERENSI (inference.py)                                 │
│    → Evaluasi 243 aturan menggunakan operator MIN           │
│    → Menentukan kekuatan (strength) setiap kategori output  │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. AGREGASI (aggregation.py)                                │
│    → Menggabungkan kekuatan aturan (operator MAX)           │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. DEFUZZIFIKASI (defuzzification.py)                       │
│    → Metode Centroid → Skor kecocokan (misal: 78.5)         │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. PERINGKAT & OUTPUT (recommendation.py → results.html)    │
│    → Urutkan skor tertinggi → terendah                      │
│    → Ambil Top 10 game                                      │
│    → Tampilkan di browser beserta alasannya                 │
└─────────────────────────────────────────────────────────────┘
```

## 4.3 Variabel Fuzzy yang Digunakan

### Variabel Input (5 variabel)
| No | Variabel | Himpunan Fuzzy | Rentang |
|----|----------|---------------|---------|
| 1 | **Anggaran (Budget)** | Rendah, Sedang, Tinggi | Rp 0 – Rp 1.000.000 |
| 2 | **Level PC** | Rendah, Sedang, Tinggi | 1, 2, 3 (singleton) |
| 3 | **Tipe Gamer** | Casual, Balanced, Hardcore | 1, 2, 3 (singleton) |
| 4 | **Rating** | Rendah, Sedang, Tinggi | 0% – 100% |
| 5 | **Waktu Bermain** | Singkat, Sedang, Lama | 0 – 200 jam |

### Variabel Output (1 variabel)
| Kategori Output | Rentang Skor |
|----------------|-------------|
| Tidak Direkomendasikan | 0 – 25 |
| Kurang Direkomendasikan | 20 – 50 |
| Direkomendasikan | 45 – 75 |
| Sangat Direkomendasikan | 70 – 100 |

### Total Aturan Fuzzy

$$
3_{\text{(budget)}} \times 3_{\text{(pc\_level)}} \times 3_{\text{(gamer\_type)}} \times 3_{\text{(rating)}} \times 3_{\text{(playtime)}} = 243 \text{ Aturan}
$$

---

# 5. CONTOH INPUT → PROSES → OUTPUT

## 5.1 Skenario: Mahasiswa Mencari Game Action

### 📥 INPUT (Pengguna memasukkan preferensi di form web)
| Parameter | Nilai yang Dimasukkan |
|-----------|----------------------|
| **Anggaran** | Rp 300.000 |
| **Spesifikasi PC** | Medium (Mid-End) |
| **Tipe Gamer** | Balanced (Seimbang) |
| **Rating Minimum** | 75% |
| **Waktu Bermain** | 30 Jam |
| **Genre** | Action |

---

### ⚙️ PROSES (Apa yang terjadi di dalam sistem)

#### Langkah 1: Filter Database
```sql
SELECT * FROM games 
WHERE (genre LIKE '%Action%' OR tags LIKE '%Action%') 
  AND total_reviews >= 5 
  AND price_idr <= 300000
```
**Hasil:** Misalnya ditemukan 85 game Action yang sesuai budget.

---

#### Langkah 2: Fuzzifikasi (untuk game peringkat #1)

**Contoh Game Kandidat: "Nuclear Option" (Harga: Rp 287.840, Rating: 94%, 7.024 ulasan)**

**A. Fuzzifikasi Budget (Harga game Rp 287.840):**

Menggunakan fungsi keanggotaan segitiga dari `membership.py`:

$$
\mu_{\text{Low}}(287840) = \frac{c - x}{c - b} = \frac{300000 - 287840}{300000 - 0} = 0.04
$$

$$
\mu_{\text{Medium}}(287840) = \frac{x - a}{b - a} = \frac{287840 - 50000}{300000 - 50000} = 0.95
$$

$$
\mu_{\text{High}}(287840) = 0.00 \quad \text{(di luar rentang, } x < a = 500000\text{)}
$$

**Hasil Fuzzifikasi Budget:**

$$
\text{Budget} = \{ \text{Low}: 0.04,\quad \text{Medium}: 0.95,\quad \text{High}: 0.00 \}
$$

**B. Fuzzifikasi Level PC (Game butuh level 3/High, User punya level 2/Medium):**

$$
\text{PC Level} = \{ \text{Low}: 0.0,\quad \text{Medium}: 1.0,\quad \text{High}: 0.0 \}
$$

*(Singleton: nilai PC pengguna = 2, maka hanya Medium = 1.0)*

**C. Fuzzifikasi Tipe Gamer (User memilih Balanced = 2):**

$$
\text{Gamer Type} = \{ \text{Casual}: 0.0,\quad \text{Balanced}: 1.0,\quad \text{Hardcore}: 0.0 \}
$$

**D. Fuzzifikasi Rating (Rating game 94%, preferensi user 75%):**

$$
\mu_{\text{High}}(94) = \frac{x - a}{b - a} = \frac{94 - (75-15)}{100 - (75-15)} = \frac{94 - 60}{40} = 0.85
$$

$$
\text{Rating} = \{ \text{Low}: 0.0,\quad \text{Medium}: 0.0,\quad \text{High}: 0.85 \}
$$

*(94% jauh di atas preferensi 75%, masuk kategori High)*

**E. Fuzzifikasi Waktu Bermain (Game ~30 jam, preferensi user 30 jam):**

$$
\text{Playtime} = \{ \text{Short}: 0.0,\quad \text{Medium}: 1.0,\quad \text{Long}: 0.0 \}
$$

*(30 jam = tepat di titik puncak preferensi 30 jam, kecocokan sempurna)*

---

#### Langkah 3: Inferensi (Evaluasi Aturan)

Dari 243 aturan, yang paling relevan untuk game ini misalnya:

**Aturan #X:**
```
JIKA Budget = Medium (0.95)
DAN  PC Level = Medium (1.0)
DAN  Gamer Type = Balanced (1.0)
DAN  Rating = High (0.85)
DAN  Playtime = Medium (1.0)
MAKA Rekomendasi = Sangat Direkomendasikan
```

**Menghitung α-predikat (menggunakan operator MIN):**

$$
\alpha = \min(0.95,\ 1.0,\ 1.0,\ 0.85,\ 1.0) = 0.85
$$
*(Nilai terkecil dari semua kondisi yang terpenuhi)*

Profil ideal untuk tipe Balanced: `{budget: Medium, rating: High, playtime: Medium}`
- Budget game = Medium, ideal Balanced = Medium → **cocok** ✓
- Rating game = High, ideal Balanced = High → **cocok** ✓
- Playtime game = Medium, ideal Balanced = Medium → **cocok** ✓

Kecocokan = 3 dari 3 → consequent = **Sangat Direkomendasikan** (index 3)

Maka kekuatan aturan ini untuk kategori "Sangat Direkomendasikan" = 0.85

---

#### Langkah 4: Agregasi

Setelah **semua 243 aturan** dievaluasi, hasil agregasi (MAX dari setiap kategori):
```
Strengths = {
    'Not Recommended':    0.00,
    'Less Recommended':   0.04,
    'Recommended':        0.85,
    'Highly Recommended': 0.85,   ← Nilai tertinggi
}
```

---

#### Langkah 5: Defuzzifikasi (Centroid)

Sistem menghitung titik pusat massa (centroid) dari area di bawah kurva.

Untuk setiap titik sampel $x_i$ pada rentang 0–100 (1000 sampel):

$$
\mu(x_i) = \max_{\text{kategori}} \left( \min\left( \mu_{\text{mf\_kategori}}(x_i),\ \alpha_{\text{kategori}} \right) \right)
$$

Lalu hitung centroid:

$$
z^* = \frac{\displaystyle\sum_{i=0}^{1000} x_i \cdot \mu(x_i)}{\displaystyle\sum_{i=0}^{1000} \mu(x_i)}
$$

**Hasil Defuzzifikasi: Skor = 79.0**

---

#### Langkah 6: Kategorisasi Skor

$$
z^* = 79.0 \implies 70 \leq 79.0 \leq 100 \implies \text{Kategori: \textbf{Sangat Direkomendasikan}} \checkmark
$$

---

### 📤 OUTPUT (Ditampilkan di browser pengguna)

Setelah semua game Action dievaluasi satu per satu, sistem mengurutkan skor tertinggi dan menampilkan **Top 10**:

| Peringkat | Nama Game | Harga | Rating | Ulasan | Skor | Kategori |
|-----------|-----------|-------|--------|--------|------|----------|
| #1 | Nuclear Option | Rp 287.840 | 94% | 7.024 | 79% | Sangat Direkomendasikan |
| #2 | Dome Keeper | Rp 287.840 | 91% | 16.108 | 77% | Sangat Direkomendasikan |
| #3 | Life is Strange: True Colors | Rp 287.840 | 88% | 12.015 | 75% | Direkomendasikan |
| #4 | Over The Top: WWI | Rp 260.160 | 88% | 3.572 | 72% | Direkomendasikan |
| #5 | Castle Crashers® | Rp 239.840 | 95% | 105.576 | 72% | Direkomendasikan |
| #6 | DRAGON BALL FighterZ | Rp 230.240 | 91% | 53.794 | 69% | Direkomendasikan |
| #7 | People Playground | Rp 159.840 | 97% | 288.135 | 69% | Direkomendasikan |
| #8 | Crime Simulator | Rp 239.840 | 85% | 4.499 | 68% | Direkomendasikan |
| #9 | End of Zoe | Rp 239.840 | 85% | 1.190 | 68% | Direkomendasikan |
| #10 | LORT | Rp 239.840 | 83% | 2.759 | 68% | Direkomendasikan |

**Beserta Alasan untuk Setiap Game (Explainable AI):**
- ✅ "Cocok untuk gaya bermain Seimbang"
- ✅ "Rp 287.840 sesuai dengan anggaran Rp 300.000 Anda"
- ✅ "Rating 94% memenuhi preferensi 75% Anda"
- ⚠️ "Game ini membutuhkan spesifikasi High End (mungkin berat untuk PC Anda)"

---

# 6. REFERENSI JURNAL

## 6.1 Referensi Utama (Pencetus Metode)

> **[1]** E. H. Mamdani and S. Assilian, *"An experiment in linguistic synthesis with a fuzzy logic controller,"* International Journal of Man-Machine Studies, Vol. 7, No. 1, pp. 1-13, **1975**.
> 
> *(Makalah asli yang memperkenalkan metode Mamdani untuk pertama kalinya)*

> **[2]** L. A. Zadeh, *"Fuzzy Sets,"* Information and Control, Vol. 8, No. 3, pp. 338-353, **1965**.
> 
> *(Makalah dasar teori Fuzzy Sets oleh Lotfi Zadeh — bapak Logika Fuzzy)*

## 6.2 Referensi Pendukung (Penerapan Sistem Rekomendasi + Fuzzy)

> **[3]** S. Kusumadewi and H. Purnomo, *"Aplikasi Logika Fuzzy untuk Pendukung Keputusan,"* Graha Ilmu, Yogyakarta, **2010**.
> 
> *(Buku referensi utama berbahasa Indonesia tentang penerapan logika fuzzy dalam sistem pendukung keputusan)*

> **[4]** T. J. Ross, *"Fuzzy Logic with Engineering Applications,"* John Wiley & Sons, 3rd Edition, **2010**.
> 
> *(Buku referensi internasional tentang dasar teori dan aplikasi logika fuzzy)*

> **[5]** F. Ricci, L. Rokach, B. Shapira, and P. B. Kantor, *"Recommender Systems Handbook,"* Springer, **2011**.
> 
> *(Buku referensi tentang berbagai metode sistem rekomendasi)*

> **[6]** J. M. Mendel, *"Fuzzy Logic Systems for Engineering: A Tutorial,"* Proceedings of the IEEE, Vol. 83, No. 3, pp. 345-377, **1995**.
> 
> *(Tutorial komprehensif tentang sistem logika fuzzy untuk aplikasi engineering)*

---

# 7. BATASAN / KEKURANGAN SISTEM

| No | Kekurangan | Penjelasan |
|----|-----------|-----------|
| 1 | **Data Statis** | Database game diimpor secara manual (tidak real-time dari Steam API) |
| 2 | **Genre Bukan Variabel Fuzzy** | Genre hanya digunakan sebagai filter kasar, tidak dievaluasi dalam logika fuzzy |
| 3 | **Tidak Ada Personalisasi** | Sistem tidak menyimpan riwayat pencarian pengguna (tanpa akun/login) |
| 4 | **Spek PC Diestimasi** | Level PC game ditentukan dari tags/genre (bukan dari data system requirements resmi) |
| 5 | **Jumlah Aturan Besar** | 243 aturan sulit dikelola manual jika variabel bertambah (skalabilitas terbatas) |

---

# 8. RINGKASAN UNTUK PENUTUP PRESENTASI

## Kesimpulan
1. GameFinder berhasil mengimplementasikan **metode Fuzzy Mamdani** sebagai mesin inferensi untuk sistem rekomendasi game Steam.
2. Sistem menggunakan **5 variabel input** dan **243 aturan fuzzy** untuk mengevaluasi kecocokan setiap game dengan profil pengguna.
3. Proses **Fuzzifikasi → Inferensi → Agregasi → Defuzzifikasi (Centroid)** menghasilkan skor rekomendasi 0-100 yang dapat dijelaskan (*Explainable AI*).
4. Sistem menampilkan **Top 10 game** terbaik beserta alasan rekomendasinya.

## Saran Pengembangan
1. Integrasi dengan **Steam API** untuk data game real-time
2. Penambahan **fitur akun pengguna** untuk personalisasi riwayat
3. Penggunaan **metode hybrid** (Fuzzy + Machine Learning) untuk akurasi lebih tinggi
4. Penambahan variabel fuzzy baru seperti **popularitas** dan **umur game**
