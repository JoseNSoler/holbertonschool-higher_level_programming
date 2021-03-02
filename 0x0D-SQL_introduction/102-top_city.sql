-- List average temperature of city in table `temperatures`.
-- Only analyze range of months July and August
-- Use of database.
USE `hbtn_0c_0`;

-- Average temperature of cities.
SELECT `city`, AVG(value) AS `avg_temp`
FROM `temperatures`
WHERE `month`=7 OR `month`=8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;