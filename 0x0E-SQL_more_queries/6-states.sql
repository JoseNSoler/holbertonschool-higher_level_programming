-- Creates the database hbtn_0d_usa and the table states inside the first mentioned
-- Creates database.
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_usa`;

-- Select DataBase.
USE `hbtn_0d_usa`;

-- Creates Table.
CREATE TABLE 
    IF NOT EXISTS `states` 
    (`id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
    ) AUTO_INCREMENT = 1;
