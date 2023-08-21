-- Preparing MySQL server for the project
-- hbnb_dev_db database
-- new user hbnb_dev in localhost password is hbnb_dev_pwd
-- grant all privileges for hbnb_dev on hbnb_dev_db

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
