SELECT Liked, Disliked FROM Song WHERE SongID = 6958;

INSERT INTO UserReviewOnSong (`Timestamp`, `UserID`, `SongID`, `IsLike`, `Review`)
VALUES
	('2023-09-11 04:12:10',100,6958,1,'I like the song');

SELECT Liked, Disliked FROM Song WHERE SongID = 6958;

UPDATE UserReviewOnSong
SET IsLike = 0, Review = 'I dislike the song'
WHERE UserID = 100 AND SongID = 6958;

SELECT Liked, Disliked FROM Song WHERE SongID = 6958;

-- THE TRIGGER FEATURE
-- CREATE TRIGGER UpdateSongLikenessAfterNewReview 
-- AFTER INSERT ON UserReviewOnSong
-- FOR EACH ROW
-- BEGIN 
--     IF (NEW.IsLike = TRUE) THEN
--         UPDATE Song
--         SET Liked = Liked + 1
--         WHERE SongID = NEW.SongID;
--     ELSE
--         UPDATE Song
--         SET Disliked = Disliked + 1
--         WHERE SongID = NEW.SongID;
--     END IF;
-- END;
-- 
-- CREATE TRIGGER UpdateSongLikenessAfterUpdateReview 
-- AFTER UPDATE ON UserReviewOnSong
-- FOR EACH ROW
-- BEGIN 
--     IF (NEW.IsLike = TRUE AND OLD.IsLike = False) THEN
--         UPDATE Song
--         SET Liked = Liked + 1, Disliked = Disliked - 1
--         WHERE SongID = NEW.SongID;
--     ELSEIF (NEW.IsLike = FALSE AND OLD.IsLike = TRUE) THEN
--         UPDATE Song
--         SET Disliked = Disliked + 1, Liked = Liked - 1
--         WHERE SongID = NEW.SongID;
--     END IF;
-- END;