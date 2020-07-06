### How to Run
1. run 'create_tables.py'
2. run 'etl.py'

### Project Name
Data Modeling with Postgres

### Purpose
To perform ETL process on Spakify's dataset for its analytics team
* Sparkify is a startup that runs music streaming app
* The analytics team wants to know which songs its users listen to,
  and requested five tables of relational data
* Raw data from the app is stored in JSON files, and this project
  extracts data from them using a Python module.

### Process Detail 1: Running 'create_tables.py'
1. Creates database named sparkifydb
2. Creates five tables (as requests by the analytics team) in the database
   - Fact table: songplays
   - Dimention tables: songs, artists, users, time

### Process Detail 2: Running 'etl.py'
1. Extracts song-related data from 'data/song_data' directory
2. Transforms (select certain columns of data)
3. Loads into two of the tables: songs, artists

4. Extracts log-related data from 'data/log_data' directory
5. Transforms (change timestamp to datetime and select certain columns of data)
6. Loads into three of the tables: time, users, songplays

### Result
5 tables (1 fact table, 4 dimension tables) for analysis
(by Spakify's analytics team)
