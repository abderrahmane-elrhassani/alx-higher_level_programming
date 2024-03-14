-- Develop a script to list all genres from the 'hbtn_0d_tvshows' database and showcase the count of shows associated with each genre.
SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.genre_id) AS number_of_shows
    FROM tv_show_genres
    INNER JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
