"""Drop and recreate games table with new schema, then import clean CSV."""
import mysql.connector
import os

CSV_PATH = os.path.join('dataset', 'steamgames_clean.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    database='gamefinder',
    allow_local_infile=True
)
cursor = conn.cursor()

print('Dropping old games table...')
cursor.execute("DROP TABLE IF EXISTS games")

print('Creating new games table...')
cursor.execute("""
CREATE TABLE games (
    app_id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    release_date DATE NULL,
    price_idr BIGINT NOT NULL DEFAULT 0,
    rating_percentage DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    total_reviews INT NOT NULL DEFAULT 0,
    genre VARCHAR(100) NOT NULL DEFAULT '',
    tags TEXT,
    estimated_owners BIGINT NOT NULL DEFAULT 0,
    peak_players INT NOT NULL DEFAULT 0,
    PRIMARY KEY (app_id),
    KEY idx_total_reviews (total_reviews),
    KEY idx_estimated_owners (estimated_owners),
    KEY idx_peak_players (peak_players),
    FULLTEXT KEY idx_genre_tags_fulltext (genre, tags)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
""")
conn.commit()
print('Table created.')

csv_abs = os.path.abspath(CSV_PATH).replace('\\', '/')
print(f'Importing from {csv_abs}...')
sql = f"""
LOAD DATA LOCAL INFILE '{csv_abs}'
INTO TABLE games
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\\\'
LINES TERMINATED BY '\\r\\n'
IGNORE 1 LINES
(app_id, name, @release_date, price_idr, rating_percentage, total_reviews, genre, tags, estimated_owners, peak_players)
SET release_date = NULLIF(@release_date, '')
"""
cursor.execute(sql)
conn.commit()
print(f'Rows imported: {cursor.rowcount:,}')

print('\n=== Verification ===')
cursor.execute("SELECT COUNT(*) FROM games")
print(f'Total rows: {cursor.fetchone()[0]:,}')

target_ids = [730, 105600, 413150, 1245620, 3764200]
for tid in target_ids:
    cursor.execute("""
        SELECT app_id, name, price_idr, rating_percentage,
               total_reviews, genre, estimated_owners, peak_players
        FROM games WHERE app_id = %s
    """, (tid,))
    r = cursor.fetchone()
    if r:
        print(f'  ID={r[0]:>7} {str(r[1])[:45]:<45} price=Rp{r[2]:>10,} rating={r[3]:>5.1f}% reviews={r[4]:>7,} genre={r[5]:<20} owners={r[6]:>10,} peak={r[7]:>7,}')
    else:
        print(f'  ID={tid:>7} NOT FOUND')

cursor.close()
conn.close()
print('\nDone.')
