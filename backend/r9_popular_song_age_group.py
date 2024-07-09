from flask import *

from SQLService import get_connector

r9 = Blueprint('r9', __name__)

@r9.route('/api/popular_song_age_group', methods=['POST','GET'])
def popular_song_age_group():
    # data payload is in JSON format {startYear: int, endYear: int}
    data = request.get_json()
    startYear = data.get('startYear', 0)
    endYear = data.get('endYear', 2999)
    # Query to get the most popular song for each age group

    query = f"""
WITH Likes AS (
SELECT *
FROM Song
    JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
    JOIN User ON UserReviewOnSong.UserID = User.ID
WHERE BirthYear >= {startYear}
    AND BirthYear <= {endYear}
    AND IsLike = TRUE
),
Dislikes AS (
    SELECT SongName
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= {startYear}
        AND BirthYear <= {endYear}
        AND IsLike = FALSE
),
Diff AS (
    SELECT SongName
    FROM Likes
    EXCEPT ALL
    SELECT *
    FROM Dislikes
)
SELECT SongName,
    COUNT(*)
FROM Diff
GROUP BY SongName;"""
    
    conn = get_connector()
    cursor = conn.cursor()
    cursor.execute(query, (startYear, endYear, startYear, endYear))
    songs = cursor.fetchall()
    return render_template('user_recommendation.html', songs=songs)
