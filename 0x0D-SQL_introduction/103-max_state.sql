-- List average temperature of city in table `temperatures`.
-- Use of database.
USE `hbtn_0c_0`;

-- Average temperature of cities.
SELECT `State` AS `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `State`
ORDER BY `State` ASC;