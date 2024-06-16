-- Multiple table joins
SELECT g.name FROM tv_genres AS g
INNER JOIN tv_show_genres ON g.id = tv_show_genres.genre_id
INNER JOIN tv_shows AS t ON t.id = tv_show_genres.show_id
WHERE t.title = 'Dexter' ORDER BY g.name;
