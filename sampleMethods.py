"""

"""
import createXMP as c_xmp
import parseXMP as p_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes

def get_sample_name_from_sample_path(sample_path):
    """

    :param sample_path:
    :return:
    """
    return sample_path[sample_path.rfind('/') + 1:]

def get_xmp_path_from_sample_path(sample_path):
    """

    :param sample_path: String - sample POSIX path
    :return: String - POSIX path of the associated XMP file.
    """
    return sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'

def get_ableton_tags(sample_path):
    """

    :param sample_path:
    :param xmp_path:
    :return: Tuple - Entry 0 = Tag List, Entry 1 = Colors List
    :return: Tuple - Entry 0 = Tag List, Entry 1 = Colors List
    """
    xmp_path = get_xmp_path_from_sample_path(sample_path)


    sample_name = get_sample_name_from_sample_path(sample_path)
    xmp_string = c_xmp.read_xmp(xmp_path)
    tag_start = """                        <rdf:li>"""
    tag_end = '</rdf:li>\n'
    xmp_top = p_xmp.get_xmp_top(sample_name, xmp_string)
    xmp_string = xmp_string.replace(xmp_top, '')
    sample_entry = xmp_string[:xmp_string.find('</ablFR:keywords>') + 43]
    xmp_bottom = xmp_string.replace(sample_entry, '')
    keywords = p_xmp.get_keywords_as_list(sample_entry)
    colors = p_xmp.get_colors_as_list(sample_entry)
    return (keywords, colors)





def add_ableton_tag(keyword, sample_path):
    """

    :param keyword: String - new keyword (tag)
    :param sample_path: String - path of sample
    :return: No return
    """
    xmp_path = get_xmp_path_from_sample_path(sample_path)
    if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
        xmp_no.main(sample_path, keyword)
    elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
        xmp_yes.main(sample_path, keyword)

