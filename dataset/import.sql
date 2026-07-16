LOAD DATA LOCAL INFILE 'dataset/steamgames_clean.csv'
INTO TABLE games
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(app_id, name, price_idr, rating_percentage, total_reviews, genre, tags, estimated_owners, peak_players);
