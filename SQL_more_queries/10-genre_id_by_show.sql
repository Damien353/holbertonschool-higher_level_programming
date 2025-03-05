-- Script pour lister toutes les émissions avec au moins un genre, triées par titre et genre_id
--

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows_genres.shows_id = tv_show.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
