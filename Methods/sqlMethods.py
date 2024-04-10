"""
    Methods for interacting with sqlite database.
"""
import sqlite3
from sqlite3 import Error
import FormatDataForPacks as form

def create_connection(db_path):
    """
        Creates a connection object to the given SQLite databse.
    :param db_path: POSIX path to SQLite database
    :return: Connection object or none
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """
        Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_sample(conn, sample):
    """
        Create a new sample into the samples table
    :param conn: Connection Object
    :param pack:
    :return:
    """
    sql = ''' INSERT INTO samples(sample_name,
                                    sample_path,
                                    xmp_path,
                                    Type,
                                    Sounds,
                                    Drums,
                                    Devices,
                                    Genres,
                                    Key,
                                    Grooves,
                                    Tunings,
                                    Creator,
                                    '1. Favorites',
                                    'Audio Cortex',
                                    Clips,
                                    'Drum Machines',
                                    Foley,
                                    label,
                                    pack,
                                    Plugins,
                                    Splice,
                                    places)
              VALUES(?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?) '''
    cur = conn.cursor()
    cur.execute(sql, sample)
    conn.commit()