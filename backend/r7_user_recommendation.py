from SQLService import get_connector
from flask import *


r7 = Blueprint('r7', __name__)

@r7.route('/api/<int:user_id>/rec', methods=['GET'])
def user_recommendation(user_id):
    query = f"""
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
        urs.UserID = {user_id}
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
LIMIT 10;
        """
    conn = get_connector()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    if not rows:
        print(f"No recommendations found for user_id: {user_id}")
    else:
        for row in rows:
            print(f"Recommended Song: {row['SongName']}")
    return render_template('user_recommendation.html', songs=rows)