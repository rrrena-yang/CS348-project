# "Track URI","Track Name","Artist URI(s)","Artist Name(s)","Album URI","Album Name","Album Artist URI(s)","Album Artist Name(s)","Album Release Date","Album Image URL","Disc Number","Track Number","Track Duration (ms)","Track Preview URL","Explicit","Popularity","ISRC","Added By","Added At","Artist Genres","Danceability","Energy","Key","Loudness","Mode","Speechiness","Acousticness","Instrumentalness","Liveness","Valence","Tempo","Time Signature","Album Genres","Label","Copyrights"

import csv
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': "root",
    'password': 'MySQL030927',
    'host': 'localhost',
    'database': 'CS348'
}

# Connect to the database
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Connected to the database successfully, generating data, this will take a few minutes!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    exit(1)

# Read the CSV file
df = pd.read_csv('top_10000_1960-now.csv')


print("Generating Album, Song and Singer data...")
def create_maps_from_csv(file_path):
    name_to_birthdate = {}
    name_to_country = {}

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            artist = row['Name']
            birth_date = 2024 - int(row['Age'])
            country = row['Country']
            
            name_to_birthdate[artist] = birth_date
            name_to_country[artist] = country
    
    return name_to_birthdate, name_to_country

# Example usage:
file_path = 'artists.csv'  # Replace with the path to your CSV file
name_to_birthdate, name_to_country = create_maps_from_csv(file_path)


# Get the current max IDs for Singer and Album
cursor.execute("SELECT MAX(SingerID) FROM Singer")
max_singer_id = cursor.fetchone()[0]
if max_singer_id is None:
    max_singer_id = 0

cursor.execute("SELECT MAX(AlbumID) FROM Album")
max_album_id = cursor.fetchone()[0]
if max_album_id is None:
    max_album_id = 0

# Helper functions to insert or get data
def get_or_insert_singer(name):
    try:
        name = name.split(',')[0]
        global max_singer_id
        query = "SELECT SingerID FROM Singer WHERE Name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
                max_singer_id += 1
                year = name_to_birthdate.get(name)
                if year is None or year == "":
                    year = None
                else:
                    year = int(float(year))
                
                country = name_to_country.get(name)
                query = "INSERT INTO Singer (SingerID, Name, BirthYear, Country) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (max_singer_id, name, year, country))
                cnx.commit()
                return max_singer_id
    except Exception as e:
        return None

def get_or_insert_album(name):
    try:
        global max_album_id
        query = "SELECT AlbumID FROM Album WHERE Name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            max_album_id += 1
            query = "INSERT INTO Album (AlbumID, Name) VALUES (%s, %s)"
            cursor.execute(query, (max_album_id, name))
            cnx.commit()
            return max_album_id
    except Exception as e:
        return None

song_id = 0

import numpy as np

def format_date(date_str):
    if len(date_str) == 4:
        return f"{date_str}-01-01"  # Assuming January 1st for year-only dates
    return date_str

def insert_song(singer_id, song_name, publish_date ,category, spotify_link, album_id):
    global song_id
    try:
        first_cat = category.split(',')[0]
    except:
        first_cat = None
    query = """INSERT INTO Song (SongID, SingerID, PublishDate, SongName, Category, SpotifyLink, AlbumID)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    try:
        cursor.execute(query, (song_id, singer_id, format_date(publish_date), song_name, first_cat, spotify_link, album_id))
        cnx.commit()
        song_id += 1
    except Exception as e:
        return None
    return cursor.lastrowid

# Inserting data into tables
for _, row in df.iterrows():
    # Get or insert singer
    singer_id = get_or_insert_singer(row['Artist Name(s)'])
    
    # Get or insert album
    album_id = get_or_insert_album(row['Album Name'])
    
    # Insert song
    insert_song(singer_id, row['Track Name'],row['Album Release Date'] , row['Artist Genres'], row['Track URI'], album_id)

from faker import Faker
fake = Faker()

print("Generating User data...")
for i in range(100000):
    try:
        name = fake.name()
        birth_year = fake.year()
        username = fake.user_name()
        password = hash(fake.password())
        gender = fake.random_element(elements=('Male', 'Female'))
        country = fake.country()
        query = "INSERT INTO User (ID, UserPassword, UserName, Name, BirthYear, Gender, Location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (i, password, username, name, birth_year, gender, country))
        cnx.commit()
    except Exception as e:
        continue

# for each user, randomly like some songs and dislike some songs
print("Generating review on songs data...")
for i in range(100000):
    rand = np.random.randint(0, 10)
    if rand != 0:
        continue
    like_songs_count = np.random.randint(0, 5)
    dislike_songs_count = np.random.randint(0, 2)

    like_songs = np.random.choice(range(10000), like_songs_count, replace=False)
    dislike_songs = np.random.choice(range(10000), dislike_songs_count, replace=False)

    for song_id in like_songs:
        try:
            timestamp = fake.date_time_between(start_date='-365d', end_date='now')
            userid = i
            song_id = song_id.item()
            is_like = True
            review = fake.text()
            query = "INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (timestamp, i, song_id, True, review))
            cnx.commit()
        except Exception as e:
            continue
    
    for song_id in dislike_songs:
        try:
            timestamp = fake.date_time_between(start_date='-365d', end_date='now')
            userid = i
            song_id = song_id.item()
            is_like = False
            review = fake.text()
            query = "INSERT INTO UserReviewOnSong (Timestamp, UserID, SongID, IsLike, Review) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (timestamp, i, song_id, False, review))
            cnx.commit()
        except Exception as e:
            continue

# generate review for singer
print("Generating review on singer data...")
for i in range(10000):
    like_songs_count = np.random.randint(0, 3)
    dislike_songs_count = np.random.randint(0, 2)

    like_singers = np.random.choice(range(3000), like_songs_count, replace=False)
    dislike_singers = np.random.choice(range(3000), dislike_songs_count, replace=False)

    for singer_id in like_singers:
        try:
            timestamp = fake.date_time_between(start_date='-365d', end_date='now')
            userid = i
            singer_id = singer_id.item()
            is_like = True
            review = fake.text()
            query = "INSERT INTO UserReviewOnSinger (Timestamp, UserID, SingerID, IsLike, Review) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (timestamp, i, singer_id, True, review))
            cnx.commit()
        except Exception as e:
            continue

    for singer_id in dislike_singers:
        try:
            timestamp = fake.date_time_between(start_date='-365d', end_date='now')
            userid = i
            singer_id = singer_id.item()
            is_like = False
            review = fake.text()
            query = "INSERT INTO UserReviewOnSinger (Timestamp, UserID, SingerID, IsLike, Review) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (timestamp, i, singer_id, False, review))
            cnx.commit()
        except Exception as e:
            continue


print("Data inserted successfully.")


# Close the cursor and connection
cursor.close()
cnx.close()