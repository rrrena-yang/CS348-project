import mysql.connector

config = {
    'user': "",
    'password': '',
    'host': 'localhost',
    'database': 'CS348'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

query = "SELECT * FROM HelloWorld"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row[0])