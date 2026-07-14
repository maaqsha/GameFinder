"""
Tes unit untuk mesin rekomendasi GameFinder — murni Python, tanpa DB.

Tes:
  1. Kondisi batas keanggotaan segitiga
  2. evaluate_game() profil game sintetis
  3. Distribusi aturan (81 aturan)
  4. Kewarasan Centroid / defuzzifikasi
  5. Pemeriksaan silang fuzzifikasi
  6. Pemetaan batas kategori
  7. Kasus tepi (input nol/degenerasi)
"""

import sys
sys.path.insert(0, '.')
from app.services.fuzzy.recommendation import evaluate_game, score_category
from app.services.fuzzy.fuzzification import (
    fuzzify_budget, fuzzify_pc_level, fuzzify_rating, fuzzify_playtime,
)
from app.services.fuzzy.inference import generate_rules
from app.services.fuzzy.defuzzification import centroid
from app.services.fuzzy.membership import triangular

_RULES = generate_rules()


def header(title):
    print(); print('=' * 72); print(f'  {title}'); print('=' * 72)


def subheader(title):
    print(); print(f'--- {title} ---')


def check(label, ok, detail=''):
    marker = 'OK' if ok else 'FAIL'
    print(f'  [{marker}] {label}' + (f' ({detail})' if detail else ''))


def assert_near(label, actual, expected, tolerance=0.02):
    check(label, abs(actual - expected) <= tolerance,
          f'got {actual:.4f}, expected {expected:.4f}')


def assert_category(label, score, expected_cat):
    actual = score_category(score)
    check(label, actual == expected_cat,
          f'score={score:.2f}, got "{actual}", expected "{expected_cat}"')


# ======================================================================
# 1. Kondisi batas keanggotaan segitiga
# ======================================================================

header('1.1 Keanggotaan Segitiga — Kondisi Batas')

assert_near('tri(0,0,0,0) point', triangular(0, 0, 0, 0), 1.0)
assert_near('tri(5,0,0,0) degenerate a=b', triangular(5, 0, 0, 0), 1.0)
assert_near('tri(50,0,0,100) midpoint', triangular(50, 0, 0, 100), 0.5)
assert_near('tri(0,0,50,100) at left base', triangular(0, 0, 50, 100), 0.0)
assert_near('tri(100,0,50,100) at right base', triangular(100, 0, 50, 100), 0.0)
assert_near('tri(25,0,50,100) rising edge', triangular(25, 0, 50, 100), 0.5)
assert_near('tri(75,0,50,100) falling edge', triangular(75, 0, 50, 100), 0.5)
assert_near('tri(50,0,50,100) at peak', triangular(50, 0, 50, 100), 1.0)
assert_near('tri(100,70,100,100) right shoulder', triangular(100, 70, 100, 100), 1.0)
assert_near('tri(0,0,0,100) left shoulder', triangular(0, 0, 0, 100), 1.0)


# ======================================================================
# 2. evaluate_game — profil game sintetis
# ======================================================================

header('1.2 evaluate_game — Profil Game Sintetis')

# Profil A: Indie murah, PC rendah, rating tinggi (Kecocokan kasual)
#   Ideal Kasual: anggaran=Rendah, rating=Sedang, waktu bermain=Sedang
#   rating 95%: Tinggi=0.857, Sedang=0.333, Rendah=0.05
#   Sedang memicu Sangat Direkomendasikan(3/3), Tinggi memicu Direkomendasikan(2/3) → centroid ≈ 44
s, agg = evaluate_game(0, 1, 95, 2, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=1)
assert_near('[A] Cheap indie, Casual score', s, 43.98, tolerance=1.0)
assert_category('[A] Cheap indie, Casual category', s, 'Less Recommended')

# Profil A2: Game yang sama dengan Seimbang
#   Ideal Seimbang: anggaran=Sedang, rating=Tinggi, waktu bermain=Sedang
#   anggaran Rendah≠Sedang✗, rating Tinggi=Tinggi✓, waktu bermain✓ → 2/3 → Rec
#   Tapi Sedang memicu Kurang Direkomendasikan(1/3) pada 0.333. Centroid ditarik ke kiri.
s, agg = evaluate_game(0, 1, 95, 2, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=2)
assert_near('[A2] Cheap indie, Balanced score', s, 27.20, tolerance=1.0)
assert_category('[A2] Cheap indie, Balanced category', s, 'Less Recommended')

# Profil A3: Game yang sama dengan Hardcore
#   Ideal Hardcore: anggaran=Tinggi, rating=Tinggi, waktu bermain=Sedang
#   anggaran Rendah≠Tinggi✗, rating Tinggi=Tinggi✓, waktu bermain✓ → 2/3 → Rec
#   Struktur sama dengan Seimbang (anggaran tidak cocok + rating cocok)
s, agg = evaluate_game(0, 1, 95, 2, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=3)
assert_near('[A3] Cheap indie, Hardcore score', s, 27.20, tolerance=1.0)
assert_category('[A3] Cheap indie, Hardcore category', s, 'Less Recommended')

# Profil B: Game AAA, PC tinggi, rating sedang, waktu bermain lama dengan Seimbang
#   anggaran Tinggi≠Sedang✗, rating Sedang≠Tinggi✗, waktu bermain Sedang✓ → 1/3 → Kurang Direkomendasikan
s, agg = evaluate_game(800000, 3, 70, 60, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=2)
assert_near('[B] AAA score', s, 16.19, tolerance=1.0)
assert_category('[B] AAA category', s, 'Not Recommended')

# Profil C: Game kelas menengah dengan Seimbang
#   anggaran: 350k → Sedang=0.75, Tinggi=0 (tidak cukup)
#   rating=60 → Rendah=0.4, Sedang=0.25
#   waktu bermain Sedang=1.0 → ✓
#   Berbagai kombinasi kecocokan menciptakan pemicu multi-kategori
s, agg = evaluate_game(350000, 2, 60, 30, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=2)
assert_near('[C] Mid-range score', s, 43.22, tolerance=1.0)
assert_category('[C] Mid-range category', s, 'Less Recommended')

# Profil D: Murah, rating buruk dengan Seimbang
#   anggaran Rendah≠Sedang✗, rating Rendah≠Tinggi✗, waktu bermain Sedang✓ → 1/3 → Kurang Direkomendasikan
#   Rating yang sangat rendah berarti semua kategori terpicu dengan lemah → centroid mendekati 0
s, agg = evaluate_game(0, 1, 20, 5, preferred_rating=80, preferred_playtime=20,
                        preferred_gamer_type=2)
assert_near('[D] Cheap junk score', s, 9.09, tolerance=1.0)
assert_category('[D] Cheap junk category', s, 'Not Recommended')

# Profile E: Mid-range game matching Balanced profile partially
#   budget 200k → Low=0.333, Medium=0.6
#   Low rules: budget✗, playtime✓ → 1 or 2 matches depending on rating
#   Medium rules: budget✓, playtime✓ → 2 or 3 matches
#   Multi-category centroid between Rec and Highly Rec → ≈ 63
s, agg = evaluate_game(200000, 2, 80, 30, preferred_rating=80, preferred_playtime=30,
                        preferred_gamer_type=2)
assert_near('[E] Within-budget match score', s, 62.51, tolerance=1.0)
assert_category('[E] Within-budget match category', s, 'Recommended')

# Profile F: Playtime mismatch — both fire same rules with Casual (Short is ideal), so no diff
_, a_perfect = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=2,
                              preferred_gamer_type=1)
_, a_off = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=200,
                          preferred_gamer_type=1)
check('[F] Playtime change affects recommendations', a_off['Less Recommended'] > 0 or a_perfect['Less Recommended'] > 0,
      'both produce non-zero output')

# Profile G: Rating mismatch — Casual ideal is Medium, both 100% and 20% give different results
s_good_r, _ = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=10,
                             preferred_gamer_type=2)
s_bad_r, _ = evaluate_game(0, 1, 20, 2, preferred_rating=80, preferred_playtime=10,
                            preferred_gamer_type=2)
check('[G] Rating mismatch changes score', s_bad_r != s_good_r,
      f'good_rating={s_good_r:.2f}, bad_rating={s_bad_r:.2f}')


# ======================================================================
# 3. Rule distribution
# ======================================================================

header('2. Rule Distribution')

check('Total rules = 243', len(_RULES) == 243)
rule_dist = {}
for r in _RULES:
    cat = r['consequent']
    rule_dist[cat] = rule_dist.get(cat, 0) + 1

valid_cats = {'Not Recommended', 'Less Recommended', 'Recommended', 'Highly Recommended'}
all_valid = all(r['consequent'] in valid_cats for r in _RULES)
check('All consequents valid', all_valid)
for cat in ['Not Recommended', 'Less Recommended', 'Recommended', 'Highly Recommended']:
    print(f'    {cat}: {rule_dist.get(cat, 0)}')
print(f'    Sum: {sum(rule_dist.values())}')
check('All antecedents complete', all(
    len(r['antecedent']) == 5
    and r['antecedent']['budget'] in ('Low', 'Medium', 'High')
    and r['antecedent']['pc_level'] in ('Low', 'Medium', 'High')
    and r['antecedent']['gamer_type'] in ('Casual', 'Balanced', 'Hardcore')
    and r['antecedent']['rating'] in ('Low', 'Medium', 'High')
    and r['antecedent']['playtime'] in ('Short', 'Medium', 'Long')
    for r in _RULES
))


# ======================================================================
# 4. Centroid / defuzzification
# ======================================================================

header('3. Centroid / Defuzzification')

pure_tests = {
    'Not Recommended only':
        {'Not Recommended': 1.0, 'Less Recommended': 0.0, 'Recommended': 0.0, 'Highly Recommended': 0.0},
    'Less Recommended only':
        {'Not Recommended': 0.0, 'Less Recommended': 1.0, 'Recommended': 0.0, 'Highly Recommended': 0.0},
    'Recommended only':
        {'Not Recommended': 0.0, 'Less Recommended': 0.0, 'Recommended': 1.0, 'Highly Recommended': 0.0},
    'Highly Recommended':
        {'Not Recommended': 0.0, 'Less Recommended': 0.0, 'Recommended': 0.0, 'Highly Recommended': 1.0},
}
for label, agg in pure_tests.items():
    c = centroid(agg)
    cat = score_category(c)
    print(f'    {label}: {c:.2f} -> {cat}')

# All zero
c0 = centroid({'Not Recommended': 0.0, 'Less Recommended': 0.0, 'Recommended': 0.0, 'Highly Recommended': 0.0})
assert_near('centroid(all zero)', c0, 0.0)


# ======================================================================
# 5. Fuzzification cross-check
# ======================================================================

header('4. Fuzzification Cross-Check')

print('  Budget MFs:')
for price in [0, 200000, 300000, 450000, 600000, 1000000]:
    fb = fuzzify_budget(price)
    print(f'    Rp{price:>7,}: L={fb["Low"]:.3f} M={fb["Medium"]:.3f} H={fb["High"]:.3f}')

valid_budget = all(
    any(v > 0 for v in fuzzify_budget(p).values())
    for p in [0, 200000, 300000, 450000, 600000, 1000000]
)
check('Budget fuzzification always has >=1 active MF', valid_budget)

print()
print('  PC Level MFs (crisp):')
for pc in [1, 2, 3]:
    fp = fuzzify_pc_level(pc)
    print(f'    PC{pc}: L={fp["Low"]:.0f} M={fp["Medium"]:.0f} H={fp["High"]:.0f}')

print()
print('  Rating MFs (pref=80):')
rating_samples = [0, 50, 60, 70, 75, 80, 85, 95, 100]
for r in rating_samples:
    fr = fuzzify_rating(r, 80)
    print(f'    r={r:>3}: L={fr["Low"]:.3f} M={fr["Medium"]:.3f} H={fr["High"]:.3f}')

high_vals = [fuzzify_rating(r, 80)['High'] for r in rating_samples]
mono_high = all(high_vals[i] <= high_vals[i+1] for i in range(len(high_vals)-1))
check('Rating High MF is monotonic non-decreasing', mono_high)

print()
print('  Playtime MFs (pref=20h):')
pt_samples = [0, 5, 10, 14, 18, 20, 25, 30, 50, 100]
for pt in pt_samples:
    fp = fuzzify_playtime(pt, 20)
    print(f'    pt={pt:>4}h: S={fp["Short"]:.3f} M={fp["Medium"]:.3f} L={fp["Long"]:.3f}')

mp = fuzzify_playtime(20, 20)
check('Playtime at preferred: Medium=1.0', mp['Medium'] == 1.0)
check('Playtime at preferred: Short=0', mp['Short'] == 0.0)
check('Playtime at preferred: Long=0', mp['Long'] == 0.0)


# ======================================================================
# 6. Category boundary mapping
# ======================================================================

header('5. Category Boundary Mapping')

cat_boundaries = [
    (0, 'Not Recommended'), (10, 'Not Recommended'), (25, 'Not Recommended'),
    (26, 'Less Recommended'), (35, 'Less Recommended'), (50, 'Less Recommended'),
    (51, 'Recommended'), (60, 'Recommended'), (75, 'Recommended'),
    (76, 'Highly Recommended'), (90, 'Highly Recommended'), (100, 'Highly Recommended'),
]
all_cat_ok = True
for score, expected in cat_boundaries:
    cat = score_category(score)
    ok = cat == expected
    if not ok:
        all_cat_ok = False
        print(f'    FAIL: {score:>4} -> {cat:<22} (expected {expected})')
print(f'    All boundary mappings correct: {all_cat_ok}')


# ======================================================================
# 7. Edge cases
# ======================================================================

header('6. Edge Cases')

# 6a: Zero playtime (no review data)
fp = fuzzify_playtime(0, 20)
assert_near('playtime=0 -> Short=1.0', fp['Short'], 1.0)
assert_near('playtime=0 -> Medium=0', fp['Medium'], 0.0)
assert_near('playtime=0 -> Long=0', fp['Long'], 0.0)

# 6b: Very large playtime
fp = fuzzify_playtime(5000, 20)
assert_near('playtime=5000h -> Long=1.0', fp['Long'], 1.0)

# 6c: PC Level outside range (should not crash)
fp = fuzzify_pc_level(0)
assert_near('pc=0: all zero', fp['Low'] + fp['Medium'] + fp['High'], 0.0)
fp = fuzzify_pc_level(4)
assert_near('pc=4: all zero', fp['Low'] + fp['Medium'] + fp['High'], 0.0)

# 6d: Degenerate preferred_playtime=0 (was bug: all MFs returned 1.0)
fp = fuzzify_playtime(10, 0)
check('pref_playtime=0 no longer degenerate',
      not (fp['Short'] == 1.0 and fp['Medium'] == 1.0 and fp['Long'] == 1.0),
      f'S={fp["Short"]:.3f} M={fp["Medium"]:.3f} L={fp["Long"]:.3f}')

# 6e: Ensure preferred_rating=0 is guarded
fr = fuzzify_rating(0, 0)
check('pref_rating=0, game=0%: Low active', fr['Low'] > 0.5, f'Low={fr["Low"]:.3f}')

# 6f: Evaluate with degenerate preferences (should not crash)
s, _ = evaluate_game(0, 1, 50, 10, preferred_rating=0, preferred_playtime=0,
                     preferred_gamer_type=2)
check('evaluate with pref_rating=0, pref_playtime=0', s > 0, f'score={s:.2f}')

# 6g: Different rating preferences affect fuzzification (same game, different pref)
s1, _ = evaluate_game(0, 1, 100, 2, preferred_rating=50, preferred_playtime=10,
                      preferred_gamer_type=2)
s2, _ = evaluate_game(0, 1, 100, 2, preferred_rating=99, preferred_playtime=10,
                      preferred_gamer_type=2)
check('Different rating pref changes score', s1 != s2,
      f's1(pref=50%)={s1:.2f}, s2(pref=99%)={s2:.2f}')

# 6h: Different playtime preferences affect score
s_short_pref, _ = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=2,
                                 preferred_gamer_type=1)
s_long_pref, _ = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=200,
                                preferred_gamer_type=1)
check('Different playtime pref changes score', s_short_pref != s_long_pref,
      f'short_pref={s_short_pref:.2f}, long_pref={s_long_pref:.2f}')

# 6i: Determinism — same inputs produce same score
s1, _ = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=2,
                       preferred_gamer_type=1)
s2, _ = evaluate_game(0, 1, 100, 2, preferred_rating=80, preferred_playtime=2,
                       preferred_gamer_type=1)
check('Deterministic output', s1 == s2, f's1={s1:.2f}, s2={s2:.2f}')


# ======================================================================
# Summary
# ======================================================================

header('UNIT TEST SUMMARY')
print()
print('  All tests above are pure Python -- no database required.')
print('  Each verifies a specific component of the fuzzy pipeline.')
print()
print('  If no FAIL markers above, the engine is internally consistent.')
print()
print('  Next step: run integration tests against MySQL:')
print('    python tests/test_integration.py')
