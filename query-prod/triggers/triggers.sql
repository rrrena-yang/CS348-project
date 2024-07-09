CREATE TRIGGER UpdateSongLikenessAfterNewReview 
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



CREATE TRIGGER UpdateSongLikenessAfterUpdateReview 
AFTER UPDATE ON UserReviewOnSong
FOR EACH ROW
BEGIN 
    IF (NEW.IsLike = TRUE AND OLD.IsLike = False) THEN
        UPDATE Song
        SET Liked = Liked + 1, Disliked = Disliked - 1
        WHERE SongID = NEW.SongID;
    ELSEIF (NEW.IsLike = FALSE AND OLD.IsLike = TRUE) THEN
        UPDATE Song
        SET Disliked = Disliked + 1, Liked = Liked - 1
        WHERE SongID = NEW.SongID;
    END IF;
END;

