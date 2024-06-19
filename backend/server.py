from SQLService import get_connector
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='../templates/rock', static_folder='../static')

conn = get_connector()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        print(f"Form submitted with query: {query}")  # Debug print
        return redirect(url_for('search_results', query=query))
    return render_template('index.html')


@app.route('/api/hello',methods=['GET', 'POST'])
def hello():
    return jsonify(message="Hello, World!")

@app.route('/search',methods=['GET', 'POST'])
def search_results():
    query = request.args.get('query')
    print(f"Search results for query: {query}")  # Debug print
    if not query:
        return render_template('search_results.html', error="Please enter a search query.")
    search_query = f"SELECT * FROM Song WHERE SongID Like %s "
    cursor = conn.cursor()
    cursor.execute(search_query, (f"%{query}%",))
    results = cursor.fetchall()
    cursor.close()
    songs = []
    for row in results:
        songs.append({
            "song_id": row[0],
            "name": row[1],
            "singer_id": row[2],
            "publish_date": row[3],
            "category": row[4],
            "total_review_amount": row[5],
            "liked": row[6],
            "disliked": row[7],
            "spotify_link": row[8],
            "yt_link": row[9],
            "album_id": row[10]
        })
    return render_template('search_results.html', query=query, songs=songs)


@app.route('/api/popularity/<int:song_id>', methods=['GET'])
def get_song_popularity(song_id):
    if not song_id:
        raise Exception("No song_id provided")
    print(song_id)
    query = f"SELECT (Liked + Disliked) AS TotalLikes FROM Song WHERE SongID = {song_id};"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise Exception(f"No song with song_id {song_id}")
    
    song = rows[0]
    return jsonify({"popularity": song[0]})

# Example route for a POST request
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    # Process the data here
    return jsonify(received_data=data), 201

if __name__ == '__main__':
    app.run(debug=True)
