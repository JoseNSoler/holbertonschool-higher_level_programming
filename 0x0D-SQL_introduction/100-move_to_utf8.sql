-- convert all of the following to UTF8 in database `first_table`.

USE `hbtn_0c_0`;

-- For each database:
ALTER DATABASE
    `hbtn_0c_0`
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

-- For each table
ALTER TABLE
    `first_table`
    MODIFY COLUMN `name`
    VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
