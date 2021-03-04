-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- FORMAT: tv_shows.title - tv_show_genres.genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows, tv_show_genres, tv_genres
    WHERE  tv_shows.id = tv_show_genres.show_id
    GROUP BY tv_shows.title, tv_show_genres.genre_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;