"""

"""
import os
import Methods.sqlMethods as squeel
from Methods import id3Methods as id
import addAbletonTag as ab_tag
import re



# TO FILTER FOR SPECIFIC FILES, ENTER THE APPROPRIATE DATA IN THE FOLLOWING LISTS:
extensions = ['aiff'] # e.g.: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}

# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/Music Production/Ableton/User Library/Sample Packs"

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
            pprint = id.get_pprint(sample_path)
            description = id.get_description(sample_path)
            if description != None:
                #print(description)
                ab_tag.add_ableton_tag(description, sample_path)
