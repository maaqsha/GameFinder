import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

CSV_PATH = os.path.join('dataset', 'steamgames_clean.csv')

conn = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST', 'localhost'),
    user=os.getenv('MYSQL_USER', 'root'),
    password=os.getenv('MYSQL_PASSWORD', ''),
    database=os.getenv('MYSQL_DATABASE', 'gamefinder'),
    allow_local_infile=True,
)
cursor = conn.cursor()

csv_abs = os.path.abspath(CSV_PATH).replace('\\', '/')

sql = f"""
LOAD DATA LOCAL INFILE '{csv_abs}'
INTO TABLE games
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\\\'
LINES TERMINATED BY '\\r\\n'
IGNORE 1 LINES
(app_id, name, price_idr, rating_percentage, total_reviews, genre, tags, estimated_owners, peak_players)
"""

cursor.execute(sql)
conn.commit()
print(f'Rows imported: {cursor.rowcount}')

cursor.close()
conn.close()
