from SQLService import get_connector
from flask import *


r7 = Blueprint('r7', __name__)

@r7.route('/api/<int:user_id>/rec', methods=['GET'])
def user_recommendation(user_id):
    query = """
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
        urs.UserID = %s
    ORDER BY 
        LikeCount DESC
    LIMIT 3
),
UserRec (SongID, SongName, Category, AlbumID, SingerID) AS (
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
    LIMIT 10
),
UserLikes AS (
    SELECT SongID
    FROM UserReviewOnSong
    WHERE UserID = %s AND IsLike = TRUE
), 
OtherUserLikes AS (
    SELECT UserID, SongID
    FROM UserReviewOnSong
    WHERE UserID != %s AND IsLike = TRUE
),
CommonLikes AS (
    SELECT ou.UserID
    FROM UserLikes ul
    JOIN OtherUserLikes ou ON ul.SongID = ou.SongID
    GROUP BY ou.UserID 
    HAVING COUNT(*) > 3
    ORDER BY COUNT(*) DESC
    LIMIT 1
),
MostSimilarUserLikes AS (
    SELECT SongID
    FROM CommonLikes cl
    JOIN UserReviewOnSong urs ON cl.UserID = urs.UserID
    WHERE urs.IsLike = TRUE
    LIMIT 3
),
MostSimilarUserLikeSongs AS (
    SELECT 
        s.SongID,
        s.SongName,
        s.Category,
        s.AlbumID,
        s.SingerID
    FROM 
        Song s
    JOIN
        MostSimilarUserLikes msl ON s.SongID = msl.SongID
)
SELECT * FROM UserRec ur
UNION
SELECT * FROM MostSimilarUserLikeSongs msls;
        """
    conn = get_connector()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (user_id))
    rows = cursor.fetchall()
    if not rows:
        print(f"No recommendations found for user_id: {user_id}")
    else:
        for row in rows:
            print(f"Recommended Song: {row['SongName']}")
    return render_template('user_recommendation.html', songs=rows)