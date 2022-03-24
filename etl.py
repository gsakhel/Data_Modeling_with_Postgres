import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Formats our song file data and inserts it into the database.
    
    Parameters:
    cur (psycopg2.extensions.cursor): Postgres cursor
    filepath (str): path to song file
    """
    
    # open song file
    df = pd.read_json(filepath, lines=True)
    
    # fill NA/NaNs with np.nan then replace with None so postgres can recognize NULL values
    df = df.fillna(np.nan).replace(np.nan, None)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 
                      'artist_latitude', 'artist_longitude']].values[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Formats our logfile data and inserts it into the database.
        
    Parameters:
    cur (psycopg2.extensions.cursor): Postgres cursor
    filepath (str): Path to log file
    """
    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong'].copy()

    # convert timestamp column to datetime
    t = pd.DataFrame(df['ts'].apply(lambda x: pd.to_datetime(x)))
    
    # insert time data records
    time_data = [t.ts, t.ts.dt.hour, t.ts.dt.day, t.ts.dt.isocalendar().week, 
                 t.ts.dt.month, t.ts.dt.year, t.ts.dt.weekday]
    column_labels = ['timestamp', 'hour', 'day', 'week_of_year', 
                     'month', 'year', 'weekday']
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid, duration = results
        else:
            songid, artistid, duration = None, None, None

        # insert songplay record
        songplay_data = [index, row.ts, row.userId, row.level, songid, 
                         artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Grabs the actual filenames containing our data and passes them 
    for further processing into the database.
        
    Parameters:
    cur (psycopg2.extensions.cursor): Postgres cursor
    conn (psycopg2.extensions.connection): Postgres connection
    filepath (str): Path to folder containing song or log files
    func (function): Function for processing the song or log files
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Main function, connects to postgress database and initiates data processing.
    """
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()