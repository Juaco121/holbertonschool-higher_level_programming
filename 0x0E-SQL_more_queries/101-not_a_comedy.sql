-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
(SELECT tv_shows.title FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id AND tv_genres.name ='Comedy' INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id)
ORDER BY tv_shows.title;