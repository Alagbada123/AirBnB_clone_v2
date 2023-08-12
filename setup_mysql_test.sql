-- script that prepares a MySQL server for the project
-- create a database, a new user and grant with all privileges

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
CREATE SCHEMA IF NOT EXISTS hbnb_test_db;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
