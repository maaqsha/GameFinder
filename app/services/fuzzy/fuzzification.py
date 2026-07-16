from .membership import (
    BUDGET_LOW, BUDGET_MEDIUM, BUDGET_HIGH,
    PC_LEVEL_LOW, PC_LEVEL_MEDIUM, PC_LEVEL_HIGH,
    GAMER_CASUAL, GAMER_BALANCED, GAMER_HARDCORE,
    PLAYTIME_SHORT, PLAYTIME_MEDIUM, PLAYTIME_LONG,
    triangular,
)

# TAHAP 1: FUZZIFIKASI
# Proses mengubah nilai pasti (crisp value) yang diinputkan pengguna / dari database
# menjadi derajat keanggotaan fuzzy (rentang 0.0 sampai 1.0) untuk setiap kategori.

def fuzzify_budget(price_idr):
    # Mengembalikan derajat keanggotaan harga game ke dalam 3 kategori: Low, Medium, High
    return {
        'Low': BUDGET_LOW(price_idr),
        'Medium': BUDGET_MEDIUM(price_idr),
        'High': BUDGET_HIGH(price_idr),
    }


def fuzzify_pc_level(pc_level):
    # Mengembalikan derajat keanggotaan spesifikasi PC
    return {
        'Low': PC_LEVEL_LOW(pc_level),
        'Medium': PC_LEVEL_MEDIUM(pc_level),
        'High': PC_LEVEL_HIGH(pc_level),
    }


def fuzzify_rating(rating_percentage, preferred_rating):
    # Fuzzifikasi rating game dibandingkan dengan preferensi user yang dinamis (preferred_rating)
    p = max(preferred_rating, 1)
    return {
        'Low': triangular(rating_percentage, 0, 0, p + 20),
        'Medium': triangular(rating_percentage, p - 25, p - 5, p + 25),
        'High': triangular(rating_percentage, p - 15, 100, 100),
    }


def fuzzify_playtime(playtime_hours, preferred_playtime):
    # Fuzzifikasi jam bermain game dibandingkan dengan preferensi user
    p = max(preferred_playtime, 1)
    # Bandingkan waktu bermain game dengan waktu bermain pilihan pengguna.
    # Short = jauh lebih singkat dari pilihan
    # Medium = mendekati pilihan (kecocokan terbaik)
    # Long = jauh lebih lama dari pilihan
    return {
        'Short': triangular(playtime_hours, 0, 0, p * 0.7),
        'Medium': triangular(playtime_hours, p * 0.4, p, p * 1.6),
        'Long': triangular(playtime_hours, p * 1.2, p * 2, p * 2),
    }


def fuzzify_gamer_type(gamer_type):
    # Mengembalikan tipe gamer user
    return {
        'Casual': GAMER_CASUAL(gamer_type),
        'Balanced': GAMER_BALANCED(gamer_type),
        'Hardcore': GAMER_HARDCORE(gamer_type),
    }


def fuzzify_game(price_idr, pc_level, rating_percentage, playtime_hours,
                 preferred_rating=100, preferred_playtime=50,
                 preferred_gamer_type=2):
    # Mengumpulkan dan membungkus semua hasil fuzzifikasi dari masing-masing kriteria 
    # ke dalam satu objek kamus (dictionary) yang akan digunakan di tahap inferensi.
    return {
        'budget': fuzzify_budget(price_idr),
        'pc_level': fuzzify_pc_level(pc_level),
        'gamer_type': fuzzify_gamer_type(preferred_gamer_type),
        'rating': fuzzify_rating(rating_percentage, preferred_rating),
        'playtime': fuzzify_playtime(playtime_hours, preferred_playtime),
    }
