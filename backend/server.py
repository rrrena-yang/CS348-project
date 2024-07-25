from SQLService import get_connector
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
from r6_search_by_song_name import r6
from r14_user_recommendation import r14
from r7_singer_category import r7
from r15_popular_song_age_group import r15
from r8_popular_song_with_unknown_singer import r8
from r10_most_similar_user import r10
from r11_trigger_complementary import r11

# this file supports the basic functionality of the interface 
# including the sign up/login routine
# including the display of main and sub page
# for clearity, we divide the features to sub routine, please review backend/rx_feature_name for detail :)

app = Flask(__name__, template_folder='../templates/rock', static_folder='../static')
app.register_blueprint(r6)
app.register_blueprint(r7)
app.register_blueprint(r8)
app.register_blueprint(r10)
app.register_blueprint(r11)
app.register_blueprint(r14)
app.register_blueprint(r15)

conn = get_connector()

app.secret_key = "030927"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        print(f"Form submitted with query: {query}")  # Debug print
        return redirect(url_for('r6.search_results', query=query))
    return render_template('index.html')

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


@app.route('/song/<int:song_id>/data', methods=['GET', 'POST'])
def song_data(song_id):
    liked = request.args.get('liked')
    disliked = request.args.get('disliked')
    total_review_amount = request.args.get('total_review_amount')
    popularity = int(liked) - int(disliked)
    return render_template('data.html', liked = liked, disliked = disliked, total_review_amount =  total_review_amount, popularity = popularity )



if __name__ == '__main__':
    app.run(debug=True)
