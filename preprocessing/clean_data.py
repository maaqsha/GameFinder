import csv
import os
import re
from collections import defaultdict

SRC_DIR = os.path.join('dataset', 'steam_dataset_2025_csv_package_v1', 'steam_dataset_2025_csv')
DST = os.path.join('dataset', 'steamgames_clean.csv')
USD_TO_IDR = 16000

APPS_FILE = os.path.join(SRC_DIR, 'applications.csv')
REVIEWS_FILE = os.path.join(SRC_DIR, 'reviews.csv')
GENRES_FILE = os.path.join(SRC_DIR, 'genres.csv')
APP_GENRES_FILE = os.path.join(SRC_DIR, 'application_genres.csv')

def parse_ram_gb(ram_text):
    if not ram_text or not ram_text.strip():
        return None
    match = re.search(r'(\d+)\s*GB', ram_text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r'(\d+)\s*MB', ram_text, re.IGNORECASE)
    if match:
        mb = int(match.group(1))
        return round(mb / 1024)
    return None

def ram_to_pc_level(ram_gb):
    if ram_gb is None:
        return 2
    if ram_gb <= 4:
        return 1
    if ram_gb <= 8:
        return 2
    return 3

def main():
    print('Phase 1/3: Loading games from applications.csv...')
    game_appids = set()
    games = {}
    with open(APPS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[2] == 'game':
                aid = row[0]
                game_appids.add(aid)
                try:
                    price_cents = float(row[16]) if row[16] and row[16].strip() else 0
                except ValueError:
                    price_cents = 0
                ram_text = row[22]
                ram_gb = parse_ram_gb(ram_text)
                pc_level = ram_to_pc_level(ram_gb)
                games[aid] = {
                    'name': row[1],
                    'price_cents': price_cents,
                    'header_image': row[8] if row[8] else '',
                    'short_description': row[6] if row[6] else '',
                    'ram_gb': ram_gb,
                    'pc_level': pc_level
                }
    print(f'  Games found: {len(game_appids)}')

    print('Phase 2/3: Loading genres...')
    genre_id_to_name = {}
    with open(GENRES_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            genre_id_to_name[row[0]] = row[1]
    app_genres = defaultdict(list)
    with open(APP_GENRES_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            aid = row[0]
            if aid in game_appids:
                gid = row[1]
                gname = genre_id_to_name.get(gid)
                if gname:
                    app_genres[aid].append(gname)
    print(f'  Games with genres: {len(app_genres)}')

    print('Phase 3/3: Aggregating reviews (this may take a while)...')
    review_agg = defaultdict(lambda: {'pos': 0, 'neg': 0, 'playtime_sum': 0, 'playtime_count': 0})
    with open(REVIEWS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for i, row in enumerate(reader):
            if i % 100000 == 0 and i > 0:
                print(f'  Processed {i} reviews...')
            aid = row[1]
            if aid not in game_appids:
                continue
            if row[13] == 'True':
                review_agg[aid]['pos'] += 1
            else:
                review_agg[aid]['neg'] += 1
            try:
                pt = int(row[5])
                if pt > 0:
                    review_agg[aid]['playtime_sum'] += pt
                    review_agg[aid]['playtime_count'] += 1
            except (ValueError, IndexError):
                pass
    print(f'  Games with reviews: {len(review_agg)}')

    print('Writing cleaned dataset...')
    out_header = [
        'app_id', 'name', 'price_idr', 'positive', 'negative',
        'rating_percentage', 'playtime_hours', 'genre',
        'pc_level', 'header_image', 'short_description'
    ]
    written = 0
    stats_missing_ram = 0
    stats_no_reviews = 0
    stats_no_genre = 0

    with open(DST, 'w', encoding='utf-8', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(out_header)
        for aid in game_appids:
            g = games[aid]
            rev = review_agg.get(aid, {'pos': 0, 'neg': 0, 'playtime_sum': 0, 'playtime_count': 0})

            pos = rev['pos']
            neg = rev['neg']
            total = pos + neg
            rating_percentage = round(pos / total * 100, 2) if total > 0 else 0
            avg_playtime_min = (rev['playtime_sum'] / rev['playtime_count']) if rev['playtime_count'] > 0 else 0
            playtime_hours = round(avg_playtime_min / 60, 2)
            price_idr = int(round(g['price_cents'] / 100 * USD_TO_IDR))
            genre_str = ','.join(app_genres.get(aid, ['']))
            pc_level = g['pc_level']

            if g['ram_gb'] is None:
                stats_missing_ram += 1
            if total == 0:
                stats_no_reviews += 1
            if not genre_str:
                stats_no_genre += 1

            writer.writerow([
                aid, g['name'], price_idr, pos, neg,
                rating_percentage, playtime_hours, genre_str,
                pc_level, g['header_image'], g['short_description']
            ])
            written += 1

    print(f'\n=== RESULT ===')
    print(f'Total games imported: {len(game_appids)}')
    print(f'Total cleaned games written: {written}')
    print(f'Output: {DST}')
    print(f'\n=== MISSING VALUE SUMMARY ===')
    print(f'Games missing RAM (pc_level defaulted to 2): {stats_missing_ram} ({100*stats_missing_ram/written:.1f}%)')
    print(f'Games with no reviews (pos/neg/rating/playtime = 0): {stats_no_reviews} ({100*stats_no_reviews/written:.1f}%)')
    print(f'Games with no genre assigned: {stats_no_genre} ({100*stats_no_genre/written:.1f}%)')

if __name__ == '__main__':
    main()
