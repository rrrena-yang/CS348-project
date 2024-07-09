WITH Likes AS (
    SELECT Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = TRUE
),
Dislikes AS (
    SELECT Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = FALSE
),
Diff AS (
    SELECT SongID
    FROM Likes
    EXCEPT ALL
    SELECT *
    FROM Dislikes
)
SELECT SongName, Diff.SongID,
    COUNT(*)
FROM Diff
JOIN SONG on Diff.SongID = Song.SongID
GROUP BY Diff.SongID
ORDER BY COUNT(*) DESC
LIMIT 10;