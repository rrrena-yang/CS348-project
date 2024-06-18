from SQLService import get_connector
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

conn = get_connector()

# Example route for a simple GET request
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


# Get category for singer
@app.route('/api/category/<int:singer_id>', methods=['GET'])
def get_singer_category(singer_id):
    if not singer_id:
        raise Exception("No singer_id provided")
    
    
    query = f"SELECT Category, COUNT(*) AS NumberOfSongs FROM Song WHERE SingerID = {singer_id} GROUP BY Category ORDER BY NumberOfSongs DESC LIMIT 3"
    cursor =  conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise Exception(f"No song with SingerID {singer_id}")
    
    return jsonify(rows)


# Search For Song Reviews
@app.route('/api/review/<int:song_id>', methods=['GET'])
def search_for_song_reviews(song_id):
   if not song_id:
       raise Exception("No song_id provided")


   query = f"SELECT Review FROM UserReviewOnSong WHERE SongID = {song_id} "
   cursor = conn.cursor()
   cursor.execute(query)
   rows = cursor.fetchall()
   if len(rows) == 0:
       raise Exception(f"No reviews with song_id {song_id}")
  
  
   return jsonify(rows)

# Add User Song reviews
# ?? database route does not accept any url methods.
@app.route('/api/add_review/<int:song_id>/<int:user_id>/<is_like>/<review>', methods=['POST'])
def add_review(song_id, user_id, is_like, review):
    # data = request.json
    # song_id = data['song_id']
    # review = data['review']
    # user_id = data['user_id']
    # is_like = data['is_like']
    if not song_id:
        raise Exception("No song_id provided")
    if not review:
        raise Exception("No review provided")
    if not user_id:
        raise Exception("No user_id provided")
    print("asd")
    query = f"INSERT INTO UserReviewOnSong (UserID, SongID, IsLike, Review) VALUES ({user_id}, {song_id}, {is_like}, '{review}');"
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return jsonify(message="Review added successfully"), 201


if __name__ == '__main__':
    app.run(debug=True)
