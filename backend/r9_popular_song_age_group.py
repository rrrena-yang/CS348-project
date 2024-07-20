from flask import *

from SQLService import get_connector

r9 = Blueprint('r9', __name__)

@r9.route('/api/popular_song_age_group', methods=['POST','GET'])
def popular_song_age_group():
    songs = None
    start_year = None
    end_year = None
    if request.method == 'POST':
        start_year = request.form.get('startYear', 0)
        end_year = request.form.get('endYear', 2999)
        
        query = """
        WITH Likes AS (
    SELECT SongName, Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= %s
        AND BirthYear <= %s
        AND IsLike = TRUE
),
Dislikes AS (
    SELECT SongName, Song.SongID
    FROM Song
        JOIN UserReviewOnSong ON Song.SongID = UserReviewOnSong.SongID
        JOIN User ON UserReviewOnSong.UserID = User.ID
    WHERE BirthYear >= %s
        AND BirthYear <= %s
        AND IsLike = FALSE
),
Diff AS (
    SELECT SongName, SongID
    FROM Likes
    EXCEPT ALL
    SELECT *
    FROM Dislikes
)
SELECT SongName, SongID,
    COUNT(*)
FROM Diff
GROUP BY SongID, SongName
ORDER BY COUNT(*) DESC, SongName
LIMIT 10;
        """

        conn = get_connector()
        cursor = conn.cursor()
        cursor.execute(query, (start_year, end_year, start_year, end_year))
        songs = cursor.fetchall()
        conn.close()
        songs = [{"songname": song[0], "song_id": song[1], "popular": song[2]} for song in songs]

    return render_template('popular_songs.html', songs=songs, start_year=start_year, end_year=end_year)

