#Import the python packages for the project.
import configparser
import os


# Read config file.
working_directory = os.getcwd()
file_path = working_directory + '/de_udacity/datawarehouse/dwh.cfg'
config = configparser.ConfigParser()
config.read(file_path)


# Get S3 and ARN details.
LOG_DATA = config.get("S3", "LOG_DATA")
LOG_JSONPATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")
ARN = config.get("IAM_ROLE", "ARN")

# DROP TABLES if exists
staging_events_table_drop = "DROP table IF EXISTS staging_events;"
staging_songs_table_drop = "DROP table IF EXISTS staging_songs;"
songplays_table_drop = "DROP table IF EXISTS songplays;"
users_table_drop = "DROP table IF EXISTS users;"
songs_table_drop = "DROP table IF EXISTS songs;"
artists_table_drop = "DROP table IF EXISTS artists;"
time_table_drop = "DROP table IF EXISTS time;"

# create events table
staging_events_table_create= ("""
CREATE TABLE staging_songs
(
  num_songs int,
  artist_id varchar,
  artist_latitude decimal,
  artist_longitude decimal,
  artist_location varchar,
  artist_name varchar,
  song_id varchar,
  title varchar,
  duration decimal,
  year int
);
""")
 #create songs table
staging_songs_table_create = ("""
CREATE TABLE staging_events
(
    artist          varchar,
    auth            varchar, 
    firstName       varchar,
    gender          varchar,   
    itemInSession   int,
    lastName        varchar,
    length          decimal,
    level           varchar, 
    location        varchar,
    method          varchar,
    page            varchar,
    registration    varchar,
    sessionId       int,
    song            varchar,
    status          int,
    ts              timestamp,
    userAgent       varchar,
    userId          int
);
""")
 #create songplay table
songplay_table_create = ("""
    CREATE TABLE songplays(
        songplay_id   int IDENTITY (0,1),
        start_time    timestamp       REFERENCES  time(start_time)    sortkey,
        user_id       int             REFERENCES  users(user_id) distkey,
        level           varchar       ,
        song_id       varchar         REFERENCES  songs(song_id),
        artist_id     varchar         REFERENCES  artists(artist_id),
        session_id    int             NOT NULL,
        location        varchar       ,
        user_agent    varchar         ,
        PRIMARY KEY (songplay_id)
    );
""")
 #create users table
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id       int distkey,
        first_name    varchar     ,
        last_name     varchar     ,
        gender          varchar   ,
        level           varchar   ,
        PRIMARY KEY (user_id)
    );
""")

#create songs table
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id   varchar sortkey,
        title     varchar         NOT NULL,
        artist_id varchar         NOT NULL,
        year        int           ,
        duration    decimal       ,
        PRIMARY KEY (song_id)
    );
""")

#create artist table
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id varchar sortkey,
        name        varchar        NOT NULL,
        location    varchar        ,
        latitude    decimal        ,
        logitude    decimal        ,
        PRIMARY KEY (artist_id)
    );
""")

#create time table
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time    timestamp sortkey,
        hour            int     NOT NULL,
        day             int     NOT NULL,
        week            int     NOT NULL,
        month           int     NOT NULL,
        year            int     NOT NULL,
        weekday         int     NOT NULL,
        PRIMARY KEY (start_time)
    );
""")

#copy events STAGING TABLE
staging_events_copy = ("""
    COPY staging_events 
        FROM {} 
        iam_role {} 
        
        FORMAT AS JSON {} 
        timeformat 'epochmillisecs'
        TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL;
""").format(LOG_DATA, ARN, LOG_JSONPATH)

#copy songs STAGING TABLE
staging_songs_copy = ("""
    COPY staging_songs 
        FROM {}
        iam_role {}
        
        FORMAT AS JSON 'auto' 
        TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL;
""").format(SONG_DATA, ARN)

# Ingest data into songplays table
songplay_table_insert = ("""

    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
        SELECT DISTINCT se.ts, 
                        se.userId, 
                        se.level, 
                        ss.song_id, 
                        ss.artist_id, 
                        se.sessionId, 
                        se.location, 
                        se.userAgent
        FROM staging_events se 
        INNER JOIN staging_songs ss 
            ON se.song = ss.title AND se.artist = ss.artist_name
        WHERE se.page = 'NextSong';

""")

# Ingest data into users table
user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
        SELECT DISTINCT se.userId, 
                        se.firstName, 
                        se.lastName, 
                        se.gender, 
                        se.level
        FROM staging_events se
        WHERE se.userId IS NOT NULL;
""")

# Ingest data into songs table
song_table_insert = ("""

    INSERT INTO songs (song_id, title, artist_id, year, duration) 
        SELECT DISTINCT ss.song_id, 
                        ss.title, 
                        ss.artist_id, 
                        ss.year, 
                        ss.duration
        FROM staging_songs ss
        WHERE ss.song_id IS NOT NULL;

""")
 # Ingest data into artists table
artist_table_insert = ("""

    INSERT INTO artists (artist_id, name, location, latitude, logitude)
        SELECT DISTINCT ss.artist_id, 
                        ss.artist_name, 
                        ss.artist_location,
                        ss.artist_latitude,
                        ss.artist_longitude
        FROM staging_songs ss
        WHERE ss.artist_id IS NOT NULL;

""")
 # Ingest data into time table
time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
        SELECT DISTINCT  se.ts,
                        EXTRACT(hour from se.ts),
                        EXTRACT(day from se.ts),
                        EXTRACT(week from se.ts),
                        EXTRACT(month from se.ts),
                        EXTRACT(year from se.ts),
                        EXTRACT(weekday from se.ts)
        FROM staging_events se
        WHERE se.page = 'NextSong';

""")

# Execute the QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, user_table_create,song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplays_table_drop, users_table_drop,songs_table_drop, artists_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert,artist_table_insert, time_table_insert]
