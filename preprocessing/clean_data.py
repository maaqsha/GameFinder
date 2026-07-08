import csv
import os

SRC = os.path.join('dataset', 'steam_games_2024-2026.csv')
DST = os.path.join('dataset', 'steamgames_clean_v3.csv')
USD_TO_IDR = 16000

def main():
    print(f'Reading {SRC}...')
    with open(SRC, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        raw = list(reader)
    print(f'  Loaded {len(raw)} rows')

    out_header = [
        'app_id', 'name', 'price_idr', 'positive', 'negative',
        'rating_percentage', 'playtime_hours', 'genre',
        'pc_level', 'header_image', 'short_description',
        'total_reviews',
    ]

    rows = []
    stats_no_rating = 0
    stats_no_reviews = 0
    stats_no_genre = 0

    for r in raw:
        aid = r['AppID'].strip()
        name = r['Name'].strip()

        try:
            price_usd = float(r['Price_USD'])
        except (ValueError, TypeError):
            price_usd = 0.0
        price_idr = int(round(price_usd * USD_TO_IDR))

        try:
            rating_pct = float(r['Review_Score_Pct'])
        except (ValueError, TypeError):
            rating_pct = 0.0

        try:
            total_reviews = int(r['Total_Reviews'])
        except (ValueError, TypeError):
            total_reviews = 0

        if total_reviews > 0 and rating_pct > 0:
            positive = round(total_reviews * rating_pct / 100)
            negative = total_reviews - positive
        else:
            positive = 0
            negative = 0

        genre = r.get('Primary_Genre', '').strip()
        if not genre:
            stats_no_genre += 1
        if rating_pct == 0:
            stats_no_rating += 1
        if total_reviews == 0:
            stats_no_reviews += 1

        rows.append([aid, name, price_idr, positive, negative, rating_pct,
                     0.0, genre, 2, '', '', total_reviews])

    print(f'Writing {DST}...')
    with open(DST, 'w', encoding='utf-8', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(out_header)
        for row in rows:
            writer.writerow(row)

    print(f'\n=== RESULT ===')
    print(f'Total games written: {len(rows)}')
    print(f'Output: {DST}')
    print(f'\n=== SUMMARY ===')
    print(f'Games with no rating (0%): {stats_no_rating} ({100*stats_no_rating/len(rows):.1f}%)')
    print(f'Games with no reviews (total=0): {stats_no_reviews} ({100*stats_no_reviews/len(rows):.1f}%)')
    print(f'Games with no genre: {stats_no_genre} ({100*stats_no_genre/len(rows):.1f}%)')
    print(f'Free games: {sum(1 for r in rows if r[2] == 0)}')

if __name__ == '__main__':
    main()
