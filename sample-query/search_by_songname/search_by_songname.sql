SELECT song.SongID, song.SingerID, song.SongName, singer.Name as SingerName, song.Category 
FROM song song JOIN Singer singer ON song.singerID = singer.singerID 
WHERE SongName Like "AAA";