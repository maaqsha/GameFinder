from .membership import REC_NOT, REC_LESS, REC_YES, REC_HIGH

# Memetakan kategori output ke fungsi keanggotaan kurva outputnya masing-masing
OUTPUT_MFS = {
    'Not Recommended': REC_NOT,
    'Less Recommended': REC_LESS,
    'Recommended': REC_YES,
    'Highly Recommended': REC_HIGH,
}


# TAHAP 3: AGREGASI
def aggregate(rule_strengths):
    # Proses menggabungkan (mengagregasi) semua hasil rule (α-predikat)
    # dari tahap inferensi. Mengembalikan dictionary yang berisi batas maksimal (MAX)
    # derajat kebenaran untuk setiap kategori kurva output.
    return {
        cat: rule_strengths.get(cat, 0.0)
        for cat in OUTPUT_MFS
    }
