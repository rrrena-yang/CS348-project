# CS348-project

Our big idea is to develop a song-review web app. The database of the web app stores information such as textual reviews of songs, ratings of songs, song titles, song authors, singers, etc. The web app will support functionalities such as: sorting songs based on artists, regions, languages, trending, and reviews; searching for songs; adding/removing reviews for songs, etc. 

# How to run

1. Ensure you have mysql-server installed and running
2. Set your username and password in `bootstrap_test.sh` and `backend/SQLService.py`
3. Bootstrap your database by running `./bootstrap_test.sh`

4. Ensure you have `python3` and `pip` installed
5. Install python mysql connector `pip install -r requirements.txt`
6. run `python3 backend/server.py`

# R2. System support description:
Our application architecture utilizes a MySQL database managed via a Flask backend server. The Flask server implements API endpoints for each application feature, employing the mysql-python-connector to dynamically construct and execute SQL queries based on incoming data. This setup ensures efficient data management and seamless communication between the frontend and backend systems.

On the frontend, JavaScript, HTML, CSS, and potentially React are employed to facilitate user interaction and data fetching from the backend. This combination enables a responsive and interactive user experience. Currently, our development environment is local, aimed at streamlining the development process. However, we are considering future deployment on cloud infrastructure to enhance scalability and accessibility.

# R3. Database with sample dataset:
Data for the sample dataset can be found in `bootstrap_test.sql`. The corresopnding create table commands can be found in `create_table.sql` The idea is that we will build the testing database as we add more requirements for testing in the form of ``INSERT INTO table_name(attr...) VALUES (attr...)`. I.e., we will add more rows to the test database when we need to test more complex features when when we do more rigorous testing. This allows us to keep query outputs predictable, but also allows us to build up a testing database.

We also have scripts `bootstrap_test.sh` to reset the test database.

