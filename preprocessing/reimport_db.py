"""Drop and recreate games table with total_reviews column, then import."""
import mysql.connector
import os

CSV_PATH = os.path.join('dataset', 'steamgames_clean_v3.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    database='gamefinder',
    allow_local_infile=True
)
cursor = conn.cursor()

# Drop old table
print('Dropping old games table...')
cursor.execute("DROP TABLE IF EXISTS games")

# Create new schema with total_reviews
print('Creating new games table...')
cursor.execute("""
CREATE TABLE games (
    app_id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price_idr BIGINT NOT NULL DEFAULT 0,
    positive INT NOT NULL DEFAULT 0,
    negative INT NOT NULL DEFAULT 0,
    rating_percentage DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    playtime_hours DECIMAL(8,2) NOT NULL DEFAULT 0.00,
    genre TEXT,
    pc_level TINYINT NOT NULL DEFAULT 2,
    header_image TEXT,
    short_description TEXT,
    total_reviews INT NOT NULL DEFAULT 0,
    PRIMARY KEY (app_id),
    KEY idx_pc_level (pc_level),
    KEY idx_rating_playtime (rating_percentage, playtime_hours),
    KEY idx_total_reviews (total_reviews),
    FULLTEXT KEY idx_genre_fulltext (genre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
""")
conn.commit()
print('Table created.')

# Import data
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
(app_id, name, price_idr, positive, negative, rating_percentage, playtime_hours, genre, pc_level, header_image, short_description, total_reviews)
"""

cursor.execute(sql)
conn.commit()
print(f'Rows imported: {cursor.rowcount:,}')

# Verify
print('\n=== Verification ===')
cursor.execute("SELECT COUNT(*) FROM games")
print(f'Total rows: {cursor.fetchone()[0]:,}')

# Check target games
target_ids = [570, 550, 620, 440, 10, 730, 105600, 413150, 367520, 2322010, 1245620]
for tid in target_ids:
    cursor.execute("""
        SELECT app_id, name, price_idr, positive, negative, 
               positive+negative, rating_percentage, total_reviews
        FROM games WHERE app_id = %s
    """, (tid,))
    r = cursor.fetchone()
    if r:
        print(f'  ID={r[0]:>7} {str(r[1])[:45]:<45} price=Rp{r[2]:>10,} pos={r[3]:>4} neg={r[4]:>4} sampled={r[5]:>5} total_reviews={r[6]:>7,} rating={float(r[7]):.1f}%')
    else:
        print(f'  ID={tid:>7} NOT FOUND')

cursor.close()
conn.close()
print('\nDone.')
