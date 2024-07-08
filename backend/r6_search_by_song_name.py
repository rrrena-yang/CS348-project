from SQLService import get_connector
from flask import Flask, jsonify, request, Blueprint, render_template

from SQLService import get_connector

r6 = Blueprint('r6', __name__)


@r6.route('/search', methods=['GET', 'POST'])
def search_results():
    query = request.args.get('query')
    print(f"Search results for query: {query}")  # Debug print
    if not query:
        return render_template('search_results.html', error="Please enter a search query.")
    search_query = f"SELECT song.SongID, song.SingerID, song.SongName, singer.Name, song.Category FROM Song JOIN Singer singer ON song.singerID = singer.singerID WHERE SongName Like %s  "
    conn = get_connector()
    cursor = conn.cursor()
    cursor.execute(search_query, (f"%{query}%",))
    results = cursor.fetchall()
    cursor.close()
    # can not pass the table directly, must use array
    songs = []
    for row in results:
        songs.append({
            "song_id": row[0],
            "singer_id": row[1],
            "song_name": row[2],
            "singer_name": row[3],
            "category": row[4],
            
        })
    return render_template('search_results.html', query=query, songs=songs)