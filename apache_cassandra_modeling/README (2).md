### Apache cassandra project two.
Working with Apache Cassandra in Data engineering.
## Data Source:
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv

## Project Goal,
Understand how to work with apache cassandra and ingest data into apache cassandra.

First is to ingest the csv file into cassandra denormalized tables.

Then proceed to develop the queries that will answer the listed questions.

## Create queries to ask the following three questions of the data
1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'