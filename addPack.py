"""

"""

import sys
import FormatDataForPacks as form
import sqlMethods as squeel
from sqlite3 import Error

database = "/Users/Shared/Music Production/Sample Database Files/SamplePacks.db"
conn = squeel.create_connection(database)

uuid = form.gen_uuid()
pack_path = (sys.argv[1])[:sys.argv[1].rfind('/')]
#pack_path = '/Users/Shared/Music Production/Ableton/User Library/Sample Packs/Noiiz/80\'s Analog Love'
#if not (form.is_album_exist(conn, pack_path)):
pack_name = form.get_pack_name(pack_path)
#print(pack_path)
#print(pack_name)
description = form.get_description(pack_path)
art_path = form.get_art_path(pack_path)
genre = form.get_genre(pack_path)
provider_name = form.get_provider_name(pack_path)
pack_uuid = 'None'

#if not (form.is_album_exist(conn, pack_path)):
with conn:
    pack = (uuid, pack_name, description, pack_path, art_path, genre, provider_name)
    pack_uuid = squeel.create_pack(conn, pack)
#else:
    #pack_uuid = form.get_uuid(conn, pack_path)
#print(form.is_album_exist(conn, pack_name))
print(pack_uuid)