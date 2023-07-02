-- Create the database hbtn_0d_usa and table states (in the database hbtn_0d_usa)
--  states description: 
--      id INT unique, auto generated, cant be null and is primary key
--      name VARCHAR(256) can't be null
--  If the database hbtn_0d_usa already exists, your script should not fail
--  If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL AUTO_INCREMENT, 
    `name` VARCHAR(256),
    PRIMARY KEY (`id`),
    UNIQUE (`id`)
);