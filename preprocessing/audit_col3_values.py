import csv
from collections import Counter

def safe(s):
    if isinstance(s, str):
        return s.encode('ascii', 'replace').decode('ascii')[:60]
    return str(s)

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Header:', header)

    col3_dist = Counter()
    col8_len_dist = Counter()
    total = 0
    col8_about_text = 0
    col8_with_comma = 0
    col6_vals = Counter()
    col7_vals = Counter()

    for i, row in enumerate(reader):
        total += 1
        if len(row) != 10:
            continue

        c3 = row[3].strip()
        try:
            col3_dist[float(c3)] += 1
        except:
            col3_dist['non-numeric: ' + c3[:20]] += 1

        c8 = row[8].strip()
        if c8:
            col8_len_dist[len(c8)] += 1
            if ',' in c8:
                col8_with_comma += 1
            # Check if it looks like a content warning
            lower = c8.lower()
            if any(w in lower for w in ['content', 'mature', 'nudity', 'violence', 'gore', 'sexual']):
                col8_about_text += 1

        # Check col 6 & 7 (positive/negative) - are they always numeric?
        try:
            col6_vals[int(row[6].strip())] += 1
        except:
            col6_vals['non-numeric'] += 1
        try:
            col7_vals[int(row[7].strip())] += 1
        except:
            col7_vals['non-numeric'] += 1

    print(f'\nTotal rows: {total}')
    print(f'\nColumn 3 (About the game) value distribution:')
    for k, v in sorted(col3_dist.items(), key=lambda x: -x[1])[:10]:
        print(f'  {k}: {v}')
    print(f'  ... ({len(col3_dist)} unique values total)')

    print(f'\nColumn 6 (Positive) - all numeric: {sum(v for k,v in col6_vals.items() if k != "non-numeric")}')
    print(f'Column 7 (Negative) - all numeric: {sum(v for k,v in col7_vals.items() if k != "non-numeric")}')
    if 'non-numeric' in col6_vals:
        print(f'Column 6 non-numeric: {col6_vals["non-numeric"]}')
    if 'non-numeric' in col7_vals:
        print(f'Column 7 non-numeric: {col7_vals["non-numeric"]}')

    print(f'\nColumn 8 (Playtime) analysis:')
    print(f'  Non-empty: {sum(col8_len_dist.values())}')
    print(f'  Contains commas: {col8_with_comma}')
    print(f'  Looks like content warnings: {col8_about_text}')
    if col8_len_dist:
        min_len = min(col8_len_dist.keys())
        max_len = max(col8_len_dist.keys())
        print(f'  Length min: {min_len}, max: {max_len}')
