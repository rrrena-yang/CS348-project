# CS348-project

Our big idea is to develop a song-review web app. The database of the web app stores information such as textual reviews of songs, ratings of songs, song titles, song authors, singers, etc. The web app will support functionalities such as: sorting songs based on artists, regions, languages, trending, and reviews; searching for songs; adding/removing reviews for songs, etc. 

# How to run
1. Ensure you have mysql-server (v.8.0.31) installed and running
2. Set your username and password in `bootstrap_test.sh` and `bootstrap.sh`
3. Bootstrap your database by running `./bootstrap_test.sh` and `bootstrap.sh` Note that this will create CS348 and CS348_TEST databases

# How to test
1. Follow the instructions in `how to run` section
2. Set your user and password in `test_test.sh`
3. run `./test_test.sh` to test all queries in sample-query
4. Set your user and password in `test_prod.sh`
5. run `./test_prod.sh` to test all queries in query-prod. Note that each run rebootstraps your database.

Alternatives, you can execute each query in sample-query manually.

#  How to run flask server
1. Follow instructions in `how to run` section
2. Set your username and password in `backend/SQLService.py`
3. Install python packages `pip install -r requirements.txt`
4. run `python3 backend/server.py`
5. navigate to `127.0.0.1:5000` to use the UI (you can try searching for song `aaa` in the top right)
   
# Some features supported by our UI.
See submission PDF for detailed instructions.


