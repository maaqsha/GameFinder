import csv, os
from collections import Counter

path = os.path.join('dataset', 'steamdataset.csv')

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    # col[28]=avg_forever, col[29]=avg_2weeks, col[30]=median_forever
    # Also check col[8] (About the game) and col[27] (Notes)
    # col[13]=Header image, col[14]=Website, col[22]=Positive, col[23]=Negative
    # col[35]=Genres, col[6]=Price

    platform_stats = Counter()
    total = 0
    pt_nonzero = 0
    pt_over_60 = 0
    pt_over_600 = 0
    pt_max = 0

    for row in reader:
        total += 1
        # Median playtime forever
        pt_str = row[30].strip() if len(row) > 30 else ''
        if pt_str:
            try:
                v = float(pt_str)
                if v > 0:
                    pt_nonzero += 1
                if v >= 60:
                    pt_over_60 += 1
                if v >= 600:
                    pt_over_600 += 1
                if v > pt_max:
                    pt_max = v
            except:
                pass

    print(f'Total rows: {total}')
    print()
    print('Median Playtime Forever (col[30]):')
    print(f'  Non-zero (>0 min): {pt_nonzero}')
    print(f'  >= 1 hour (60 min): {pt_over_60}')
    print(f'  >= 10 hours (600 min): {pt_over_600}')
    print(f'  Max value: {pt_max} min ({pt_max/60:.1f} hours)')
    print(f'  Has data for: {total} rows (100%)')
