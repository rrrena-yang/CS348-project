from SQLService import get_connector
from flask import Flask, jsonify, request

app = Flask(__name__)

cursor = get_connector()

# Example route for a simple GET request
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

@app.route('/api/popularity/{song_id}', methods=['GET'])
def get_song_popularity():
    song_id = request.args.get('song_id')
    if not song_id:
        raise Exception("No song_id provided")
    
    query = f"SELECT * FROM Song WHERE song_id = %{song_id} LIMIT 1"
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise Exception(f"No song with song_id {song_id}")
    
    song = rows[0]
    return jsonify(song[5] + song[6])






    return jsonify(message="Hello, World!")

# Example route for a POST request
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    # Process the data here
    return jsonify(received_data=data), 201

if __name__ == '__main__':
    app.run(debug=True)
