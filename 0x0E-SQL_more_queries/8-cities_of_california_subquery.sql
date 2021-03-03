-- lists all the cities of California that can be found in a given database.

SELECT `id`, `name` FROM cities
    WHERE `state_id` IN (
        SELECT `id` FROM states
        WHERE `id` = 1
    ) ORDER BY `id`;