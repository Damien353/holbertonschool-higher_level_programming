-- Script pour lister les genres et le nombre de shows liés à chaque genre
--

SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = genres.id
GROUP BY genres.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
