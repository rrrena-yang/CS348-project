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

-- WITH UserProfile(UserID, Category, AlbumID, SingerID, LikeCount) AS (
--     SELECT 
--         urs.UserID,
--         urs.Category,
--         urs.AlbumID,
--         urs.SingerID,
--         urs.LikeCount
--     FROM 
--         UserPreferences urs
--     WHERE 
--         urs.UserID = 9999
--     ORDER BY 
--         LikeCount DESC
--     LIMIT 3
-- ),
-- UserRec (SongID, SongName, Category, AlbumID, SingerID) AS (
--     SELECT 
--         s.SongID,
--         s.SongName,
--         s.Category,
--         s.AlbumID,
--         s.SingerID
--     FROM 
--         Song s
--     WHERE 
--         s.Category IN (SELECT Category FROM UserProfile)
--         OR s.AlbumID IN (SELECT AlbumID FROM UserProfile)
--         OR s.SingerID IN (SELECT SingerID FROM UserProfile)
--     LIMIT 10
-- ),
-- UserLikes AS (
--     SELECT SongID
--     FROM UserReviewOnSong
--     WHERE UserID = 9999 AND IsLike = TRUE
-- ), 
-- OtherUserLikes AS (
--     SELECT UserID, SongID
--     FROM UserReviewOnSong
--     WHERE UserID != 9999 AND IsLike = TRUE
-- ),
-- CommonLikes AS (
--     SELECT ou.UserID
--     FROM UserLikes ul
--     JOIN OtherUserLikes ou ON ul.SongID = ou.SongID
--     GROUP BY ou.UserID 
--     HAVING COUNT(*) > 3
--     ORDER BY COUNT(*) DESC
--     LIMIT 1
-- ),
-- MostSimilarUserLikes AS (
--     SELECT SongID
--     FROM CommonLikes cl
--     JOIN UserReviewOnSong urs ON cl.UserID = urs.UserID
--     WHERE urs.IsLike = TRUE
--     LIMIT 3
-- ),
-- MostSimilarUserLikeSongs AS (
--     SELECT 
--         s.SongID,
--         s.SongName,
--         s.Category,
--         s.AlbumID,
--         s.SingerID
--     FROM 
--         Song s
--     JOIN
--         MostSimilarUserLikes msl ON s.SongID = msl.SongID
-- )
-- SELECT * FROM UserPreferences up
-- UNION
-- SELECT * FROM MostSimilarUserLikeSongs msls;