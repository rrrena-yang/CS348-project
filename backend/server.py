from SQLService import get_connector
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
#from r5_search_by_song_name import r5
from r6_search_by_song_name import r6
from r14_user_recommendation import r14
from r7_singer_category import r7
from r15_popular_song_age_group import r15
from r8_popular_song_with_unknown_singer import r8

app = Flask(__name__, template_folder='../templates/rock', static_folder='../static')

#app.register_blueprint(r5)
app.register_blueprint(r6)
app.register_blueprint(r14)
app.register_blueprint(r7)
app.register_blueprint(r15)
app.register_blueprint(r8)

conn = get_connector()

app.secret_key = "030927"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        print(f"Form submitted with query: {query}")  # Debug print
        return redirect(url_for('r6.search_results', query=query))
    return render_template('index.html')

@app.route('/all_songs', methods=['GET'])
def all_songs():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Song")
    songs = cursor.fetchall()

    cursor.close()
    return render_template('all_songs.html', songs=songs)

@app.route('/all_singers', methods=['GET'])
def all_singers():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Singer")
    singers = cursor.fetchall()
    cursor.close()

    return render_template('all_singers.html', singers=singers)

@app.route('/singer/<int:singer_id>')
def singer_detail(singer_id):
    conn = get_connector()
    cursor = conn.cursor()
    
    # Query to get singer details
    singer_query = """
    SELECT SingerID, Name, BirthYear, Country 
    FROM Singer 
    WHERE SingerID = %s
    """
    cursor.execute(singer_query, (singer_id,))
    singer = cursor.fetchone()
    
    if not singer:
        return render_template('singer_detail.html', error="Singer not found.")
    
    # Query to get top 3 categories
    category_query = """
    SELECT Category, COUNT(*) AS NumberOfSongs 
    FROM Song 
    WHERE SingerID = %s 
    GROUP BY Category 
    ORDER BY NumberOfSongs DESC 
    LIMIT 3
    """
    cursor.execute(category_query, (singer_id,))
    categories = cursor.fetchall()
    print(categories)
    cursor.close()
    
    singer_data = {
        "singer_id": singer[0],
        "name": singer[1],
        "age": singer[2],
        "country": singer[3]
    }
    
    return render_template('singer_detail.html', singer=singer_data, categories=categories)

@app.route('/api/hello',methods=['GET', 'POST'])
def hello():
    return jsonify(message="Hello, World!")


# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form.get('name')
        birthyear = request.form.get('birthyear')
        gender = request.form.get('gender')
        location = request.form.get('location')
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(ID) FROM User")
        uid = cursor.fetchone()[0]
        new_uid = (uid + 1) if uid else 1

        cursor.execute("""
            INSERT INTO User (ID, UserName, UserPassword, Name, BirthYear, Gender, Location)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (new_uid, username, password, name, birthyear, gender, location))

        conn.commit()
        cursor.close()

        flash('Sign up successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('sign_up.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor(buffered=True)

        cursor.execute("SELECT ID, UserPassword FROM User WHERE UserName = %s", (username,))
        user = cursor.fetchone()
        if user and user[1] == password:
            session['user_id'] = user[0]
            flash('Login successful!', 'success')
            return redirect(url_for('user_info'))
        else:
            flash('Invalid username, email, or password', 'danger')
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/user_info')
def user_info():
    if 'user_id' not in session:
        flash('You need to log in first', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    cursor = conn.cursor(dictionary=True)

    # Fetch user details
    cursor.execute("SELECT * FROM User WHERE ID = %s", (user_id,))
    user = cursor.fetchone()
    
    # Fetch user reviews
    cursor.execute("""
        SELECT s.SongName AS SongName, si.Name AS SingerName, ur.IsLike, ur.Review
        FROM UserReviewOnSong ur 
        JOIN Song s ON ur.SongID = s.SongID 
        JOIN Singer si ON si.SingerID = s.SingerID 
        WHERE ur.UserID = %s
    """, (user_id,))
    reviews = cursor.fetchall()
    
    # Fetch common likes
    cursor.execute(f"""
        WITH UserLikes AS (
            SELECT SongID
            FROM UserReviewOnSong
            WHERE UserID = {user_id} AND IsLike = TRUE
        ),
        OtherUserLikes AS (
            SELECT UserID, SongID
            FROM UserReviewOnSong
            WHERE UserID != {user_id} AND IsLike = TRUE
        ),
        CommonLikes AS (
            SELECT ou.UserID
            FROM UserLikes ul
            JOIN OtherUserLikes ou ON ul.SongID = ou.SongID
            GROUP BY ou.UserID
            HAVING COUNT(*) > 3
        )
        SELECT cl.UserID, u.UserName, s.SongName
        FROM CommonLikes cl
        JOIN User u ON cl.UserID = u.ID
        JOIN UserReviewOnSong ur ON ur.UserID = cl.UserID
        JOIN Song s ON ur.SongID = s.SongID
        WHERE ur.IsLike = TRUE;
    """)
    results = cursor.fetchall()
    
    # Organize data by user
    common_likes = {}
    for row in results:
        user_id = row['UserID']
        if user_id not in common_likes:
            common_likes[user_id] = {
                "username": row['UserName'],
                "songs": []
            }
        common_likes[user_id]["songs"].append(row['SongName'])
    
    cursor.close()

    return render_template('user.html', user=user, reviews=reviews, common_likes=common_likes)


@app.route('/song/<int:song_id>', methods=['GET', 'POST'])
def song_detail(song_id):
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        user_id = session.get('user_id')
        if not user_id:
            flash('You need to log in first', 'danger')
            return redirect(url_for('login'))

        is_like = request.form.get('is_like') == 'true'
        review = request.form.get('review')
        
        cursor.execute("""
            INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review)
            VALUES (NOW(), %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                Timestamp = NOW(),
                IsLike = VALUES(IsLike),
                Review = VALUES(Review)
        """, (user_id, song_id, is_like, review))
        
        conn.commit()
        flash('Review submitted successfully', 'success')
    
    cursor.execute("SELECT * FROM Song LEFT JOIN Singer singer ON song.singerID = singer.singerID WHERE SongID = %s", (song_id,))
    song = cursor.fetchone()

    cursor.execute("""
        SELECT ur.Review, ur.IsLike, u.UserName
        FROM UserReviewOnSong ur
        JOIN User u ON ur.UserID = u.ID
        WHERE ur.SongID = %s
    """, (song_id,))
    reviews = cursor.fetchall()
    
    cursor.close()

    return render_template('song_detail.html', song=song, reviews=reviews)


@app.route('/song/<int:song_id>/data', methods=['GET', 'POST'])
def song_data(song_id):
    liked = request.args.get('liked')
    disliked = request.args.get('disliked')
    total_review_amount = request.args.get('total_review_amount')
    popularity = int(liked) - int(disliked)
    return render_template('data.html', liked = liked, disliked = disliked, total_review_amount =  total_review_amount, popularity = popularity )

@app.route('/api/popularity/<int:song_id>', methods=['GET'])
def get_song_popularity(song_id):
    if not song_id:
        raise Exception("No song_id provided")
    print(song_id)
    query = f"SELECT (Liked - Disliked) AS TotalLikes FROM Song WHERE SongID = %s;"
    cursor = conn.cursor()
    cursor.execute(query, (song_id))
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


   query = f"SELECT Review FROM UserReviewOnSong WHERE SongID = %s "
   cursor = conn.cursor()
   cursor.execute(query, (song_id))
   rows = cursor.fetchall()
   if len(rows) == 0:
       raise Exception(f"No reviews with song_id {song_id}")
  
  
   return jsonify(rows)



if __name__ == '__main__':
    app.run(debug=True)
