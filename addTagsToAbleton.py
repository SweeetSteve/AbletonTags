"""

"""
import Methods.sqlMethods as squeel
import sqlite3

database = "/Users/Shared/Music Production/Sample Database Files/SamplePacks.db"
# create a database connection
conn = squeel.create_connection(database)
cur = conn.cursor()

sql = '''SELECT sample_path, sample_type, genre FROM samples'''
cur.execute(sql)
samples = cur.fetchall()
for sample in samples:
    sample_path = sample[0]
    sample_type = sample[1]
    genre = sample[2]
    type_tag = 'Type|' + sample_type
    #print(type_tag)
    genre_tag = ''
    if genre != 'NULL':
        genre_tag = 'Genre|' + genre
        #print(genre_tag)