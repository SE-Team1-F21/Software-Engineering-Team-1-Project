
-- Create database
CREATE DATABASE credentials;

--Connect to database
\c credentials

--Create table
CREATE TABLE credentials (
  _user VARCHAR(100),
  _password VARCHAR(100),
  _host VARCHAR(100),
  _port VARCHAR(100),
  _database VARCHAR(100)
);

--Place first record into table
INSERT INTO credentials (_user, _password, _host, _port, _database)
VALUES ('leemdipikfjyvk', 'b02a82e4e956bd6b2308b373258f48e20d291ac795fbea568105ef238cd5a324', 'ec2-23-22-191-232.compute-1.amazonaws.com', '5432', 'd8c1130jk9t7t2');



"""
user = 'leemdipikfjyvk'
password = 'b02a82e4e956bd6b2308b373258f48e20d291ac795fbea568105ef238cd5a324'
host = 'ec2-23-22-191-232.compute-1.amazonaws.com'
port = '5432'
database = 'd8c1130jk9t7t2'
"""