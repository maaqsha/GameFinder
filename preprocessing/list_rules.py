from app.services.fuzzy.inference import generate_rules

rules = generate_rules()
print('Full 81-rule knowledge base:')
print('=' * 80)
print(f'{"#":<3} {"Budget":<8} {"PC":<8} {"Rating":<8} {"Playtime":<8} {"Output":<20}')
print('-' * 55)
for i, r in enumerate(rules, 1):
    a = r['antecedent']
    print(f'{i:<3} {a["budget"]:<8} {a["pc_level"]:<8} {a["rating"]:<8} {a["playtime"]:<8} {r["consequent"]:<20}')
print(f'\nTotal: {len(rules)} rules')
