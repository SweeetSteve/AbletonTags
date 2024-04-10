"""

"""
import os
import sys
import sqlite3
from sqlite3 import Error
import Methods.createXMP as c_xmp
import Methods.mainXMP_NO as xmp_no
import Methods.mainXMP_YES as xmp_yes


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

def add_ableton_tag(keyword, sample_path):
    new_keyword = keyword
    xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    sample_name = sample_path[sample_path.rfind('/') + 1:]

    if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
        xmp_no.main(sample_path, new_keyword)
    elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
        xmp_yes.main(sample_path, new_keyword)



database = '/Users/Shared/Music Production/Sample Database Files/SamplePacks.db'
conn = create_connection(database)
cur = conn.cursor()

sql = '''SELECT sample_path, sample_type, genre FROM samples'''
cur.execute(sql)
samples = cur.fetchall()
count = 0
for sample in samples:
    sample_path = sample[0]
    print(sample_path)
    sample_type = sample[1]
    genre = str(sample[2]).replace('-', ' ')
    type_tag = 'Type|' + sample_type
    #print(type_tag)
    genre_tag = ''
    if genre != 'NULL':
        count = count + 1
        genre_tag = 'Genres|' + genre
        #add_ableton_tag(genre_tag, sample_path)
        #print(count)
        print(genre_tag)

#tag = sys.argv[1]
#sample_path = sys.argv[2]

