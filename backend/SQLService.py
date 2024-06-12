import mysql.connector


config = {
    'user': "root",
    'password': 'MySQL030927',
    'host': 'localhost',
    'database': 'CS348_TEST'
}

def get_connector():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = "SELECT * FROM HelloWorld"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])
    return cursor

