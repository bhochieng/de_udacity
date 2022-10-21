# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES
#song plays as the fact table
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL, 
    start_time timestamptz NOT NULL, 
    user_id BIGINT NOT NULL, 
    level VARCHAR, 
    song_id VARCHAR , 
    artist_id VARCHAR , 
    session_id VARCHAR, 
    location VARCHAR, 
    user_agent VARCHAR,
    PRIMARY KEY (songplay_id)
    )
""")
#Rest of the tables are dimension tables.
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT NOT NULL, 
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    gender VARCHAR NOT NULL, 
    level VARCHAR NOT NULL,
    primary key (user_id)
    )
""")
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR NOT NULL, 
    title VARCHAR NOT NULL, 
    artist_id VARCHAR NOT NULL, 
    year int NOT NULL, 
    duration float NOT NULL,
    PRIMARY KEY (song_id)
    )
""")
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
artist_id VARCHAR NOT NULL, 
name VARCHAR NOT NULL, 
location VARCHAR NOT NULL, 
latitude FLOAT NOT NULL, 
longitude FLOAT NOT NULL,
PRIMARY KEY (artist_id)
)
""")
time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
    start_time timestamptz NOT NULL, 
    hour int NOT NULL, 
    day int NOT NULL, 
    week int NOT NULL, 
    month int NOT NULL, 
    year int NOT NULL, 
    weekday int NOT NULL,
    PRIMARY KEY (start_time))
""")
#/Users/bhochieng/Downloads/project-template/data/song_data/A/A/A/TRAAAAW128F429D538.json
# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
on conflict (songplay_id) do nothing
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s,%s,%s,%s,%s)
on conflict (user_id) do update set level = users.level
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s)
on conflict (song_id) do nothing
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO UPDATE SET name = artists.name, location = artists.location, latitude = artists.latitude, longitude = artists.longitude
""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES(%s,%s,%s,%s,%s,%s,%s)
on conflict (start_time) do nothing
""")

# FIND SONGS

song_select = ("""select a.song_id,b.artist_id from songs a join artists b on b.artist_id = a.artist_id where a.title = (%s) AND b.name = (%s) AND a.duration = (%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]