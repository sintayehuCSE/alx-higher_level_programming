-- NOT IN Membership Operator
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN
(SELECT genre_id
FROM tv_shows
INNER JOIN  tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
