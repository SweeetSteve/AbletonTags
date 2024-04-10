"""
Author: Stephen Shea
Date: 12/09/23

Contains methods that edit the embedded id3v2 data.
"""
import re
from mutagen.aiff import AIFF
import formatDataForSamples as sform
from pymusickit.key_finder import KeyFinder
from mutagen.id3 import TBPM
from mutagen.id3 import TCOP
from mutagen.id3 import APIC
from mutagen.id3 import TALB
from mutagen.id3 import TCON
from mutagen.id3 import COMM
from mutagen.id3 import TDES
from mutagen.id3 import TKEY




# GET Methods
def get_bpm(sample_path):
    """
        Returns the embedded BPM value.
    :param sample_path:
    :return: String - The BPM of the sample
    """
    try:
        sample = AIFF(sample_path)
        bpm = sample.pprint()
        if (bpm.find('TBPM=') != -1):
            bpm = str(sample.get('TBPM'))
        else:
            bpm = 'NULL'
        return bpm
    except:
        print('error')
        
def get_genre(sample_path):
    """
        Returns the genre that is embedded in the sample file.
    :param sample_path: POSIX path of an aiff sample
    :return: String - The genre of the sample
    """
    try:
        sample = AIFF(sample_path)
        genre = sample.pprint()
        if (genre.find('TCON=') != -1):
            genre = genre[genre.find('TCON='):].rstrip().lstrip()
            genre = genre[:genre.find('\n')]
            genre = genre.replace('TCON=', '')
            genre = genre.replace(' / ', ',')
        else:
            genre = 'NULL'
        return genre
    except:
        print('error')
        
def get_audio_key(sample_path):
    """
        Returns the audio key that is embedded in the sample file.
    :param sample_path:
    :return: String - The key of the sample
    """
    try:
        sample = AIFF(sample_path)
        key = sample.pprint()
        if (key.find('TKEY=') != -1):
            key = key[key.find('TKEY='):].rstrip().lstrip()
            key = key[:key.find('\n')]
            key = key.replace('TKEY=', '')
        else:
            key = 'NULL'
        return key
    except:
        print('error')
        
def get_artist(sample_path):
    """
        Returns the artist name that is embedded in the file.
    :param sample_path:
    :return: String - The artist of the sample
    """
    try:
        sample = AIFF(sample_path)
        artist = sample.pprint()

        if (artist.find('TPE1=') != -1):
            artist = artist[artist.find('TPE1='):].rstrip().lstrip()
            artist = artist[:artist.find('\n')]
            artist = artist.replace('TPE1=', '')
            artist = artist.replace(';;;', ',')
        else:
            artist = 'NULL'
        return artist
    except:
        print('error')

def get_album(sample_path):
    """
        Returns the album name that is embedded in the file.
    :param sample_path: String
    :return: String
    """
    try:
        sample = AIFF(sample_path)
        album = sample.pprint()
        if (album.find('TALB=') != -1):
            album = str(sample.get('TALB'))
        else:
            album = None
        return album
    except:
        return None

def get_description(sample_path):
    """
        Returns the description that is embedded in the file.
    :param sample_path:
    :return: String
    """
    sample = AIFF(sample_path)
    description = sample.pprint()
    if (description.find('TDES=') != -1):
        description = str(sample.get('TDES'))
    else:
        description = None
    return description

def get_creator(sample_path):
    """
        Returns the creator of the sample that is embedded in the file.
    :param sample_path: String
    :return: String
    """
    sample = AIFF(sample_path)
    creator = sample.pprint()
    if (creator.find('TCOP=') != -1):
        creator = str(sample.get('TCOP'))
    else:
        creator = None
    return creator

def get_pprint(sample_path):
    """
        Returns all the embedded properties.
    :param
        None
    :return: String
    """
    return AIFF(sample_path).pprint()




# SET Methods
def set_artwork(sample_path,art_path):
    """
        Embeds the given art into the given sample
    :param sample_path: String - POSIX Path to sample file
    :param art_path: String - POSIX path to artwork
    :return: None
    """
    try:
        sample = AIFF(sample_path)
        with open(art_path, 'rb') as albumart:
            sample['APIC'] = APIC(
                encoding=3,
                mime='image/jpeg',
                type=3, desc=u'Cover',
                data=albumart.read()
            )
        sample.save()
    except:
        print('error')

def set_comment(sample_path, comment):
    """
        Embeds the given comment into the given sample
    :param sample_path: String - POSIX Path to sample file
    :param description: String
    :return: None
    """
    sample = AIFF(sample_path)
    sample['COMM'] = COMM(text=comment)
    sample.save()

def set_description(sample_path, description):
    """
        Embeds the given description into the given sample
    :param sample_path: String - POSIX Path to sample file
    :param description: String
    :return: None
    """
    sample = AIFF(sample_path)
    sample['TDES'] = TDES(text=description)
    sample.save()

def set_key(sample_path, key):
    """
        Embeds the given key into the given sample
    :param sample_path: String - POSIX Path to sample file
    :param key: String
    :return: None
    """
    sample = AIFF(sample_path)
    sample['TKEY'] = TKEY(text=key)
    sample.save()

def set_song_key(sample_path):
    """
        Auto-detects the key of the given song and then embbeds the key into the song file
    :param sample_path: string - POSIX path of song
    :return: None
    """
    song = KeyFinder(sample_path)
    key = str(song.key_primary)
    song = AIFF(sample_path)
    if re.search(' major', key) != None:
        key = key.replace(' major', '')
        key = key + 'maj'
    elif re.search(' minor', key) != None:
        key = key.replace(' minor', '')
        key = key + 'min'
    song['TKEY'] = TKEY(text=key)
    song.save()




# CHECK Methods
def is_bpm_embedded(sample_path):
    """
        Checks if a sample has the bpm value embedded.
        1 = bpm is embedded
        0 = bpm is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        bpm = sample.pprint()
        if (bpm.find('TBPM=') != -1):
            return 1
        else:
            return 0
    except:
        print('error')
        
def is_genre_embedded(sample_path):
    """
        Checks if a sample has the genre embedded.
        1 = genre is embedded
        0 = genre is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        genre = sample.pprint()
        if (genre.find('TCON=') != -1):
            return 1
        else:
            return 0
    except:
        print('error')
        
def is_audio_key_embedded(sample_path):
    """
        Checks if a sample has the key embedded
        1 = key is embedded
        0 = key is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        key = sample.pprint()
        if (key.find('TKEY=') != -1):
            return 1
        else:
            return 0
    except:
        print('error')
        
def is_artist_embedded(sample_path):
    """
        Checks if a sample has the artists embedded.
        1 = artist is embedded
        0 = artist is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        artist = sample.pprint()
        if (artist.find('TPE1=') != -1):
           return 1
        else:
            return 0
    except:
        print('error')
        
def is_album_embedded(sample_path):
    """
        Checks if a sample has the album name embedded.
        1 = album is embedded
        0 = album is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        album = sample.pprint()
        if (album.find('TALB=') != -1):
            return 1
        else:
            return 0
    except:
        print('error')
        
def is_art_embedded(sample_path):
    """
        Checks if the sample pack art has been embedded.
        1 = art is embedded
        0 = art is not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
    except:
        return 0
    art = sample.pprint()
    if (art.find('APIC=') != -1):
        return 1
    else:
        return 0
    
def are_tags_embedded(sample_path):
    """
        Checks if a sample has the tags embedded.
        1 = tags are embedded
        0 = tags are not embedded
    :param sample_path: String - POSIX Path to sample file
    :return: int
    """
    try:
        sample = AIFF(sample_path)
        tags = sample.pprint()
        f_tags = ',' + sform.get_finder_tags(sample_path) + ','
        e_tags = ''
        if (tags.find('COMM==') != -1):
            e_tags = tags[tags.find('COMM==XXX='):].rstrip().lstrip()
            e_tags = e_tags[:e_tags.find('\n')]
            e_tags = e_tags.replace('COMM==XXX=','').replace(';;;', ',')
        if (f_tags == e_tags):
            return 1
        else:
            return 0
    except:
        print('error')
