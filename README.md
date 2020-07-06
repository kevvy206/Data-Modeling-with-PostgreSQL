### Project Name
Data Modeling with PostgreSQL<br><br>

### Purpose
To perform ETL process on Spakify's dataset for its analytics team<br><br>

### Background Info
This project is a part of Udacity's Data Engineering Nanodegree program. Sparkify is a startup that runs music streaming app. The company's analytics team wants to know which songs its users listen to, and requested five tables of relational data. Raw data from the app is stored in JSON files, and ETL is performed on the data using a Python module.<br><br>

### How to Run
1. run 'create_tables.py'
2. run 'etl.py'<br><br>

### Process Detail 1: Running 'create_tables.py'
1. Creates database named sparkifydb
2. Creates five tables (as requests by the analytics team) in the database
   - Fact table: songplays
   - Dimention tables: songs, artists, users, time<br><br>

## Process Detail 2: Running 'etl.py'
##### Part 1
1. Extracts song-related data from 'data/song_data' directory
2. Transforms (certain columns of data)
3. Loads into two of the tables: songs, artists
#### Part 2
4. Extracts log-related data from 'data/log_data' directory
5. Transforms (change timestamp to datetime and select certain columns of data)
6. Loads into three of the tables: time, users, songplays<br><br>

### Result
5 tables (1 fact table, 4 dimension tables) for analysis
(by Spakify's analytics team)
