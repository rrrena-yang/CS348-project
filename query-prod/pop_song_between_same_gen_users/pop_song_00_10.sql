WITH Likes AS (
    SELECT SongName, Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = TRUE
),
Dislikes AS (
    SELECT SongName, Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= 2000
        AND BirthYear <= 2010
        AND IsLike = FALSE
),
Diff AS (
    SELECT SongName, SongID
    FROM Likes
    EXCEPT ALL
    SELECT *
    FROM Dislikes
)
SELECT SongName,
    COUNT(*)
FROM Diff
GROUP BY SongID, SongName
ORDER BY COUNT(*) DESC, SongName
LIMIT 10;