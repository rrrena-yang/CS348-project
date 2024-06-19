-- Use the newly created database
USE CS348_TEST;



-- Insert one row with the value 'World'
INSERT INTO HelloWorld (Hello) VALUES ('World');

-- Test Popularity Queries

INSERT INTO Album (AlbumID, Name) VALUES (1, 'Album1');

INSERT INTO Singer (SingerID, Name, Age, SongProduced, Country) VALUES (1, 'Teacher Tou', 30, 10, 'USA');
INSERT INTO Singer (SingerID, Name, Age, SongProduced, Country) VALUES (2, 'Teacher G', 30, 10, 'USA');

INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (1, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (2, 'password', 'username', 'name', 1999);
INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear)  VALUES 
    (3, 'password', 'username', 'name', 1999);

INSERT INTO Song (SongID, SingerID, SongName, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (1, 1, "AAA", '2021-01-01', 'Pop', 0, 100, 50, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (2, 1, "BBB", '2021-01-02', 'Pop', 0, 200, 100, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (3, 1, "CCC", "HHH", '2021-01-03', 'Pop', 0, 300, 150, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (4, 1, "DDD",'2021-01-03', 'Rock', 0, 300, 150, 'spotify.com', 'youtube.com', 1);
INSERT INTO Song (SongID, SingerID, PublishDate, Category, TotalReviewAmount, Liked, Disliked, SpotifyLink, YTLink, AlbumID) VALUES 
    (5, 1, "EEE",'2021-01-03', 'Rock', 0, 300, 150, 'spotify.com', 'youtube.com', 1);

INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-01', 1, 1, TRUE, 'Great Teacher Tou very epic');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-03', 1, 2, TRUE, 'Teacher G is good');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 2, 1, TRUE, 'Good Teacher G epic');
INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES 
    ('2021-01-02', 3, 1, FALSE, 'Good Teacher G epic');

SELECT * FROM SONG WHERE SongID = 1;