#Import the python packages
import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries
import os


#Call the load staging tables queries form the sql_queries file
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

#Call the inser tables queries form the sql_queries file
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

# defines connection to cloud through config file and Executes the above two functuons insert_tables and load_staging_tables
def main():
    working_directory = os.getcwd()
    file_path = working_directory + '/de_udacity/datawarehouse/dwh.cfg'
    config = configparser.ConfigParser()
    config.read(file_path)

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()