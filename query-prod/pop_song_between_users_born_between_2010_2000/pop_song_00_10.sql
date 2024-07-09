WITH Likes AS (
    SELECT SongName
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = TRUE
),
Dislikes AS (
    SELECT SongName
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = FALSE
),
Diff AS (
    SELECT SongName
    FROM Likes
    EXCEPT ALL
    SELECT *
    FROM Dislikes
)
SELECT SongName,
    COUNT(*)
FROM Diff
GROUP BY SongName
ORDER BY COUNT(*) DESC;