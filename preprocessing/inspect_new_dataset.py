import csv, os

path = os.path.join('dataset', 'steamdataset.csv')
size_mb = os.path.getsize(path) / 1024 / 1024

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f'File size: {size_mb:.1f} MB')
    print(f'Header ({len(header)} cols):')
    for i, h in enumerate(header):
        print(f'  [{i}] {h}')
    print()

    # First 5 rows
    for i, row in enumerate(reader):
        if i < 5:
            print(f'Row {i}:')
            for j, val in enumerate(row):
                v = val[:80] if val else '(empty)'
                print(f'  [{j}] {v}')
        if i >= 10:
            break

    # Stats
    f.seek(0)
    next(reader)
    total = 0
    col_counts = {}
    for row in reader:
        total += 1
        l = len(row)
        col_counts[l] = col_counts.get(l, 0) + 1
    
    print(f'\nTotal rows: {total}')
    print(f'Column count distribution: {col_counts}')
