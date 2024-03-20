-- Creates a Mysql server for the project
-- with a user and authentication
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating server user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the necessary DB
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- Reload instruction into memory
FLUSH PRIVILEGES;
