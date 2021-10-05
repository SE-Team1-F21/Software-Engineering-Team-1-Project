
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
INSERT INTO player (id, first_name, last_name, codename)
VALUES (1, 'Jose', 'Martinez', 'Bean'),
  (2, 'Alexis', 'Mercado', 'AIMS'),
  (3, 'Steve', 'Liang', 'jsliang0417'),
  (4, 'Carson', 'Reed', 'Carson'),
  (5, 'Diego', 'Castro', 'Diego');

--VALUES (1, 'Jim', 'Strother', 'Opus'), 