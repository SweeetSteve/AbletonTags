"""

"""
import re
import os
from Methods import id3Methods as id



# TO FILTER FOR SPECIFIC FILES, ENTER THE APPROPRIATE DATA IN THE FOLLOWING LISTS:
extensions = ['aiff'] # e.g.: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}

# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/DJ Library (Practice)"

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
            id.set_song_key(sample_path)
            count += 1
            print(count)




