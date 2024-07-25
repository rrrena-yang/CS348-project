from SQLService import get_connector
from flask import *


r7 = Blueprint('r7', __name__)

@r7.route('/singer/<int:singer_id>')
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