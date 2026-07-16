from .aggregation import OUTPUT_MFS

# TAHAP 4: DEFUZZIFIKASI
# Mengubah kurva output fuzzy kembali menjadi satu nilai angka tegas (crisp value)

# Jumlah titik sampel yang diambil di bawah kurva (semakin banyak semakin presisi)
SAMPLES = 1000


def centroid(aggregated_strengths):
    # Metode Centroid (Center of Gravity/Area)
    # Menghitung titik pusat massa dari area di bawah kurva fuzzy hasil agregasi
    
    step = 100.0 / SAMPLES
    numerator = 0.0     # Pembilang: jumlah dari (titik x * nilai y)
    denominator = 0.0   # Penyebut: jumlah dari (nilai y)
    
    # Looping melalui rentang skor 0 - 100
    for i in range(SAMPLES + 1):
        x = i * step
        mu = 0.0
        # Untuk titik x ini, cari titik tertinggi (MAX) dari semua kurva kategori 
        # yang telah dipotong (clipped) oleh batas kekuatan rule (strength)
        for cat, strength in aggregated_strengths.items():
            mf = OUTPUT_MFS[cat]
            # Potong (clip) kurva asli dengan nilai kekuatan rule dari tahap inferensi (MIN)
            clipped = min(mf(x), strength)
            # Ambil nilai tertinggi dari seluruh area kategori yang menumpuk (MAX)
            if clipped > mu:
                mu = clipped
                
        # Akumulasi nilai untuk rumus titik berat (centroid)
        numerator += mu * x
        denominator += mu
        
    # Skor akhir (0 - 100) adalah titik pusat massanya (Pembilang / Penyebut)
    return numerator / denominator if denominator > 0 else 0.0
