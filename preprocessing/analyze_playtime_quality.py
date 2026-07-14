import csv, os
from collections import Counter

path = os.path.join('dataset', 'steamdataset.csv')

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    # col[28]=avg_selamanya, col[29]=avg_2minggu, col[30]=median_selamanya
    # Periksa juga col[8] (Tentang game) dan col[27] (Catatan)
    # col[13]=Gambar header, col[14]=Situs web, col[22]=Positif, col[23]=Negatif
    # col[35]=Genre, col[6]=Harga

    platform_stats = Counter()
    total = 0
    pt_nonzero = 0
    pt_over_60 = 0
    pt_over_600 = 0
    pt_max = 0

    for row in reader:
        total += 1
        # Median waktu bermain selamanya
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
