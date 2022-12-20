#Here we import the necessary python packages for the project.
import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

#This function drop the existing tables.
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

#This function creates tables.
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

#The main function creates connection string and calls the drop table and create table functions.
def main():
    config = configparser.ConfigParser()
    config.read('/Users/bhochieng/Documents/projects/de_udacity/datawarehouse/dwh.cfg')
    print(config.read('/Users/bhochieng/Documents/projects/de_udacity/datawarehouse/dwh.cfg'))

    #conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(HOST,DB_NAME,DB_USER,DB_PASSWORD,DB_PORT))
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    #conn_string="postgresql://{}:{}@{}:{}/{}".format(DWH_DB_USER, DWH_DB_PASSWORD, DWH_ENDPOINT, DWH_PORT,DWH_DB)
    print(conn)
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()

if __name__ == "__main__":
    main()