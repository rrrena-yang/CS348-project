from flask import Blueprint, json, request

from SQLService import get_connector

r10 = Blueprint('r10', __name__)

@r10.route('/api/popular_song_unknown_singer', methods=['POST'])
def popular_song_unknown_singer():

    query = """SELECT DISTINCT Song.SongID, Song.SongName
FROM Song, Singer 
WHERE Song.SingerID is NULL AND
    (Song.Liked+Song.Disliked) >= ALL(SELECT (Song.Liked+Song.Disliked) FROM Song WHERE Song.SingerID is NULL)"""

    conn = get_connector()
    cursor = conn.cursor()
    cursor.execute(query)
    songs = cursor.fetchall()
    conn.close()
    songs_list = [{"song_id": song[0], "song_name": song[1]} for song in songs]
    songs_json = json.dumps(songs_list, indent=4)

    return songs_json