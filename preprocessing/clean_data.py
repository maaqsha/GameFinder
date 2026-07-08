import csv
import os

SRC = os.path.join('dataset', 'steam_games_2024-2026.csv')
DST = os.path.join('dataset', 'steamgames_clean.csv')
USD_TO_IDR = 16000

OUT_HEADER = [
    'app_id', 'name', 'price_idr', 'rating_percentage',
    'total_reviews', 'genre', 'tags',
    'estimated_owners', 'peak_players',
]


def main():
    print(f'Reading {SRC}...')
    with open(SRC, 'r', encoding='utf-8-sig') as f:
        raw = list(csv.DictReader(f))
    print(f'  Loaded {len(raw)} rows')

    rows = []
    stats_no_rating = 0
    stats_no_reviews = 0
    stats_no_genre = 0

    for r in raw:
        aid = r['AppID'].strip()
        name = r['Name'].strip()
        genre = r.get('Primary_Genre', '').strip()
        tags_raw = r.get('All_Tags', '').strip()
        tags = ','.join(t.strip() for t in tags_raw.split(';') if t.strip()) if tags_raw else ''

        try:
            price_idr = int(round(float(r['Price_USD']) * USD_TO_IDR))
        except (ValueError, TypeError):
            price_idr = 0

        try:
            rating_pct = float(r['Review_Score_Pct'])
        except (ValueError, TypeError):
            rating_pct = 0.0

        try:
            total_reviews = int(r['Total_Reviews'])
        except (ValueError, TypeError):
            total_reviews = 0

        try:
            estimated_owners = int(r['Estimated_Owners'])
        except (ValueError, TypeError):
            estimated_owners = 0

        try:
            peak_players = int(r['24h_Peak_Players'])
        except (ValueError, TypeError):
            peak_players = 0

        if not genre:
            stats_no_genre += 1
        if rating_pct <= 0:
            stats_no_rating += 1
        if total_reviews <= 0:
            stats_no_reviews += 1

        rows.append([aid, name, price_idr, rating_pct, total_reviews,
                     genre, tags, estimated_owners, peak_players])

    print(f'Writing {DST}...')
    with open(DST, 'w', encoding='utf-8', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(OUT_HEADER)
        for row in rows:
            writer.writerow(row)

    print(f'\n=== RESULT ===')
    print(f'Total games: {len(rows)}')
    print(f'Output: {DST}')
    print(f'Genres: {len(set(r[5] for r in rows if r[5]))}')
    print(f'No genre: {stats_no_genre}')
    print(f'No rating: {stats_no_rating}')
    print(f'No reviews: {stats_no_reviews}')
    print(f'Free games: {sum(1 for r in rows if r[2] == 0)}')


if __name__ == '__main__':
    main()
