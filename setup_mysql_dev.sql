-- Creates a MySQL server with:
--   Database hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd in localhost.
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   Grants SELECT privilege for hbnb_dev on performance_schema.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
    ON hbnb_dev_db.*
    TO 'hbhnb_dev'@ WITH GRANT OPTION;
GRANT SELECT 
    ON performance_schema.*
    TO 'hbhnb_dev'@ WITH GRANT OPTION;
FLUSH PRIVILEGES;
