SELECT SongName, COUNT(*)
FROM Song
    JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
    JOIN User ON UserReviewOnSong.UserID = User.ID
WHERE BirthYear >= 2000
    AND BirthYear <= 2010
    GROUP BY SongName;