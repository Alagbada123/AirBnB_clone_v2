-- a script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_test_db;
GRANT ALL PRIVILEGES on hbnb_test_db.* TO 'hbnb_test'@'localhost';
USE performance_schema;
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
SET FOREIGN_KEY_CHECKS=1;