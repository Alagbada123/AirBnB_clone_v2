-- prepares a MySQL server for the AirBnB clone
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user and grant privileges
GRANT ALL ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
