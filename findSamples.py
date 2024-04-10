"""

"""
import os
import Methods.sqlMethods as squeel
from Methods import id3Methods as id
import addAbletonTag as ab_tag
import addSample as add
import re



# TO FILTER FOR SPECIFIC FILES, ENTER THE APPROPRIATE DATA IN THE FOLLOWING LISTS:
extensions = ['aiff'] # e.g.: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}

# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/Music Production/Ableton/User Library/Sample Packs"

database = "/Users/Shared/Music Production/Sample Database Files/Ableton Samples.db"

# create a database connection
conn = squeel.create_connection(database)

count = 0
def file_filter(file_path):
    is_file = False
    for extension in extensions:
        if (re.search(extension + '$', file_path)):
            is_file = True
    return is_file




for root, dirs, files in os.walk(walk_path):
    for file in files:
        sample_path = os.path.join(root, file)
        if (file_filter(sample_path)):
            count += 1
            print(count)
            #album = 'Packs|' + id.get_album(sample_path).replace(' -', ':')
            #print(album)
            #ab_tag.add_ableton_tag(album, sample_path)
            add.add_sample(conn, sample_path)