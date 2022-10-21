# Udacity Data Engineering Nano Degree Course Project.
## Project Requirements:
    ### Read Json files in the data directory and insert the data into the table.
    ### Design data base with fact and dimension tables.
    ### Pull data from the created tables.
## Experience withh the task:
    created tables with all varchar columns just to see how the id's are populated.
    ### Table names are:
        1. users.
        2. songs.
        3. artists.
        4. time.
        5. songs_plays -  fact table.
    I first experimented on reading the json file and parsing the values into strings and then atempting to insert into the database.
    I later on realized that the data was not being well inserted and gad to purge the db and try again.
    ### The learning part was on deciding the data types in the db.:
        I started with all varchar columns just to achieve a zero fail insert into the tables.
        I then proceeded to putting the correct data types to the tables and attempting to insert the data with the accurate data formats.
        The end goal was to drop all tables and receate them with the right data types.
    The next step was to identify the joins (foregin keys ), was able to do this and adjusted the tables creation query accordingly.
    Also added table contraints like, not null, unique and learnt alot from the project.

For this project, I got help from websites like:
    geeksforgeeks
    https://www.geeksforgeeks.org/insert-python-list-into-postgresql-database/,
    Stackoverflow
    https://stackoverflow.com/questions/25674169/how-does-the-list-comprehension-to-flatten-a-python-list-work
    realpython
    https://www.projectpro.io/recipes/connect-mysql-python-and-import-csv-file-into-mysql-and-create-table