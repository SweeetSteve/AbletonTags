"""

"""
import sys
import createXMP as c_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes


def add_ableton_tag(keyword, sample_path):
    xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    sample_name = sample_path[sample_path.rfind('/') + 1:]

    if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
        xmp_no.main(sample_path, keyword)
    elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
        xmp_yes.main(sample_path, keyword)



new_keyword = str(sys.argv[1]).lstrip().rstrip()
if new_keyword == '':
    sys.exit()
sample_path = sys.argv[2]

xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
sample_name = sample_path[sample_path.rfind('/') + 1:]
new_keyword = new_keyword.strip()

if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
    xmp_no.main(sample_path, new_keyword)
elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
    xmp_yes.main(sample_path, new_keyword)

