SELECT DISTINCT Song.SongID, Song.SongName
FROM Song, Singer 
WHERE Song.SingerID is NULL AND
    (Song.Liked+Song.Disliked) >= ALL(SELECT (Song.Liked+Song.Disliked) FROM Song WHERE Song.SingerID is NULL)