import mysql.connector


config = {
    'user': "root",
    'password': 'MySQL030927',
    'host': 'localhost',
    'database': 'CS348'
}

def get_connector():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn

