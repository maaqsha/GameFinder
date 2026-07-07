import csv, os

path = os.path.join('dataset', 'steamdataset.csv')

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    # Find playtime-related column indices
    for i, h in enumerate(header):
        if 'playtime' in h.lower() or 'time' in h.lower():
            print(f'Playtime col [{i}]: {h}')

    print()

    total = 0
    pt_cols = [28, 29, 30, 31]  # Average playtime columns
    pt_counts = {c: 0 for c in pt_cols}
    pt_numeric = {c: 0 for c in pt_cols}
    pt_samples = {c: [] for c in pt_cols}
    
    for row in reader:
        total += 1
        for c in pt_cols:
            if len(row) > c:
                val = row[c].strip()
                if val:
                    pt_counts[c] += 1
                    try:
                        float(val)
                        pt_numeric[c] += 1
                        if len(pt_samples[c]) < 3:
                            pt_samples[c].append(val)
                    except ValueError:
                        pass
    
    print(f'Total rows: {total}')
    print()
    for c in pt_cols:
        print(f'Column [{c}] ({header[c]}):')
        print(f'  Non-empty: {pt_counts[c]} ({pt_counts[c]*100//total}%)')
        print(f'  Numeric:   {pt_numeric[c]}')
        if pt_samples[c]:
            print(f'  Samples:   {pt_samples[c]}')
        print()
