WITH SingerWithSong AS (
    SELECT SingerID
    FROM Singer
    RIGHT OUTER JOIN Song ON Singer.SingerID = Song.SingerID
    WHERE Singer.SingerID IS NOT NULL
)
SELECT SingerID
FROM Singer
WHERE SingerID NOT IN (
    SELECT SingerID
    FROM SingerWithSong
);
