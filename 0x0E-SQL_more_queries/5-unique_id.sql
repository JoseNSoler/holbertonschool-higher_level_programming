-- Creates a user with null name and default unique id 1.
CREATE TABLE 
    IF NOT EXISTS `unique_id` 
    (`id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256));