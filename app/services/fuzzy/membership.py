# Fungsi Keanggotaan Segitiga (Triangular Membership Function)
# Menghitung derajat keanggotaan (0.0 sampai 1.0) untuk sebuah nilai x
# berdasarkan batas bawah (a), titik puncak (b), dan batas atas (c)
def triangular(x, a, b, c):
    # Jika bentuknya siku-siku kiri (batas bawah sama dengan puncak) dan x lebih kecil dari a
    if a == b and x <= a:
        return 1.0
    # Jika bentuknya siku-siku kanan (puncak sama dengan batas atas) dan x lebih besar dari c
    if b == c and x >= c:
        return 1.0
    # Jika x berada di luar rentang kurva
    if x <= a or x >= c:
        return 0.0
    # Menghitung kemiringan garis naik (sisi kiri segitiga)
    if x < b:
        return (x - a) / (b - a)
    # Menghitung kemiringan garis turun (sisi kanan segitiga)
    if x > b:
        return (c - x) / (c - b)
    # Jika x tepat berada di titik puncak (x == b)
    return 1.0


# --- FUNGSI KEANGGOTAAN UNTUK BUDGET (Anggaran) ---
BUDGET_LOW = lambda x: triangular(x, 0, 0, 300000)            # Murah: 0 - 300rb
BUDGET_MEDIUM = lambda x: triangular(x, 50000, 300000, 700000)# Sedang: 50rb - 700rb
BUDGET_HIGH = lambda x: triangular(x, 500000, 1000000, 1000000)# Mahal: 500rb - 1jt+


# --- FUNGSI KEANGGOTAAN UNTUK PC LEVEL (Spesifikasi PC) ---
# Menggunakan logika singleton (hanya bernilai 1 jika persis sama)
PC_LEVEL_LOW = lambda x: 1.0 if x == 1 else 0.0               # Low End
PC_LEVEL_MEDIUM = lambda x: 1.0 if x == 2 else 0.0            # Mid End
PC_LEVEL_HIGH = lambda x: 1.0 if x == 3 else 0.0              # High End


# --- FUNGSI KEANGGOTAAN UNTUK PLAYTIME (Waktu Bermain) ---
PLAYTIME_SHORT = lambda x: triangular(x, 0, 0, 20)            # Singkat: 0 - 20 Jam
PLAYTIME_MEDIUM = lambda x: triangular(x, 10, 45, 80)         # Sedang: 10 - 80 Jam
PLAYTIME_LONG = lambda x: triangular(x, 60, 130, 200)         # Lama: 60 - 200 Jam


# --- FUNGSI KEANGGOTAAN UNTUK GAMER TYPE (Tipe Pemain) ---
# Menggunakan logika singleton (hanya bernilai 1 jika persis sama)
GAMER_CASUAL = lambda x: 1.0 if x == 1 else 0.0               # Kasual
GAMER_BALANCED = lambda x: 1.0 if x == 2 else 0.0             # Seimbang (Balanced)
GAMER_HARDCORE = lambda x: 1.0 if x == 3 else 0.0             # Hardcore


# --- FUNGSI KEANGGOTAAN UNTUK OUTPUT REKOMENDASI ---
# Merupakan kurva output yang akan dievaluasi dan didefuzzifikasi di akhir
REC_NOT = lambda x: triangular(x, 0, 0, 25)                   # Tidak Direkomendasikan
REC_LESS = lambda x: triangular(x, 20, 35, 50)                # Kurang Direkomendasikan
REC_YES = lambda x: triangular(x, 45, 60, 75)                 # Direkomendasikan
REC_HIGH = lambda x: triangular(x, 70, 100, 100)              # Sangat Direkomendasikan
