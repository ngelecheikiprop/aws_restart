-- import file from csv
LOAD DATA INFILE '/var/lib/mysql-files/family.csv'
INTO TABLE people.family
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
