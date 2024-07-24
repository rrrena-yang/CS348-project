from SQLService import get_connector
from flask import Flask, jsonify, request, Blueprint

from SQLService import get_connector

r8 = Blueprint('r8', __name__)

@r8.route('/api/category/<int:singer_id>', methods=['GET'])
def get_singer_category(singer_id):
    if not singer_id:
        raise Exception("No singer_id provided")
    query = "SELECT Category, COUNT(*) AS NumberOfSongs FROM Song WHERE SingerID = %s GROUP BY Category ORDER BY NumberOfSongs DESC LIMIT 3"
    conn = get_connector()
    cursor =  conn.cursor()
    cursor.execute(query, (singer_id))
    rows = cursor.fetchall()
    if len(rows) == 0:
        raise Exception(f"No song with SingerID {singer_id}")
    
    return jsonify(rows)