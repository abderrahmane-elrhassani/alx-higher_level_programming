-- Write a script that utilizes the 'hbtn_0d_tvshows' database to list all genres available.
SELECT
    tv_genres.name AS name
    FROM tv_show_genres
    INNER JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_genres.id
    AND tv_shows.title = 'Dexter'
    ORDER BY name;
