LOAD DATA LOCAL INFILE 'D:/Sem4 2D TRPL Aqsha/Python/GameFinder/dataset/steamgames_clean.csv'
INTO TABLE gamefinder.games
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(app_id, name, price_idr, positive, negative, rating_percentage, playtime_hours, genre, pc_level, header_image, short_description);
