-- List average temperature of city in table `temperatures`.
-- Use of database.
USE `hbtn_0c_0`;

-- Average temperature of cities.
SELECT `city`, AVG(value) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;