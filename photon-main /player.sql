
-- Create database
CREATE DATABASE game;

--Connect to database
\c game

--Create table
CREATE TABLE player (
  id INT,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  codename VARCHAR(30)
);

--Place first record into table
INSERT INTO player (id, codename)
VALUES (1, 'Bean'),
  (2, 'AIMS'),
  (3, 'jsliang0417'),
  (4, 'Carson'),
  (5, 'Diego');

--VALUES (1, 'Jim', 'Strother', 'Opus'), 


