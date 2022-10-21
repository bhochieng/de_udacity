import os
import glob
# import psycopg2
import pandas as pd
from sql_queries import *

# conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
# cur = conn.cursor()
print('disabled db connection')

def get_files(filepath):
    # rcount = 0
    # while rcount < 1:
    all_files = []
    rows=[]
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        # n = 0
        for f in files:
            df = pd.read_json(f, typ='series')
            # print(df)
            
            # song_id = df['song_id']
            # title = df['title']
            # artist_id=df['artist_id']
            # year=df['year']
            # duration=df['duration']
            for row in df:
                print('fgg',row[0])
                num_songs  = df['num_songs']  
                artist_id = df['artist_id']   
                artist_latitude=df['artist_latitude']
                artist_longitude=df['artist_longitude'] 
                artist_name=df['artist_name']  
                song_id = df['song_id']  
                title = df['title']  
                duration=df['duration']
                year=df['year']
                # print(song_id)
                song_data =  [song_id,title,artist_id,year,duration]
                # song_data = [('SOQOTLQ12AB01868D0', 'Clementina Santafè', 'ARGCY1Y1187B9A4FA5', 0, 153.33832)]
                # print(song_data)
            #     cur.execute('''
            #     insert into songs(song_id,title,artist_id,year,duration)
            #     VALUES (?,?,?,?,?)
            #     ''',
            #     song_id, 
            #     title,
            #     artist_id,
            #     year,
            #     duration
            #     )
            # conn.commit()
                # rows.append(song_data)
                
                all_files.append(os.path.abspath(f))
            
            # for d in song_data:
            #     print('testet')
            #     sql = "insert into songs(song_id,title,artist_id,year,duration) VALUES (%s, %s,%s,%s,%s)"
            #     cur.execute(sql, list(d))
            # n = n+1
        # if n > 1:
            # print('terenf')
                # cur.prepare('insert into songs(song_id,title,artist_id,year,duration) values (:1, :2, :3, :4, :5)')
                # cur.executemany(None, rows)
                # conn.commit()
        # rcount =  rcount+1

filepath = get_files('//Users/bhochieng/Downloads/project-template/data/song_data')


