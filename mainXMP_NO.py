"""

"""
import createXMP as c_xmp


def main(sample_path, new_keyword):
    xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    sample_name = sample_path[sample_path.rfind('/') + 1:]

    xmp_string = c_xmp.create_xmp_string_from_scratch(sample_name, new_keyword)
    c_xmp.write_xmp(xmp_path, xmp_string)
    #print(xmp_string)

