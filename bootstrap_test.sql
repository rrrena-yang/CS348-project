-- Use the newly created database
USE CS348_TEST;


-- Insert one row with the value 'World'
INSERT INTO HelloWorld (Hello) VALUES ('World');

-- Test Popularity Queries

INSERT INTO Album (AlbumID, Name) VALUES (1, 'Album1');
INSERT INTO Album (AlbumID, Name) VALUES (2, 'Album2');

<<<<<<< HEAD
INSERT INTO Singer (SingerID, Name, Age, SongProduced, Country) VALUES (1, 'Teacher To', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, Age, SongProduced, Country) VALUES (2, 'Teacher G', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, Age, SongProduced, Country) VALUES (3, 'Teacher C', 30, 10, 'USA');

=======
INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (1, 'Teacher Tou', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (2, 'Teacher G', 30, 10, 'USA');
>>>>>>> 5764398199a08c68e76e25132f74ef05fd21e5c3

INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (1, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (2, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (3, 'password', 'username', 'name', 1999);

INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (1, 1, "AAA", '2021-01-01', 'Pop', 0, 100, 50, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (2, 2, "AAA", '2021-01-02', 'Pop', 0, 200, 100, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (3, 2, "CCC", '2021-01-03', 'Pop', 0, 300, 150, 'spotify.com', 'youtube.com', 2);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (4, 2, "DDD", '2021-01-03', 'Rock', 0, 300, 150, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (5, 3, "EEE",'2021-01-03', 'Rock', 0, 300, 150, 'spotify.com', 'youtube.com', 2);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (6, 3, "LOL",'2021-01-03', 'Rap', 0, 300, 150, 'spotify.com', 'youtube.com', 2);


INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-01', 1, 1, TRUE, 'Great Teacher Tou very epic');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-03', 1, 2, TRUE, 'Teacher G is good');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 2, 1, TRUE, 'Good Teacher G epic');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 3, 1, FALSE, 'Good Teacher G epic');

-- View to aggregate user preferences
CREATE VIEW UserPreferences AS
SELECT 
    urs.UserID,
    s.Category,
    s.AlbumID,
    s.SingerID,
    COUNT(*) AS LikeCount
FROM 
    UserReviewOnSong urs
JOIN 
    Song s ON urs.SongID = s.SongID
JOIN 
    User u ON urs.UserID = u.ID
WHERE 
    urs.IsLike = TRUE
GROUP BY 
    urs.UserID, s.Category, s.AlbumID, s.SingerID;


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
LIMIT 3;

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
ORDER BY 
    RAND()
LIMIT 10;


-- SELECT 
--     s.SongID,
--     s.SongName,
--     s.Category,
--     s.AlbumID,
--     s.SingerID
-- FROM 
--     Song s
-- WHERE 
--     s.Category IN (SELECT Category FROM UserPreferences WHERE UserID = 2)
--     OR s.AlbumID IN (SELECT AlbumID FROM UserPreferences WHERE UserID = 2)
--     OR s.SingerID IN (SELECT SingerID FROM UserPreferences WHERE UserID = 2)
-- ORDER BY 
--     RAND()
-- LIMIT 10;


SELECT * FROM Song WHERE SongID = 1;
