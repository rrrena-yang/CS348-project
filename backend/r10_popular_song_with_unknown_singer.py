from flask import *

from SQLService import get_connector

r10 = Blueprint('r10', __name__)

@r10.route('/api/popular_song_unknown_singer', methods=['GET'])
def popular_song_unknown_singer():

    query = """SELECT DISTINCT Song.SongID, Song.SongName
FROM Song, Singer 
WHERE Song.SingerID is NULL AND
    (Song.Liked+Song.Disliked) >= ALL(SELECT (Song.Liked+Song.Disliked) FROM Song WHERE Song.SingerID is NULL)"""

    conn = get_connector()
    cursor = conn.cursor()
    cursor.execute(query)
    songs = cursor.fetchall()
    return render_template('user_recommendation2.html', songs=songs)