-- Drop the database if it exists
DROP DATABASE IF EXISTS CS348_TEST;

-- Create the database
CREATE DATABASE CS348_TEST;

-- Use the newly created database
USE CS348_TEST;

-- Create the HelloWorld table with one column Hello
CREATE TABLE User (
    ID INT PRIMARY KEY,
    UserPassword VARCHAR(40) NOT NULL,
    UserName VARCHAR(30) NOT NULL,
    Name VARCHAR(30),
    BirthYear INT,
    Gender VARCHAR(10),
    Location VARCHAR(50)
);

CREATE TABLE Album (
    AlbumID INT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Singer (
    SingerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    SongProduced INT,
    Country VARCHAR(50)
);

CREATE TABLE Song (
    SongID INT PRIMARY KEY,
    SongName VARCHAR(50),
    SingerID INT,
    PublishDate DATE,
    Category VARCHAR(50),
    TotalReviewAmount INT,
    Liked INT,
    Disliked INT,
    SpotifyLink VARCHAR(255),
    YTLink VARCHAR(255),
    AlbumID INT,
    FOREIGN KEY (SingerID) REFERENCES Singer(SingerID),
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
);

CREATE TABLE UserReviewOnSong (
    Timestamp TIMESTAMP,
    UserID INT,
    SongID INT,
    IsLike BOOLEAN,
    Review TEXT,
    PRIMARY KEY (UserID, SongID),
    FOREIGN KEY (UserID) REFERENCES User(ID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID)
);

DELIMITER //

CREATE TRIGGER UpdateSongLikeness 
AFTER INSERT ON UserReviewOnSong
FOR EACH ROW
BEGIN 
    IF (NEW.IsLike = TRUE) THEN
        UPDATE Song
        SET Liked = Liked + 1
        WHERE SongID = NEW.SongID;
    ELSE
        UPDATE Song
        SET Disliked = Disliked + 1
        WHERE SongID = NEW.SongID;
    END IF;
END;

//

DELIMITER ;

CREATE TABLE UserReviewOnSinger (
    Timestamp TIMESTAMP,
    UserID INT,
    SingerID INT,
    IsLike BOOLEAN,
    Review TEXT,
    PRIMARY KEY (UserID, SingerID),
    FOREIGN KEY (UserID) REFERENCES User(ID),
    FOREIGN KEY (SingerID) REFERENCES Singer(SingerID)
);

CREATE TABLE PokeTable (
    UserID1 INT,
    UserID2 INT,
    SongID INT,
    Timestamp TIMESTAMP,
    PRIMARY KEY (UserID1, UserID2, SongID, Timestamp),
    FOREIGN KEY (UserID1) REFERENCES User(ID),
    FOREIGN KEY (UserID2) REFERENCES User(ID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID)
);

CREATE TABLE HelloWorld (
    Hello VARCHAR(255)
);