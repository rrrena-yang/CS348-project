WITH UserLikes AS (
    SELECT SongName
    FROM UserReviewOnSong
    WHERE UserID = 1 AND IsLike = TRUE
), 
OtherUserLikes AS (
    SELECT UserID, SongID
    FROM UserReviewOnSong
    WHERE UserID != 1 AND IsLike = TRUE
),
CommonLikes AS (
    SELECT ou.UserID
    FROM UserLikes ul
    JOIN OtherUserLikes ou ON ul.SongID = ou.SongID
    GROUP BY ou.UserID 
    HAVING COUNT(*) > 3
)
SELECT * FROM CommonLikes;



-- CommonLikes AS (
--     SELECT SongName
--     FROM UserLikes
--     INTERSECT
--     SELECT SongName
--     FROM OtherUserLikes
-- )

