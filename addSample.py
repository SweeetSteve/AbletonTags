"""
Author: Stephen Shea
Date: 12/08/23

Adds a sample data entry to the Ableton Samples Database
"""

import Methods.createXMP as c_xmp
import Methods.mainXMP_NO as xmp_no
import re
import Methods.sqlMethods as squeel
import Methods.sampleMethods as samp

database = "/Users/Shared/Music Production/Sample Database Files/Ableton Samples.db"
conn = squeel.create_connection(database)


def add_sample(conn, sample_path):

        #sample_path = '/Users/Shared/Music Production/Ableton/User Library/Sample Packs/Noiiz/\'80s DX Kit/Loops/125_DXDrums_01_818.aiff'
        sample_name = samp.get_sample_name_from_sample_path(sample_path)
        xmp_path = samp.get_xmp_path_from_sample_path(sample_path)
        type = ''
        sounds = ''
        drums = ''
        devices = ''
        genres = ''
        key = ''
        grooves = ''
        tunings = ''
        creators = ''
        favorites = ''
        audio_cortex = ''
        clips = ''
        drum_machines = ''
        foley = ''
        label = ''
        pack = 'None '
        plugins = ''
        splice = ''
        places = 'None '
        if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
                xmp_no.main(sample_path, '1. Favorites|Delete Me')
        tags = samp.get_ableton_tags(sample_path)
        tags = tags[0]
        #colors = samp.get_ableton_tags()[1]
        for tag in tags:
                if (re.search('^Type[|]', tag)):
                        type = type + tag + ','
                elif(re.search('^Sounds[|]', tag)):
                        sounds = sounds + tag + ','
                elif(re.search('^Drums[|]', tag)):
                        drums = drums + tag + ','
                elif (re.search('^Devices[|]', tag)):
                        devices = devices + tag + ','
                elif (re.search('^Genres[|]', tag)):
                        genres = genres + tag + ','
                elif (re.search('^Key[|]', tag)):
                        key = key + tag + ','
                elif (re.search('^Grooves[|]', tag)):
                        grooves = grooves + tag + ','
                elif (re.search('^Tunings[|]', tag)):
                        tunings = tunings + tag + ','
                elif (re.search('^Creator[|]', tag)):
                        creators = creators + tag + ','
                elif (re.search('^1[.]\sFavorites[|]', tag)):
                        favorites = favorites + tag + ','
                elif (re.search('^Audio\sCortex[|]', tag)):
                        audio_cortex = audio_cortex + tag + ','
                elif (re.search('^Clips[|]', tag)):
                        clips = clips + tag + ','
                elif (re.search('^Drum\sMachines[|]', tag)):
                        drum_machines = drum_machines + tag + ','
                elif (re.search('^Foley[|]', tag)):
                        foley = foley + tag + ','
                elif (re.search('^Label[|]', tag)):
                        label = label + tag + ','
                elif (re.search('^Pack[|]', tag)):
                        pack = pack + tag + ','
                        pack = pack.replace('None ', '')
                elif (re.search('^Plugins[|]', tag)):
                        plugins = plugins + tag + ','
                elif (re.search('^Splice[|]', tag)):
                        splice = splice + tag + ','
                elif (re.search('^Places[|]', tag)):
                        places = places + tag + ','
                        places = places.replace('None ', '')
        with conn:
            sample = (sample_name,
                    sample_path,
                    xmp_path,
                    type[:len(type) - 1],
                    sounds[:len(sounds) - 1],
                    drums[:len(drums) - 1],
                    devices[:len(devices) - 1],
                    genres[:len(genres) - 1],
                    key[:len(key) - 1],
                    grooves[:len(grooves) - 1],
                    tunings[:len(tunings) - 1],
                    creators[:len(creators) - 1],
                    favorites[:len(favorites) - 1],
                    audio_cortex[:len(audio_cortex) - 1],
                    clips[:len(clips) - 1],
                    drum_machines[:len(drum_machines) - 1],
                    foley[:len(foley) - 1],
                    label[:len(label) - 1],
                    pack[:len(pack) - 1],
                    plugins[:len(plugins) - 1],
                    splice[:len(splice) - 1],
                    places[:len(places) - 1])
            squeel.create_sample(conn, sample)