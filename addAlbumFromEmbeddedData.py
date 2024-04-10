"""

"""
import sys
import createXMP as c_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes
from Methods import id3Methods as id3

sample_path = sys.argv[1]

if (id3.get_album(sample_path) != None):
    new_keyword = 'Sample Pack|' + id3.get_album(sample_path).lstrip().rstrip()
else: sys.exit()

new_xmp_string = ''

xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
sample_name = sample_path[sample_path.rfind('/') + 1:]

if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
    xmp_no.main(sample_path, new_keyword)
elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
    print(xmp_yes.main(sample_path, new_keyword))
