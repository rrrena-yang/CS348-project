SELECT DISTINCT song.songID, song.SongName
FROM song, singer 
WHERE song.SingerID is NULL AND
    (song.Liked+song.Disliked) >= ALL(SELECT (song.Liked+song.Disliked) FROM song WHERE song.SingerID is NULL)