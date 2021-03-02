-- List in descending order score in `second_table` above 10.
SELECT `score`, `name`
FROM `second_table`
WHERE score >= 10
ORDER BY score DESC