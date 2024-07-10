INSERT INTO User (ID, UserName, UserPassword, Name, BirthYear, Gender, Location) 
VALUES (1000001, 'tony03', 5907836549860929550, 'Ziheng Zhou', 2023, 'Male', 'Waterloo');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000001,1,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000001,2,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000001,3,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000001,4,1,'I like the song');

INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000000,1,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000000,2,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000000,3,1,'I like the song');
INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',1000000,4,1,'I like the song');

WITH UserLikes AS (
    SELECT SongID
    FROM UserReviewOnSong
    WHERE UserID = 1000000 AND IsLike = TRUE
), 
OtherUserLikes AS (
    SELECT UserID, SongID
    FROM UserReviewOnSong
    WHERE UserID != 1000000 AND IsLike = TRUE
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

