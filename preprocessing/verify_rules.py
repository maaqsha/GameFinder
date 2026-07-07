from app.services.fuzzy.inference import generate_rules

rules = generate_rules()
print(f'Total rules generated: {len(rules)}')
print()

cats = {}
for r in rules:
    c = r['consequent']
    cats[c] = cats.get(c, 0) + 1
print('Output distribution:')
for c, n in sorted(cats.items()):
    print(f'  {c}: {n}')
print()

print('Sample first 5 rules:')
for r in rules[:5]:
    a = r['antecedent']
    print(f'  IF budget={a["budget"]} AND pc={a["pc_level"]} AND rating={a["rating"]} AND playtime={a["playtime"]} THEN {r["consequent"]}')
print('  ...')
print('Sample last 5 rules:')
for r in rules[-5:]:
    a = r['antecedent']
    print(f'  IF budget={a["budget"]} AND pc={a["pc_level"]} AND rating={a["rating"]} AND playtime={a["playtime"]} THEN {r["consequent"]}')
print()

assert len(rules) == 81, f'Expected 81, got {len(rules)}'
signatures = set()
for r in rules:
    a = r['antecedent']
    sig = (a['budget'], a['pc_level'], a['rating'], a['playtime'])
    signatures.add(sig)
assert len(signatures) == 81, f'Expected 81 unique combos, got {len(signatures)}'
print('All 81 combinations unique — verified.')
print('No duplicates — verified.')
print('No missing combinations — verified.')
