import os
import sys
import createXMP as c_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes

def add_ableton_tag(keyword, sample_paths):
    count = 0
    new_keyword = keyword
    for sample_path in sample_paths:
        count = count + 1
        xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
        sample_name = sample_path[sample_path.rfind('/') + 1:]

        if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
            xmp_no.main(sample_path, new_keyword)
        elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
            xmp_yes.main(sample_path, new_keyword)
        print(count)

directory = '/Users/Shared/Music Production/Sample Database Files/m3u for Ableton Tags'

for filename in os.listdir(directory):
    if (filename == '.DS_Store'):
        continue
    full_path = os.path.join(directory, filename)
    sample_paths_string = c_xmp.read_xmp(full_path).rstrip().lstrip()
    sample_paths = sample_paths_string.split('\n')
    keyword = filename.replace('.m3u8', '').replace('.m3u', '')
    add_ableton_tag(keyword, sample_paths)