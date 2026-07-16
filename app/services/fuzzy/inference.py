OUTPUT_CATEGORIES = ['Not Recommended', 'Less Recommended', 'Recommended', 'Highly Recommended']

# Himpunan linguistik untuk setiap variabel (berkaitan dengan fuzzifikasi)
LABELS = {
    'budget': ['Low', 'Medium', 'High'],
    'pc_level': ['Low', 'Medium', 'High'],
    'gamer_type': ['Casual', 'Balanced', 'Hardcore'],
    'rating': ['Low', 'Medium', 'High'],
    'playtime': ['Short', 'Medium', 'Long'],
}

# Profil ideal dari masing-masing tipe gamer
GAMER_PROFILES = {
    'Casual': {'budget': 'Low', 'rating': 'Medium', 'playtime': 'Medium'},
    'Balanced': {'budget': 'Medium', 'rating': 'High', 'playtime': 'Medium'},
    'Hardcore': {'budget': 'High', 'rating': 'High', 'playtime': 'Medium'},
}


def _get_output(budget, pc, gamer, rating, playtime):
    # Menentukan hasil (consequent) dari kombinasi variabel berdasarkan kecocokan (matches) 
    # terhadap profil ideal gamer. Semakin banyak yang cocok, semakin direkomendasikan (0-3).
    ideal = GAMER_PROFILES[gamer]
    matches = sum([
        budget == ideal['budget'],
        rating == ideal['rating'],
        playtime == ideal['playtime'],
    ])
    # Mengembalikan indeks dari OUTPUT_CATEGORIES (0 sampai 3)
    return {3: 3, 2: 2, 1: 1, 0: 0}.get(matches, 0)


def generate_rules():
    """
    Fungsi ini membangkitkan (generate) basis aturan (rule base) secara dinamis.
    Daripada menulis 243 aturan (IF-THEN) secara manual, sistem menggunakan 
    5 tingkat perulangan (nested loops) untuk mengkombinasikan semua himpunan variabel.
    Total Kombinasi: 3 (budget) x 3 (pc_level) x 3 (gamer_type) x 3 (rating) x 3 (playtime) = 243 Aturan.
    """
    rules = []
    for b in LABELS['budget']:
        for p in LABELS['pc_level']:
            for g in LABELS['gamer_type']:
                for r in LABELS['rating']:
                    for pt in LABELS['playtime']:
                        # Menentukan output kesimpulan (consequent) yang cocok untuk kombinasi ini
                        idx = _get_output(b, p, g, r, pt)
                        
                        # Membentuk aturan dan menyimpannya ke dalam memori array (rules)
                        # 'antecedent' merepresentasikan bagian kondisi prasyarat (IF)
                        # 'consequent' merepresentasikan bagian hasil/kesimpulan (THEN)
                        rules.append({
                            'antecedent': {
                                'budget': b, 'pc_level': p,
                                'gamer_type': g,
                                'rating': r, 'playtime': pt,
                            },
                            'consequent': OUTPUT_CATEGORIES[idx],
                        })
    return rules


# TAHAP 2: INFERENSI
def evaluate_rules(fuzzy_inputs, rules):
    # Mengevaluasi semua aturan dan mencari nilai α-predikat (kekuatan aturan)
    # Menyimpan kekuatan maksimal (firing strength) untuk setiap kategori output
    strengths = {cat: 0.0 for cat in OUTPUT_CATEGORIES}
    
    for rule in rules:
        ant = rule['antecedent']
        # Menggunakan operator MIN (karena menggunakan logika AND) untuk mencari 
        # nilai terkecil dari derajat keanggotaan pada antecedent. Ini disebut α-predikat.
        firing = min(
            fuzzy_inputs['budget'][ant['budget']],
            fuzzy_inputs['pc_level'][ant['pc_level']],
            fuzzy_inputs['gamer_type'][ant['gamer_type']],
            fuzzy_inputs['rating'][ant['rating']],
            fuzzy_inputs['playtime'][ant['playtime']],
        )
        # Jika nilai firing (kekuatan aturan) saat ini lebih besar dari yang sudah tersimpan
        # di kategori output tersebut, maka perbarui (Operator MAX secara implisit dilakukan di sini)
        if firing > strengths[rule['consequent']]:
            strengths[rule['consequent']] = firing
            
    # Mengembalikan nilai maksimum α-predikat untuk masing-masing kategori output
    return strengths