from SQLService import get_connector
from flask import Flask, jsonify, request, Blueprint

from SQLService import get_connector

r7 = Blueprint('r7', __name__)

@r7.route('/api/<int:user_id>/rec', methods=['GET'])
def user_recommendation(user_id):
    file_path = '../sample-query/user_recommendation/user_rec.txt'
    with open(file_path, 'r') as file:
        file_content = file.read()
    query = eval('f' + repr(file_content))
    conn = get_connector()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)