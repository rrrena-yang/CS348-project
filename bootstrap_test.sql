-- Use the newly created database
USE CS348_TEST;


-- Insert one row with the value 'World'
INSERT INTO HelloWorld (Hello) VALUES ('World');

-- Test Popularity Queries

INSERT INTO Album (AlbumID, Name) VALUES (1, 'Album1');
INSERT INTO Album (AlbumID, Name) VALUES (2, 'Album2');

INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (1, 'Teacher To', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (2, 'Teacher G', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (3, 'Teacher C', 30, 10, 'USA');



INSERT INTO Singer (SingerID, Name, BirthYear, SongProduced, Country) VALUES (10, 'Teacher G', 30, 10, 'USA');

INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (1, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (2, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (3, 'password', 'username', 'name', 1999);

INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (4, 'password', 'John', 'John', 2001);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (5, 'password', 'Jane', 'Jane', 2002);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (6, 'password', 'hater', 'Hater', 2001);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (7, 'password', 'Joe', 'Joe', 2011);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (8, 'password', 'liker', 'liker', 2001);

INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (1, 1, "AAA", '2021-01-01', 'Pop', 0, 100, 50, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (2, 1, "BBB", '2021-01-02', 'Pop', 0, 200, 100, 'spotify.com', 'youtube.com', 1);
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
    ('2021-01-02', 2, 5, TRUE, 'Good Teacher G epic');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 3, 1, FALSE, 'Good Teacher G epic');

INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 4, 1, TRUE, 'Johns review');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 5, 1, TRUE, 'Janes review');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 6, 1, FALSE, 'Hater review');
 INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 8, 1, TRUE, 'liker review');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 7, 1, TRUE, 'Joes review');

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
