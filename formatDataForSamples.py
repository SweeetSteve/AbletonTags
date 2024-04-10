"""
    Methods for formatting data to input into samples table.
"""
import os
import subprocess
import sqlite3
import macos_tags
from macos_tags import Tag, Color
from mutagen.aiff import AIFF
from sqlite3 import Error
import re

def get_dir(conn, sample_path, pack_uuid):
    """

    :param conn: Connection object
    :param sample_path: POSIX path to sample file
    :param pack_uuid:
    :return:
    """
    query = "SELECT pack_path FROM packs WHERE uuid = \'" + pack_uuid + "\'"
    pack_path = ""
    try:
        c = conn.cursor()
        c.execute(query)
        pack_path = str(c.fetchall())
    except Error as e:
        print(e)
    pack_path = pack_path[3:len(pack_path) - 4] + "/"
    dir = sample_path.replace(pack_path, '')
    dir = dir[:dir.rfind('/')]
    return dir

def get_sample_name(sample_path):
    """
        Isolates and returns the sample name from the POSIX path of the sample.
    :param sample_path: The POSIX path of the sample
    :return: String - Name of the given sample
    """
    return sample_path[sample_path.rfind('/') + 1:].rstrip().lstrip()

def get_sample_type(sample_path):
    """
        Returns the type of sample. 0 = Loop, 1 = one-shot, 3 = unknown
    :param sample_path:
    :return: String
    """
    tags = str(macos_tags.get_all(sample_path))
    #sample = AIFF(sample_path)
    #sample_type = sample.pprint()
    #print(tags)
    if (tags.find('🔁') != -1):
        return 'Loop'
    elif (tags.find('1️⃣') != -1):
        return 'One Shot'
    else:
        return 'NULL'

def get_album(conn, sample_path, pack_uuid):
    """

    :param conn:
    :param sample_path:
    :param pack_uuid:
    :return:
    """
    query = 'SELECT name FROM packs WHERE uuid = \'' + pack_uuid + '\''
    album = ""
    try:
        c = conn.cursor()
        c.execute(query)
        album = str(c.fetchall())
    except Error as e:
        print(e)
    album = album[3:len(album) - 4]
    return album



def get_finder_tags(sample_path):
    """
        Returns the Finder Tags that are embedded in the sample file.
    :param sample_path:
    :return:
    """
    tags = ''
    for tag in macos_tags.get_all(sample_path):
        tags = tags + tag.name + ','
    if(tags == ''):
        tags = 'NULL'
    tags = tags[:len(tags) - 1]
    return tags

def get_key(sample_name):
    """

    :param sample_path:
    :return:
    """
    mid_major_pattern = "_[ABCDEFG]_"
    mid_major_sharp_pattern = "_[ABCDEFG]#_"
    mid_major_flat_pattern = "_[ABCDEFG]b_"
    start_major_pattern = "^[ABCDEFG]_"
    star_major_sharp_pattern = "^[ABCDEFG][_]"
    start_major_flat_pattern = "^[ABCDEFG]b_"

    mid_minor_pattern = "_[ABCDEFG]m_"
    mid_minor_sharp_pattern = "_[ABCDEFG]#m_"
    mid_minor_flat_pattern = "_[ABCDEFG]bm_"
    start_minor_pattern = "^[ABCDEFG]m_"
    start_minor_sharp_pattern = "^[ABCDEFG]#m_"
    start_minor_flat_pattern = "^[ABCDEFG]bm_"

    x = re.search(mid_major_pattern, sample_name)

def is_sample_exists(conn, sample_path):
    """

    :param conn:
    :param sample_name:
    :return:
    """

    query = 'SELECT filename FROM samples WHERE sample_path = ' + '\'' + sample_path + '\''
    sample = ""
    try:
        c = conn.cursor()
        c.execute(query)
        sample = str(c.fetchall())
        #print(sample)
    except Error as e:
        print(e)
    if sample != '[]':
        return True
    else:
        return False
    