#
# SET OF SQL QUERIES USED IN create_tables.py AND etl.py.
#

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
songplay_table_create = """
    CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial PRIMARY KEY,
    start_time varchar REFERENCES time(start_time),
    user_id varchar REFERENCES users(user_id),
    level varchar REFERENCES users(level),
    song_id varchar REFERENCES songs(song_id),
    artist_id varchar REFERENCES artists(artist_id),
    session_id varchar,
    location varchar,
    user_agent varchar);"""

user_table_create = """
    CREATE TABLE IF NOT EXISTS users (
    user_id varchar PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    gender varchar,
    level varchar);"""

song_table_create = """
    CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year varchar,
    duration float);"""

artist_table_create = """
    CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar NOT NULL,
    location varchar,
    latitude varchar,
    longitude varchar);"""

time_table_create = """
    CREATE TABLE IF NOT EXISTS time (
    start_time varchar PRIMARY KEY,
    hour varchar NOT NULL,
    day varchar NOT NULL,
    week varchar NOT NULL,
    month varchar NOT NULL,
    year varchar NOT NULL,
    weekday varchar NOT NULL);"""

# INSERT RECORDS
songplay_table_insert = """
    INSERT INTO songplays
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING;"""

user_table_insert = """
    INSERT INTO users
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET level = EXCLUDED.level;"""

song_table_insert = """
    INSERT INTO songs
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;"""

artist_table_insert = """
    INSERT INTO artists
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING;"""

time_table_insert = """
    INSERT INTO time
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;"""

# FIND SONGS
song_select = """
    SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a
    ON s.artist_id = a.artist_id
    WHERE s.title = %s
    AND a.name = %s
    AND s.duration = %s;"""

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create,
                        time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop,
                      time_table_drop]
