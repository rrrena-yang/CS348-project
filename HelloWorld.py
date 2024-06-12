import mysql.connector

config = {
    'user': "root",
    'password': 'MySQL030927',
    'host': 'localhost',
    'database': 'CS348_TEST'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

query = "SELECT * FROM HelloWorld"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row[0])