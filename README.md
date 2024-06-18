# CS348-project

Our big idea is to develop a song-review web app. The database of the web app stores information such as textual reviews of songs, ratings of songs, song titles, song authors, singers, etc. The web app will support functionalities such as: sorting songs based on artists, regions, languages, trending, and reviews; searching for songs; adding/removing reviews for songs, etc. 

# How to run

1. Ensure you have mysql-server installed and running
2. Set your username and password in `bootstrap_test.sh` and `backend/SQLService.py`
3. Bootstrap your database by running `./bootstrap_test.sh`

4. Ensure you have `python3` and `pip` installed
5. Install python mysql connector `pip install -r requirements.txt`
6. run `python3 backend/server.py`

