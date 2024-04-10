"""

"""
import sqlite3
from sqlite3 import Error
import createXMP as c_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes




def create_connection(db_path):
    """
        Creates a connection object to the given SQLite databse.
    :param db_path: POSIX path to SQLite database
    :return: Connection object or none
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except Error as e:
        print(e)
    return conn

def capAllWords(stringy):
    new_string = ''
    stringy = stringy.strip().split(' ')
    for word in stringy:
        new_string = new_string + ' ' + word.capitalize()

    #print(new_string)
    return new_string

def add_ableton_tag(keyword, sample_path):
    xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
        xmp_no.main(sample_path, keyword)
    elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
        xmp_yes.main(sample_path, keyword)
    #print(count)

def formatTags(sample_path, tags):
    tags = tags.strip().split(',')
    for tag in tags:
        tag = tag.strip()

        tag = capAllWords(tag)
        if tag == 'Fx':
            tag = 'FX'
        keyword = 'Splice|' + str(tag).strip()
        print(keyword)
        #add_ableton_tag(keyword, sample_path)

def formatLabel(sample_path, label):
    if label == 'Splice':
        label = 'Splice Sounds'
    if label != 'None':
        keyword = 'Creator|' + label
        #print(keyword)
        add_ableton_tag(keyword, sample_path)

def format_tag(splice_tag):
    """

    :param splice_tag:
    :return: String
    """
    dict = {
        #Genres
        'hip hop':'Genres|Hip Hop',
        'rnb':'Genres|R&B',
        'funk':'Genres|Funk',
        'trap':'Genres|Trap',
        'soul':'Genres|Soul',
        'electronic':'Genres|Electronic',
        'reggaeton':'Genres|Reggaeton',
        'dancehall':'Genres|Dancehall',
        'moombahton':'Genres|Moombahton',
        'future bass': 'Genres|Future Bass',
        'glitch hop': 'Genres|Glitch Hop',
        'techno': 'Genres|Techno',
        'house': 'Genres|House',
        'tech house': 'Genres|Tech House',
        'deep house': 'Genres|Deep House',
        'disco': 'Genres|Disco',
        'electro': 'Genres|Electro',
        'minimal techno': 'Genres|Minimal Techno',
        'melodic techno': 'Genres|Melodic Techno',
        'hard techno': 'Genres|Hard Techno',
        'dub techno': 'Genres|Dub Techno',
        'uk garage': 'Genres|UK Garage',
        'progressive house': 'Genres|Progressive House',
        'hardstyle': 'Genres|Hard Style',
        'pop': 'Genres|Pop',
        'edm': 'Genres|EDM',
        'trance': 'Genres|Trance',
        'psy trance': 'Genres|Psy Trance',
        'future house': 'Genres|Future House',
        'fidget house': 'Genres|Fidget House',
        'tropical house': 'Genres|Tropical House',
        'rock': 'Genres|Rock',
        'indie dance': 'Genres|Indie Dance',
        'jazz': 'Genres|Jazz',
        'heavy metal': 'Genres|Heavy Metal',
        'dub': 'Genres|Dub',
        'folk': 'Genres|Folk',
        'blues': 'Genres|Blues',
        'reggae': 'Genres|Reggae',
        'bass music': 'Genres|Bass Music',
        'drum and bass': 'Genres|Drum & Bass',
        'drumstep': 'Genres|Drumstep',
        'dubstep': 'Genres|Dubstep',
        'grime': 'Genres|Grime',
        'jungle': 'Genres|Jungle',
        'breakbeat': 'Genres|Breakbeat',
        'tearout dubstep': 'Genres|Tearout Dubstep',
        'leftfield bass': 'Genres|Leftfield Bass',
        'electronica': 'Genres|Electronica',
        'downtempo': 'Genres|Downtempo',
        'synthwave': 'Genres|Synthwave',
        'experimental': 'Genres|Experimental',
        'trip hop': 'Genres|Trip Hop',
        'ambient': 'Genres|Ambient',
        'idm': 'Genres|IDM',
        'chiptune': 'Genres|Chiptune',
        'footwork': 'Genres|Footwork',
        'global': 'Genres|Global',
        'african': 'Genres|African',
        'brazilian': 'Genres|Brazilian',
        'indian': 'Genres|Indian',
        'middle eastern': 'Genres|Middle Eastern',
        'asian': 'Genres|Asian',
        'caribbean': 'Genres|Caribbean',
        'latin american': 'Genres|Latin American',
        'south asian': 'Genres|South Asian',
        'cinematic': 'Genres|Cinematic',
        'game audio': 'Genres|Game Audio',
        'live sounds': 'Character|Live Sounds',
        #Drums
        'kicks': 'Drums|Kick',
        'hats': 'Drums|Hihat',
        'snares': 'Drums|Snare',
        'tops': 'Drums|Drum Loop|Top Drum Loop',
        'claps': 'Drums|Clap',
        'percussion': 'Drums|Percussion',
        'cymbals': 'Drums|Cymbal',
        'closed': 'Drums|Hihat|Closed Hihat',
        'fills': 'Drums|Drum Loop|Drum Fill Loop',
        'open': 'Drums|Hihat|Open Hihat',
        'toms': 'Drums|Tom',
        'crash': 'Drums|Cymbal|Crash',
        'shakers': 'Drums|Percussion|Shaker',
        'bells': 'Drums|Percussion|Bell',
        'hand drums': 'Drums|Percussion|Hand Drums',
        'conga': 'Drums|Percussion|Conga',
        'congo': 'Drums|Percussion|Congo',
        'tambourine': 'Drums|Percussion|Tambourine',
        'snaps': 'Drums|Percussion|Snap',
        'bongos': 'Drums|Percussion|Bongo',
        'cowbells': 'Drums|Percussion|Cowbell',
        'steel drum': 'Drums|Percussion|Steel Drum',
        'tabla': 'Drums|Percussion|Tabla',
        'waterphone': 'Drums|Percussion|Waterphone',
        'chimes': 'Drums|Percussion|Chime',
        'cajon': 'Drums|Percussion|Cajon',
        'rides': 'Drums|Cymbal|Ride',
        'rims': 'Drums|Snare|Rim',
        'grooves': 'Drums|Drum Loop|Grooves',
        #Sounds
        'bass': 'Sounds|Bass',
        'keys': 'Sounds|Piano & Keys',
        'mallets': 'Sounds|Mallets',
        'fx':'Sounds|Ambience & FX|Sound FX',
        'melody': 'Sounds|Chords & Phrases|Melody',
        'vocals': 'Sounds|Voice',
        'phrases': 'Sounds|Chords & Phrases|Phrase',
        'adlib': 'Sounds|Voice|Adlib',
        'hooks': 'Sounds|Voice|Jook',
        'female': 'Sounds|Voice|Female',
        'male': 'Sounds|Voice|Male',
        'spoken word': 'Sounds|Voice|Spoken Word',
        'shouts': 'Sounds|Voice|Shout',
        'harmony': 'Sounds|Chords & Phrases|Harmony',
        'chants': 'Sounds|Voice|Chant',
        'acapella': 'Sounds|Voice|Acapella',
        'opera': 'Sounds|Voice|Opera',
        'screams': 'Sounds|Voice|Scream',
        'verse': 'Sounds|Chords & Phrases|Verse',

        #Character
        'modular': 'Character|Modular',
        'drum machine': 'Character|Drum Machine',
        'organic': 'Character|Organic',
        'wet': 'Character|Wet',
        'dry': 'Character|Dry',
        'metallic': 'Character|Metallic',
        'ensemble': 'Character|Ensemble',
        'pitched': 'Character|Picthed',
        'chops': 'Character|Chop',
        'leads': 'Character|Lead',
        'riffs': 'Character|Riff',
        'processed': 'Character|Processed',
        'solo': 'Character|Solo',
        'layered': 'Character|Layered',

        #Splice
        'synth': 'Splice|Synth'
    }


local_path = 1
audio_key = 4
bpm = 5
chord_type = 6
sample_type = 13
tags = 14
Label = 19

database = '/Users/Shared/Music Production/Sample Database Files/sounds.db'

conn = create_connection(database)

cur = conn.cursor()
cur.execute("""SELECT * FROM samples""")

rows = cur.fetchall()

for row in rows:
    sample_path = str(row[local_path])
    #formatTags(sample_path, str(row[tags]))
    formatLabel(sample_path, str(row[19]))


    """
    print("local_path = " +  str(row[local_path]))
    print("audio_key = " + str(r ow[audio_key]))
    print("bpm = " + str(row[bpm]))
    print("chord_type = " + str(row[chord_type]))
    print("sample_type = " + str(row[sample_type]))
    print("Tags = " + str(row[tags]))
    print("Label = " + str(row[Label]))
    print()"""