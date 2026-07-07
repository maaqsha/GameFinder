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

csv_abs = os.path.abspath(CSV_PATH).replace('\\', '/')

sql = f"""
LOAD DATA LOCAL INFILE '{csv_abs}'
INTO TABLE games
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\\\'
LINES TERMINATED BY '\\r\\n'
IGNORE 1 LINES
(app_id, name, price_idr, positive, negative, rating_percentage, playtime_hours, genre, pc_level, header_image, short_description)
"""

cursor.execute(sql)
conn.commit()
print(f'Rows imported: {cursor.rowcount}')

cursor.close()
conn.close()
