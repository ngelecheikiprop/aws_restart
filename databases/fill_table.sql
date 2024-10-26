-- create table to import data to
USE people;
CREATE TABLE IF NOT EXISTS uncles
(
	Name VARCHAR(10),
	Age INT
);
INSERT INTO uncles(Name, Age)
VALUES
	("Kirwa", 44),
	("Jack", 32);

