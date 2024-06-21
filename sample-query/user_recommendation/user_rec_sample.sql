WITH UserProfile(UserID, Category, AlbumID, SingerID, LikeCount) AS (
    SELECT 
        urs.UserID,
        urs.Category,
        urs.AlbumID,
        urs.SingerID,
        urs.LikeCount
    FROM 
        UserPreferences urs
    WHERE 
        urs.UserID = 1
    ORDER BY 
        LikeCount DESC
    LIMIT 3
)
SELECT 
    s.SongID,
    s.SongName,
    s.Category,
    s.AlbumID,
    s.SingerID
FROM 
    Song s
WHERE 
    s.Category IN (SELECT Category FROM UserProfile)
    OR s.AlbumID IN (SELECT AlbumID FROM UserProfile)
    OR s.SingerID IN (SELECT SingerID FROM UserProfile)
-- ORDER BY 
--     RAND()
LIMIT 10;