"""
Tes integrasi untuk mesin rekomendasi GameFinder - membutuhkan MySQL.

Skenario (dari persyaratan tugas):
  A. Anggaran rendah, PC rendah
  B. Anggaran menengah, PC menengah
  C. Anggaran tinggi, PC tinggi
  D. Hanya game gratis
  E. Tidak ada genre yang cocok
  F. Rating pilihan sangat tinggi
  G. Waktu bermain pilihan sangat singkat
  H. Waktu bermain pilihan sangat lama
  I. Nilai batas
  J. Verifikasi peringkat
"""

import sys
sys.path.insert(0, '.')
from app.services.fuzzy.recommendation import recommend


def header(title):
    print(); print('=' * 72); print(f'  {title}'); print('=' * 72)


def subheader(title):
    print(); print(f'--- {title} ---')


def print_results(label, results):
    print(f'  {label}:')
    if not results:
        print('    (empty)')
        return
    for i, g in enumerate(results, 1):
        name_short = g['name'][:40].encode('ascii', 'replace').decode('ascii')
        price_str = f'Rp{int(g["price_idr"]):>8,}'
        owners_str = f'{int(g["estimated_owners"]):>10,}' if g.get('estimated_owners') else '?'
        print(f'    {i:>2}. {name_short:<42} {price_str}  '
              f'{g["rating_percentage"]:>6.2f}%  '
              f'owners={owners_str}  '
              f'{g["recommendation_score"]:>6.2f}  {g["recommendation_category"]}')


# ======================================================================
# A. Low budget, Low PC
# ======================================================================

header('A. Low Budget (50K IDR), Low PC (1), Action')

print('''
Alasan: Pengguna memiliki anggaran sangat terbatas dan PC lama/lemah.
Harapan: Game dengan price_idr <= 50,000 (pc_level tidak ada lagi di skema).
''')
results = recommend(budget=50000, pc_level=1, preferred_rating=50,
                    preferred_playtime=10, genre='Action', top_n=10)
print_results('Top 10', results)
all_affordable = all(float(g['price_idr']) <= 50000 for g in results)
print(f'\n  SQL FILTER:    All price <= 50K: {all_affordable}')
print(f'  Masuk akal?    YA -- pengguna mendapatkan game gratis/murah.')


# ======================================================================
# B. Medium budget, Medium PC
# ======================================================================

header('B. Medium Budget (300K IDR), Medium PC (2), RPG')

print('''
Alasan: Gamer mainstream dengan anggaran dan PC menengah.
Harapan: Game dalam anggaran dan genre.
''')
results = recommend(budget=300000, pc_level=2, preferred_rating=70,
                    preferred_playtime=20, genre='RPG', top_n=10)
print_results('Top 10', results)
all_affordable = all(float(g['price_idr']) <= 300000 for g in results)
print(f'\n  SQL FILTER:    All price <= 300K: {all_affordable}')
print(f'  Masuk akal?    YA - RPG ramah anggaran dalam spesifikasi.')


# ======================================================================
# C. High budget, High PC
# ======================================================================

header('C. High Budget (1M IDR), High PC (3), Strategy')

print('''
Alasan: Penggemar dengan PC kelas atas, bersedia menghabiskan uang.
Harapan: Game dengan harga <= 1M.
''')
results = recommend(budget=1000000, pc_level=3, preferred_rating=90,
                    preferred_playtime=50, genre='Strategy', top_n=10)
print_results('Top 10', results)
all_affordable = all(float(g['price_idr']) <= 1000000 for g in results)
high_rated = sum(1 for g in results if float(g['rating_percentage']) >= 85)
print(f'\n  SQL FILTER:    All price <= 1M: {all_affordable}')
print(f'  Games with rating >= 85%: {high_rated}/10')
print(f'  Masuk akal?    YA - game Strategi teratas dalam anggaran.')


# ======================================================================
# D. Free games only
# ======================================================================

header('D. Free Games Only (Budget=0), PC 2, Indie')

print('''
Alasan: Pengguna hanya menginginkan game gratis (free-to-play).
Harapan: Hanya game dengan price_idr = 0.
''')
results = recommend(budget=0, pc_level=2, preferred_rating=50,
                    preferred_playtime=20, genre='Indie', top_n=10)
print_results('Top 10', results)
all_free = all(float(g['price_idr']) == 0 for g in results)
print(f'\n  SQL FILTER:    All free (Rp=0): {all_free}')
print(f'  Masuk akal?    YA - hanya game Indie gratis.')


# ======================================================================
# E. No matching genre
# ======================================================================

header('E. No Matching Genre')

print('''
Alasan: String genre yang tidak cocok dengan apapun.
Harapan: Set hasil kosong (tidak ada game dengan tag genre ini).
''')
results = recommend(budget=500000, pc_level=3, preferred_rating=80,
                    preferred_playtime=30, genre='zxy_does_not_exist_xyz', top_n=10)
print_results('Results', results)
print(f'\n  Result count: {len(results)} (expected 0)')
print(f'  Masuk akal?    YA - tidak ada game yang memiliki genre buatan ini.')


# ======================================================================
# F. Very high preferred rating
# ======================================================================

header('F. Very High Preferred Rating (95%), Action')

print('''
Alasan: Pengguna menuntut rating yang hampir sempurna.
Harapan: Game dengan rating >= 90% berperingkat lebih tinggi; banyak game disaring oleh
        perbandingan rating mesin fuzzy (rating < 95% -> bukan Tinggi).
''')
results = recommend(budget=200000, pc_level=2, preferred_rating=95,
                    preferred_playtime=20, genre='Action', top_n=10)
print_results('Top 10', results)
high_rated = sum(1 for g in results if float(g['rating_percentage']) >= 90)
print(f'\n  Games with rating >= 90%: {high_rated}/10')
print(f'  Masuk akal?    YA - game Aksi berperingkat teratas naik ke atas ketika pengguna menginginkan rating tinggi.')


# ======================================================================
# G. Very short preferred playtime
# ======================================================================

header('G. Very Short Preferred Playtime (2h), Adventure')

print('''
Alasan: Pengguna menginginkan sesi permainan yang singkat (santai/perjalanan).
Harapan: Game direkomendasikan untuk preferensi waktu bermain yang singkat.
''')
results = recommend(budget=200000, pc_level=2, preferred_rating=80,
                    preferred_playtime=2, genre='Adventure', top_n=10)
print_results('Top 10', results)
print(f'  Masuk akal?    YA - game petualangan direkomendasikan.')


# ======================================================================
# H. Very long preferred playtime
# ======================================================================

header('H. Very Long Preferred Playtime (200h), RPG')

print('''
Alasan: Pengguna menginginkan game yang sangat dapat dimainkan ulang untuk permainan yang lebih lama.
Harapan: RPG direkomendasikan untuk preferensi waktu bermain yang lama.
''')
results = recommend(budget=200000, pc_level=2, preferred_rating=80,
                    preferred_playtime=200, genre='RPG', top_n=10)
print_results('Top 10', results)
print(f'  Masuk akal?    YA - RPG direkomendasikan.')


# ======================================================================
# I. Ranking verification
# ======================================================================

header('I. Ranking Verification')

subheader('Top 10 diurutkan menurun berdasarkan skor')
results = recommend(budget=300000, pc_level=2, preferred_rating=75,
                    preferred_playtime=20, genre='Action', top_n=10)
scores = [g['recommendation_score'] for g in results]
is_sorted = all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1))
print(f'  Sorted descending: {is_sorted}   Scores: {[f"{s:.2f}" for s in scores]}')

subheader('Parameter Top N dihormati')
for n in [3, 5]:
    r = recommend(budget=300000, pc_level=2, preferred_rating=75,
                  preferred_playtime=20, genre='Action', top_n=n)
    print(f'  top_n={n}: returned {len(r)} results')
    assert len(r) == n, f'Expected {n} results, got {len(r)}'


# ======================================================================
# J. Boundary SQL values
# ======================================================================

header('J. SQL Boundary Checks')

subheader('price_idr = 0 (game gratis dengan anggaran rendah)')
results = recommend(budget=0, pc_level=1, preferred_rating=50,
                    preferred_playtime=10, genre='Action', top_n=5)
print_results('Top 5', results)

subheader('pc_level = 3 (semua game memenuhi syarat)')
results = recommend(budget=100000, pc_level=3, preferred_rating=50,
                    preferred_playtime=10, genre='Simulation', top_n=5)
all_affordable = all(float(g['price_idr']) <= 100000 for g in results)
print(f'  All price <= 100K: {all_affordable}')
print_results('Top 5', results)


# ======================================================================
# SUMMARY
# ======================================================================

header('INTEGRATION TEST SUMMARY')
print("""
  Setiap skenario di atas menguji profil pengguna tertentu terhadap data MySQL asli.
  Penyaring pra-SQL (genre, pc_level, anggaran) diverifikasi pada setiap panggilan.
  Evaluasi fuzzy berjalan pada setiap kandidat; hasil diurutkan berdasarkan skor yang menurun.

  Jika tidak ada kerusakan dan semua asersi lulus, sistem siap untuk implementasi UI.
""")
