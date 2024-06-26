# CS348-project

Our big idea is to develop a song-review web app. The database of the web app stores information such as textual reviews of songs, ratings of songs, song titles, song authors, singers, etc. The web app will support functionalities such as: sorting songs based on artists, regions, languages, trending, and reviews; searching for songs; adding/removing reviews for songs, etc. 

# How to run
1. Ensure you have mysql-server (v.8.0.31) installed and running
2. Set your username and password in `bootstrap_test.sh`
3. Bootstrap your database by running `./bootstrap_test.sh`

# How to test
1. Follow the instructions in `how to run` section
2. Set your user and password in `test.sh`
3. run `./test.sh` to test all queries in sample-query

Alternatives, you can execute each query in sample-query manually.

# (IN PROGRESS) How to run flask server
1. Follow instructions in `how to run` section
2. Set your username and password in `backend/SQLService.py`
3. Install python mysql connector `pip install -r requirements.txt`
4. run `python3 backend/server.py`
5. navigate to `localhost:5000` to use the UI (you can try searching for song `aaa` in the top right)
   
# Some features supported by our UI.
## Search for song
## Check for song popularity (like + dislike)

# Additional features supported by backend
## Find singer category: 
list categories for singers

1. send a GET request to `http://localhost:5000/api/category/<singerID>`
2. should return category and the number of songs for each category for the given singer

example: `http://localhost:5000/api/category/2`

## Find song reviews:
list reviews for a song
1. send a GET request to `http://localhost:5000/api/review/<int:song_id>`
2. should return the reviews for the song 
3. 
example: `http://localhost:5000/api/review/1`


