from SQLService import get_connector
from flask import *
from SQLService import get_connector

r11 = Blueprint('r11', __name__)


@r11.route('/song/<int:song_id>', methods=['GET', 'POST'])
def song_detail(song_id):
    conn = get_connector()
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