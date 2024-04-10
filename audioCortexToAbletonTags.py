"""

"""
import os
import createXMP as c_xmp
import mainXMP_NO as xmp_no
import mainXMP_YES as xmp_yes
from osxmetadata import *
import re

# TO FILTER FOR SPECIFIC FILES, ENTER THE APPROPRIATE DATA IN THE FOLLOWING LISTS:
extensions = ['wav', 'aif', 'aiff'] # e.g.: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}

# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/Music Production/Ableton/User Library/Sample Packs"

audio_cortex_tags = "\'Atmospheres\',\'Bass: Acid\',\'Bass: Acoustic\',\'Bass: Analog\',\'Bass: Club\',\'Bass: Digital\',\'Bass: Electric\',\'Bass: Real\',\'Bass: Sub\',\'Bass: Synthesizer\',\'Brass: Hits\',\'Brass: Horn\',\'Brass: Saxophone\',\'Brass: Section\',\'Brass: Synthesizer\',\'Brass: Trombone\',\'Brass: Trumpet\',\'Brass: Tuba\',\'Keyboards: Clavinet\',\'Keyboards: Harpsichord\',\'Keyboards: Organ\',\'Keyboards: Piano\',\'Keyboards: Piano: Electric\',\'Loop: Bass: Acid\',\'Loop: Bass: Acoustic\',\'Loop: Bass: Analog\',\'Loop: Bass: Atmosphere\',\'Loop: Bass: Electric\',\'Loop: Bass: Heavy\',\'Loop: Bass: Sub\',\'Loop: Bass: Synthesizer\',\'Loop: Brass: Flugel Horn\',\'Loop: Brass: Horn\',\'Loop: Brass: Saxophone\',\'Loop: Brass: Section\',\'Loop: Brass: Synthesizer\',\'Loop: Brass: Trombone\',\'Loop: Brass: Trumpet\',\'Loop: Keyboards: Clavinet\',\'Loop: Keyboards: Organ\',\'Loop: Keyboards: Piano\',\'Loop: Keyboards: Piano: Electric\',\'Loop: Mallets: Bell\',\'Loop: Mallets: Kalimba\',\'Loop: Music\',\'Loop: Music: Raga\',\'Loop: Percussion\',\'Loop: Percussion: Bamboo\',\'Loop: Percussion: Cabasa\',\'Loop: Percussion: Clap\',\'Loop: Percussion: Clave\',\'Loop: Percussion: Cowbell\',\'Loop: Percussion: Crash Cymbal\',\'Loop: Percussion: Cymbal\',\'Loop: Percussion: Drums\',\'Loop: Percussion: Drums: Bhapang\',\'Loop: Percussion: Drums: Bongo\',\'Loop: Percussion: Drums: Cajon\',\'Loop: Percussion: Drums: Chatan\',\'Loop: Percussion: Drums: Clay Pot\',\'Loop: Percussion: Drums: Clicks & Pops\',\'Loop: Percussion: Drums: Conga\',\'Loop: Percussion: Drums: Darbuka\',\'Loop: Percussion: Drums: Dholak\',\'Loop: Percussion: Drums: Djembe\',\'Loop: Percussion: Drums: Dumbek\',\'Loop: Percussion: Drums: Fill\',\'Loop: Percussion: Drums: Ghatam\',\'Loop: Percussion: Drums: Hand\',\'Loop: Percussion: Drums: Kanjira\',\'Loop: Percussion: Drums: Khol\',\'Loop: Percussion: Drums: Kick\',\'Loop: Percussion: Drums: Naqqara\',\'Loop: Percussion: Drums: Rim\',\'Loop: Percussion: Drums: Snare\',\'Loop: Percussion: Drums: Snare: Fill\',\'Loop: Percussion: Drums: Sub\',\'Loop: Percussion: Drums: Tabla\',\'Loop: Percussion: Drums: Timbale\',\'Loop: Percussion: Drums: Toms\',\'Loop: Percussion: Finger Cymbal\',\'Loop: Percussion: Gong\',\'Loop: Percussion: Hi-hat\',\'Loop: Percussion: Hit\',\'Loop: Percussion: Mixed Top\',\'Loop: Percussion: Ride Cymbal\',\'Loop: Percussion: Scraper\',\'Loop: Percussion: Scratches\',\'Loop: Percussion: Shaker\',\'Loop: Percussion: Stick\',\'Loop: Percussion: Tambourine\',\'Loop: Percussion: Wood Block\',\'Loop: Percussion: Zap\',\'Loop: Strings\',\'Loop: Strings: Cello\',\'Loop: Strings: Guitar: Acoustic\',\'Loop: Strings: Guitar: Electric\',\'Loop: Strings: Guitar: Heavy\',\'Loop: Strings: Guitar: Licks\',\'Loop: Strings: Guitar: Synth\',\'Loop: Strings: Harp\',\'Loop: Strings: Kantele\',\'Loop: Strings: Lute\',\'Loop: Strings: Orchestra\',\'Loop: Strings: Oud\',\'Loop: Strings: Pipa\',\'Loop: Strings: Saz\',\'Loop: Strings: Synthesizer\',\'Loop: Strings: Tar\',\'Loop: Strings: Viola\',\'Loop: Strings: Violin\',\'Loop: Strings: Yanchin\',\'Loop: Synthesizer\',\'Loop: Synthesizer: Chords & Stabs\',\'Loop: Synthesizer: Effects\',\'Loop: Synthesizer: Lead\',\'Loop: Synthesizer: Pad\',\'Loop: Synthesizer: Sequence\',\'Loop: Synthesizer: Vocoder\',\'Loop: Synthesizer: Vox\',\'Loop: Synthesizer: Flute\',\'Mallets: Analog\',\'Mallets: Bell\',\'Mallets: Bowl\',\'Mallets: Celesta\',\'Mallets: Gamelan\',\'Mallets: Glass\',\'Mallets: Kalimba\',\'Mallets: Marimba\',\'Mallets: Metal\',\'Mallets: Music Box\',\'Mallets: Synth\',\'Mallets: Synthesizer\',\'Mallets: Vibraphone\',\'Mallets: Xylophone\',\'Music: Raga\',\'Music: Vocals: Female\',\'Music: Vocals: Male\',\'Percussion: Agogo\',\'Percussion: Bell\',\'Percussion: Cabasa\',\'Percussion: Castanet\',\'Percussion: Chimes\',\'Percussion: Clap\',\'Percussion: Clave\',\'Percussion: Clicks & Pops\',\'Percussion: Cowbell\',\'Percussion: Crash Cymbal\',\'Percussion: Cuica\',\'Percussion: Cymbal\',\'Percussion: Drums: Bongo\',\'Percussion: Drums: Cajon\',\'Percussion: Drums: Conga\',\'Percussion: Drums: Darabuka\',\'Percussion: Drums: Dholak\',\'Percussion: Drums: Djembe\',\'Percussion: Drums: Fill\',\'Percussion: Drums: Frame\',\'Percussion: Drums: Hand\',\'Percussion: Drums: Kick\',\'Percussion: Drums: Rim\',\'Percussion: Drums: Snare\',\'Percussion: Drums: Sub\',\'Percussion: Drums: Tabla\',\'Percussion: Drums: Talking\',\'Percussion: Drums: Timbale\',\'Percussion: Drums: Toms\',\'Percussion: Finger Cymbal\',\'Percussion: Gong\',\'Percussion: Guiro\',\'Percussion: Hand Cymbal\',\'Percussion: Hi-hat\',\'Percussion: Hit\',\'Percussion: Human\',\'Percussion: Metal\',\'Percussion: Rainstick\',\'Percussion: Reverse\',\'Percussion: Reverse Cymabl\',\'Percussion: Ride Cymbal\',\'Percussion: Ring Modulation\',\'Percussion: Scratches\',\'Percussion: Shaker\',\'Percussion: Snap\',\'Percussion: Stick\',\'Percussion: Tanbourine\',\'Percussion: Triangle\',\'Percussion: Whistle\',\'Percussion: Wood\',\'Percussion: Wood Block\',\'Percussion: Zap\',\'Sampled: Hit\',\'Sound Effects: Ambience\',\'Sound Effects: Arcade\',\'Sound Effects: Bell\',\'Sound Effects: Breaking\',\'Sound Effects: Bubbling\',\'Sound Effects: Crowd\',\'Sound Effects: Dive\',\'Sound Effects: Echoes\',\'Sound Effects: Filter\',\'Sound Effects: Foley\',\'Sound Effects: Gated\',\'Sound Effects: Heatbeat\',\'Sound Effects: Hit\',\'Sound Effects: Impacts & Crashes\',\'Sound Effects: Loops\',\'Sound Effects: Mechanical\',\'Sound Effects: Metalic\',\'Sound Effects: Nature: Big Cat\',\'Sound Effects: Nature: Bird\',\'Sound Effects: Nature: Dolphin\',\'Sound Effects: Nature: Forest\',\'Sound Effects: Nature: Growl\',\'Sound Effects: Nature: Insect\',\'Sound Effects: Nature: Monkey\',\'Sound Effects: Nature: Synthetic\',\'Sound Effects: Nature: Wolf\',\'Sound Effects: Noise\',\'Sound Effects: Phone\',\'Sound Effects: Reverse\',\'Sound Effects: Rumble\',\'Sound Effects: Sci-Fi\',\'Sound Effects: Sirens & Alarms\',\'Sound Effects: Space\',\'Sound Effects: Steps\',\'Sound Effects: Sweep\',\'Sound Effects: Tape\',\'Sound Effects: Technology\',\'Sound Effects: Thunder\',\'Sound Effects: Tonal\',\'Sound Effects: Transportation\',\'Sound Effects: Water\',\'Sound Effects: Wind\',\'Sound Effects: Zap\',\'Strings: Bandura\',\'Strings: Cello\',\'Strings: Double Bass\',\'Strings: Dulcimer\',\'Strings: Edo\',\'Strings: Guitar: Acoustic\',\'Strings: Guitar: Electric\',\'Strings: Guitar: Heavy\',\'Strings: Guitar: Licks\',\'Strings: Harp\',\'Strings: Kantele\',\'Strings: Lute\',\'Strings: Mandolin\',\'Strings: Orchestra\',\'Strings: Plucked\',\'Strings: Sitar\',\'Strings: Strum\',\'Strings: Tamboura\',\'Strings: Viola\',\'Strings: Violin\',\'Synthesizer: Analog\',\'Synthesizer: Chords & Stabs\',\'Synthesizer: Digital\',\'Synthesizer: hit\',\'Synthesizer: Lead\',\'Synthesizer: Licks\',\'Synthesizer: Pad\',\'Synthesizer: Plucked\',\'Synthesizer: Strings\',\'Synthesizer: Vocoder\',\'Synthesizer: Vox\',\'Unclassified\',\'Vocals: Breath\',\'Vocals: Choir\',\'Vocals: Female\',\'Vocals: Female: Dialogue\',\'Vocals: Female: Phrases\',\'Vocals: Female: Shout\',\'Vocals: Male: Dialogue\',\'Vocals: Male: Phrases\',\'Vocals: Male: Shout\',\'Waveform: PWM\',\'Waveform: Sawtooth\',\'Waveform: Sine\',\'Waveform: Square\',\'Waveform: Sync\',\'Waveform: Triangle\',\'Woodwinds: Bassoon\',\'Woodwinds: Clarinet\',\'Woodwinds: Didgeridoo\',\'Woodwinds: Flute\',\'Woodwinds: Oboe\',\'Woodwinds: Reed\'".split(',')
def file_filter(file_path):
    is_file = False
    for extension in extensions:
        if (re.search(extension + '$', file_path)):
            is_file = True
    return is_file

def add_keywords(xmp_path, sample_path, keyword):
    while (keyword.find('Audio Cortex|') != -1):
        if (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-NO'):
            xmp_no.main(sample_path, keyword)
        elif (c_xmp.ensure_xmp_path(xmp_path) == 'XMP-YES'):
            xmp_yes.main(sample_path, keyword)
        #print(keyword)
        keyword = keyword[:keyword.rfind('|')]

def get_tags(sample_path):
    return OSXMetaData(sample_path).tags

count = 0
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(walk_path):
    for file in files:
        sample_path = os.path.join(root, file)
        if (file_filter(sample_path)):
            count += 1
            print(count)
            tags = str(get_tags(sample_path))
            #print(tags)
            xmp_path = str(root) + '/Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'

            for au_tag in audio_cortex_tags:
                if (tags.find(au_tag) != -1):
                    tag = tags[tags.find(au_tag):]
                    #print(tag)
                    tag = tag[:tag.find(',')]
                    tag = tag.replace('\'', '')
                    tag = tag.replace(': ', '|').strip()
                    new_keyword = 'Audio Cortex|' + tag
                    #print(sample_path)
                    add_keywords(xmp_path, sample_path, new_keyword)
                    #print(new_keyword)
                    break

