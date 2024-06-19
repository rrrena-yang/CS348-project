import os
from SQLService import get_connector
from flask import Flask, jsonify, request, render_template, send_from_directory

app = Flask(__name__, static_folder='../frontend/build/static', template_folder='../frontend/build')

conn = get_connector()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

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
