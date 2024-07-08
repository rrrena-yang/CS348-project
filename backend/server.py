from SQLService import get_connector
from flask import Flask, jsonify, request, render_template, redirect, url_for
from r6_search_by_song_name import r6
from r7_user_recommendation import r7
from r8_singer_category import r8
from r9_popular_song_age_group import r9
from r10_popular_song_with_unknown_singer import r10

app = Flask(__name__, template_folder='../templates/rock', static_folder='../static')

app.register_blueprint(r6)
app.register_blueprint(r7)
app.register_blueprint(r8)
app.register_blueprint(r9)
app.register_blueprint(r10)
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


@app.route('/song/<int:song_id>', methods=['GET', 'POST'])
def song_detail(song_id):
    search_query = f"SELECT * FROM Song WHERE SongID Like %s "
    cursor = conn.cursor()
    #print("hhhh"+ song_id)
    cursor.execute(search_query, (song_id,))
    result = cursor.fetchone()
    cursor.close()
    if not result:
        print(f"No song found with ID: {song_id}")  # Debug print
        return "Song not found", 404
    song = {
        "song_id":  result[0],
        "singer_id": result[1],
        "name":  result[2],
        "publish_date": result[3],
        "category": result[4],
        "total_review_amount": result[5],
        "liked":  result [6],
        "disliked":  result [7],
        "spotify_link": result [8],
        "yt_link":  result[9],
        "album_id":  result[10]
    }
    return render_template('song_detail.html', song=song)

@app.route('/song/<int:song_id>/data', methods=['GET', 'POST'])
def song_data(song_id):
    liked = request.args.get('liked')
    disliked = request.args.get('disliked')
    total_review_amount = request.args.get('total_review_amount')
    popularity = int(disliked) + int(liked)
    return render_template('data.html', liked = liked, disliked = disliked, total_review_amount =  total_review_amount, popularity = popularity )

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
