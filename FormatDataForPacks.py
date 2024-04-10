"""
    Methods for formatting data to input into packs.
"""
import subprocess
import uuid
import os
from sqlite3 import Error

def get_file_contents(file_path):
    """
        Returns the contents of the given file as a string.
    :param file_path: Path to file.
    :return: String -
    """
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents

def gen_uuid():
    """
        Generates a new uuid value.
    :return: uuid value
    """
    return str(uuid.uuid4())

def gen_file_hash(file_path):
    """
        Generates an SHA256 hash from the given audio file.
    :param file_path: Path to audio file.
    :return: SHA256 hash of audio file.
    """
    command = "/opt/homebrew/Cellar/ffmpeg/6.0_1/bin/ffmpeg -loglevel error -i \"" + file_path + "\" -map 0 -f hash -"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    hash = result.stdout.replace("SHA256=", "").lstrip().rstrip()
    return hash

def get_pack_name(pack_path):
    """
        Isolates and returns the sample pack name from the POSIX path of the sample pack.
    :param pack_path: The POSIX path of the sample pack directory
    :return: String - The sample pack name
    """
    return pack_path[pack_path.rfind('/') + 1:].rstrip().lstrip()

def get_art_path(pack_path):
    """
        Returns the POSIX path of the sample pack artwork for the given sample pack.
    :param pack_path: String - POSIX path to sample pack directory
    :return: String - Path to sample pack art
    """
    art_path = pack_path + "/.metadata/" + get_pack_name(pack_path)
    if os.path.isfile(art_path + ".jpg"):
        return art_path + ".jpg"
    elif os.path.isfile(art_path + ".jpeg"):
        return art_path + ".jpeg"
    elif os.path.isfile(art_path + ".png"):
        return art_path + ".png"
    else:
        return "NULL"

def get_description(pack_path):
    """
        Returns the description of the sample pack.
    :param pack_path: POSIX path to the sample pack directory
    :return:
    """
    try:
        description = get_file_contents(pack_path + '/.metadata/description.txt').rstrip().lstrip()
    except:
        description = 'NULL'
    return description

def get_genre(pack_path):
    """
        Returns the genre of the given sample pack
    :param pack_path: POSIX path of sample pack directory
    :return: String - Sample pack genre
    """
    try:
        genre = get_file_contents(pack_path + '/.metadata/genre.txt').rstrip().lstrip()
    except:
        genre = 'NULL'
    return genre

def get_provider_name(pack_path):
    """
        Returns the provider of the given sample pack
    :param pack_path: POSIX path of sample pack directory
    :return: String - The sample pack provider
    """
    try:
        provider = get_file_contents(pack_path + '/.metadata/provider.txt').rstrip().lstrip()
    except:
        provider = 'NULL'
    return provider

def get_uuid(conn, pack_path):
    """

    :param conn:
    :param pack_path:
    :return: String
    """
    query = 'SELECT uuid FROM packs WHERE pack_path = \'' + pack_path + '\''
    uuid = ''
    try:
        c = conn.cursor()
        c.execute(query)
        uuid = str(c.fetchall())
    except Error as e:
        print(e)
    return uuid

def is_album_exist(conn, pack_path):
    """

    :param conn:
    :param pack_name:
    :return:
    """
    pack_path = pack_path.replace('\'', '\'\'')
    query = 'SELECT name FROM packs WHERE pack_path = ' + '\'' + pack_path + '\''
    #print(query)
    album = ""
    try:
        c = conn.cursor()
        c.execute(query)
        album = str(c.fetchall())
        #print(album)
    except Error as e:
        print(e)
    if album != '[]':
        return True
    else:
        return False

