from SQLService import get_connector
from flask import *

r10 = Blueprint('r10', __name__)

@r10.route('/user_info')
def user_info():
    if 'user_id' not in session:
        flash('You need to log in first', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    conn = get_connector()
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