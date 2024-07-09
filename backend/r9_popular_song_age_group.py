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
        
        query = f"""
        WITH Likes AS (
            SELECT s.SongName, s.SongID
            FROM Song s
                JOIN UserReviewOnSong ur ON s.SongID = ur.SongID
                JOIN User u ON ur.UserID = u.ID
            WHERE u.BirthYear >= {start_year}
                AND u.BirthYear <= {end_year}
                AND ur.IsLike = TRUE
        ),
        Dislikes AS (
            SELECT s.SongName, s.SongID
            FROM Song s
                JOIN UserReviewOnSong ur ON s.SongID = ur.SongID
                JOIN User u ON ur.UserID = u.ID
            WHERE u.BirthYear >= {start_year}
                AND u.BirthYear <= {end_year}
                AND ur.IsLike = FALSE
        ),
        Diff AS (
            SELECT l.SongName, l.SongID
            FROM Likes l
            EXCEPT ALL
            SELECT d.SongName, d.SongID
            FROM Dislikes d
        )
        SELECT d.SongName, d.SongID,
            COUNT(*) AS Popularity
        FROM Diff d
        GROUP BY d.SongName, d.SongID;
        """

        conn = get_connector()
        cursor = conn.cursor()
        cursor.execute(query)
        songs = cursor.fetchall()
        conn.close()
        songs = [{"songname": song[0], "song_id": song[1], "popular": song[2]} for song in songs]

    return render_template('popular_songs.html', songs=songs, start_year=start_year, end_year=end_year)

