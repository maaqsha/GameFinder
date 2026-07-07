import csv
from collections import Counter

def safe(s):
    if isinstance(s, str):
        return s.encode('ascii', 'replace').decode('ascii')[:80]
    return str(s)

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Header:', header)
    print()

    total = 0
    col4_empty = 0
    col4_url = 0
    col4_other = 0
    col5_empty = 0
    col5_url = 0
    col5_other = 0
    col4_samples = []
    col5_samples = []

    for i, row in enumerate(reader):
        total += 1
        if len(row) != 10:
            continue

        c4 = row[4].strip()
        c5 = row[5].strip()

        if not c4:
            col4_empty += 1
        elif c4.startswith('http'):
            col4_url += 1
        else:
            col4_other += 1

        if not c5:
            col5_empty += 1
        elif c5.startswith('http'):
            col5_url += 1
        else:
            col5_other += 1

        if total <= 5:
            print(f'Row {i}: col4={c4[:60]!r}, col5={c5[:60]!r}')

print()
print(f'Total rows: {total}')
print(f'Column 4 (Header image):')
print(f'  Empty: {col4_empty}')
print(f'  URL:   {col4_url}')
print(f'  Other: {col4_other}')
print(f'Column 5 (Website):')
print(f'  Empty: {col5_empty}')
print(f'  URL:   {col5_url}')
print(f'  Other: {col5_other}')
