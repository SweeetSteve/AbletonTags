"""

"""
import re

def get_xmp_top(sample_name, xmp_string):
    end_index = xmp_string.find(sample_name) - 83
    header = xmp_string[:end_index]
    return header

def is_colors_exist(sample_entry):
    if (sample_entry.find('<ablFR:colors>') != -1):
        return True
    else:
        return False

def get_keywords(sample_entry, new_keyword):
    """

    :param sample_entry: string
    :param new_keyword: list
    :return: list
    """
    tag_start = """                        <rdf:li>"""
    tag_end = '</rdf:li>\n'
    sample_entry = sample_entry[sample_entry.find('<ablFR:keywords>'):].replace('<rdf:Bag>', '').replace('</rdf:Bag>', '').replace('</ablFR:keywords>', '').replace('<ablFR:keywords>', '')
    sample_entry = sample_entry[:sample_entry.rfind('</rdf:li>')]
    sample_entry = sample_entry.replace('</rdf:li>', ',').strip()
    keywords = sample_entry.split(',')
    keywords.pop(len(keywords) - 1)
    clean_keywords = ''
    for key in keywords:
        key = key.replace('<rdf:li>', '').strip()
        key = tag_start + key + tag_end
        clean_keywords = clean_keywords + key
    if (new_keyword != None):
        clean_keywords = clean_keywords + tag_start + new_keyword + tag_end
    return clean_keywords

def get_keywords_as_list(sample_entry):
    """

    :param sample_entry: string
    :return: list
    """
    tag_start = """                        <rdf:li>"""
    tag_end = '</rdf:li>\n'
    sample_entry = sample_entry[sample_entry.find('<ablFR:keywords>'):].replace('<rdf:Bag>', '').replace('</rdf:Bag>', '').replace('</ablFR:keywords>', '').replace('<ablFR:keywords>', '')
    sample_entry = sample_entry[:sample_entry.rfind('</rdf:li>')]
    sample_entry = sample_entry.replace('</rdf:li>', ',').strip()
    keywords = sample_entry.split(',')
    keywords.pop(len(keywords) - 1)
    clean_keywords = []
    for key in keywords:
        key = key.replace('<rdf:li>', '').strip()
        clean_keywords.append(key)
    return clean_keywords

def get_colors(sample_entry):
    """

    :param sample_entry:
    :return:
    """
    color_start = """                        <rdf:li>"""
    color_end = '</rdf:li>\n'
    sample_entry = sample_entry[sample_entry.find('<ablFR:colors>') + 14:sample_entry.find('</ablFR:colors>')]
    sample_entry = sample_entry.split('</rdf:li>\n')
    sample_entry.pop(len(sample_entry) - 1)
    new_colors = ''
    for color in sample_entry:
        color = color[color.find('<rdf:li>') + 8:]
        new_colors = new_colors + color_start + color + color_end
    return new_colors

def get_colors_as_list(sample_entry):
    """

    :param sample_entry:
    :return:
    """
    new_colors = []
    if (sample_entry.find('<ablFR:colors>') != -1):
        sample_entry = sample_entry[sample_entry.find('<ablFR:colors>') + 14:sample_entry.find('</ablFR:colors>')]
        sample_entry = sample_entry.split('</rdf:li>\n')
        sample_entry.pop(len(sample_entry) - 1)
        for color in sample_entry:
            color = color[color.find('<rdf:li>') + 8:]
            new_colors.append(color)
        return new_colors
    else:
        return None

def read_xmp(xmp_path):
    """

    :param xmp_path: POSIX path to xmp file
    :return: String - Contents of xmp file
    """
    f = open(xmp_path, 'r')
    xmp_string = f.read()
    f.close()
    return xmp_string





def create_new_sample_entry(sample_entry,new_keywords, sample_name):
    colors = get_colors(sample_entry)
    keywords = get_keywords(sample_entry, new_keywords)
    if sample_entry.find('<ablFR:colors>') != -1:
        entry = ('<ablFR:filePath>' + sample_name + '</ablFR:filePath>\n<ablFR:colors>\n<rdf:Bag>\n' + colors
                 + '</rdf:Bag>\n</ablFR:colors>\n<ablFR:keywords>\n<rdf:Bag>\n' + keywords + '</rdf:Bag>\n</ablFR:keywords>\n</rdf:li>\n')
    else:
        entry = ('<ablFR:filePath>' + sample_name + '</ablFR:filePath>\n<ablFR:keywords>\n<rdf:Bag>\n' + keywords + '</rdf:Bag>\n</ablFR:keywords>\n</rdf:li>\n')


    return entry

