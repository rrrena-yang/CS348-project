import mysql.connector
import time

config = {
    'user': "root",
    'password': 'MySQL030927',
    'host': 'localhost',
    'database': 'CS348'
}

conn = mysql.connector.connect(**config)
conn.autocommit = True

cursor = conn.cursor()

# Start timer
start_time = time.time()
cursor.execute("SELECT * FROM User WHERE UserName like %s; ", ('dmartin',))
end_time = time.time()
# Calculate the duration
execution_time = end_time - start_time
result = cursor.fetchone()
print(f"Query result: {result}")
print(f"Query executed in: {execution_time} seconds")

