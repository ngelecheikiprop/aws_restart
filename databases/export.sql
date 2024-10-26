-- get data into table
SELECT Name, Age FROM people.uncles
INTO OUTFILE 'uncles.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
