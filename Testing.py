"""

"""
import sampleMethods as samp
import sqlMethods as squeel
from mutagen.aiff import AIFF
from Classes.sampleClass import Sample
#import id3Methods as id3
import os



"""
# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/Music Production/Ableton/User Library/Sample Packs"

ableton_database = "/Users/Shared/Music Production/Sample Database Files/Ableton Samples.db"
sample_packs_database = '/Users/Shared/Music Production/Sample Database Files/SamplePacks.db'

# create a database connection
conn_ablton = squeel.create_connection(ableton_database)
cur_ablton = conn_ablton.cursor()

conn_sample_packs = squeel.create_connection(sample_packs_database)
cur_sample_packs = conn_sample_packs.cursor()

query = '''SELECT sample_path, sample_type, genre FROM samples'''
cur_sample_packs.execute(query)
samples = cur_sample_packs.fetchall()
for sample in samples:
    sample_path = sample[0]
    sample_type = sample[1]
    genre = sample[2]
    type_tag = ('Type|' + sample_type).strip()
    #print(type_tag)
    samp.add_ableton_tag(type_tag, sample_path)
    genre_tag = ''
    if genre != 'NULL':
        genre_tag = 'Genre|' + genre
        #print(genre_tquery

print(len(samples))
"""
sample_path = '/Users/Shared/Music Production/Ableton/User Library/Sample Packs/Artists/Bigwhite Beatz/808\'S N HIT\'S #1/BWB 808\'S N HIT\'S [808]/BWB 808\'S N HIT\'S [808] (2).aiff'
sample = Sample(sample_path)
print(sample.get_sample_name())
print(sample.get_sample_path())
print(sample.get_pack_name())
print(sample.get_pack_path())
print(sample.get_extention())