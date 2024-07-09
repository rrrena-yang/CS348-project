SELECT song.SongID, song.SingerID, song.SongName, singer.Name as SingerName, song.Category 
FROM Song JOIN Singer singer ON song.singerID = singer.singerID 
WHERE SongName Like "despacito";