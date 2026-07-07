import csv, sys
from collections import Counter

def safe(s):
    if isinstance(s, str):
        return s.encode('ascii', 'replace').decode('ascii')[:60]
    return str(s)

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Header:', header)
    print()

    col3_vals = Counter()
    col8_vals = Counter()
    total = 0
    multiline = 0

    for i, row in enumerate(reader):
        total += 1
        if len(row) != 10:
            continue

        c3 = row[3].strip() if row[3] else ''
        c8 = row[8].strip() if row[8] else ''

        # Check if col3 is numeric
        if c3:
            if c3.replace('.','',1).lstrip('-').isdigit():
                col3_vals['numeric'] += 1
            else:
                col3_vals['text'] += 1
        else:
            col3_vals['empty'] += 1

        col8_vals[bool(c8)] += 1

        if c3 and not c3.replace('.','',1).lstrip('-').isdigit():
            if total <= 5:
                print(f'Row {i}: col3 has TEXT = {safe(c3)}')

    print(f'Total rows (10 cols): {total}')
    print()
    print('Column 3 (About the game) analysis:')
    for k, v in sorted(col3_vals.items()):
        print(f'  {k}: {v}')
    print()
    print('Column 8 (Playtime) analysis:')
    for k, v in sorted(col8_vals.items()):
        print(f'  {"non-empty" if k else "empty"}: {v}')
    print()

    # Get a few rows with actual ABOUT text (not 0/1)
    # Find rows where col3 has text > 20 chars
    print('=== ROWS WITH SUBSTANTIAL ABOUT TEXT (>20 chars in col3) ===')
    with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f2:
        reader2 = csv.reader(f2)
        next(reader2)
        found = 0
        for i, row in enumerate(reader2):
            if len(row) != 10:
                continue
            c3 = row[3].strip() if row[3] else ''
            if len(c3) > 20:
                c8 = row[8].strip()[:40] if row[8] else ''
                print(f'  Row {i}: col3={safe(c3[:80])}')
                print(f'         col8={safe(c8)}')
                print(f'         AppID={row[0]}, Name={safe(row[1][:30])}')
                found += 1
                if found >= 3:
                    break
        if found == 0:
            print('  None found')
