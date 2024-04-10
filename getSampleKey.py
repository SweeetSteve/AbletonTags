"""

"""
import re
import os
import sampleMethods as samp
import addAbletonTag as ab_tag

# TO FILTER FOR SPECIFIC FILES, ENTER THE APPROPRIATE DATA IN THE FOLLOWING LISTS:
extensions = ['aiff'] # e.g.: {"txt", "text", "jpg", "jpeg"}, NOT: {".txt", ".text", ".jpg", ".jpeg"}

# FOLDER TO START SEARCH FROM:
walk_path = "/Users/Shared/Music Production/Ableton/User Library/Sample Packs/Oversampled"



count = 0

#MIDDLE REGEX SEARCH FOR NOIIZ AND Samplephonics
noiiz_regex = '[_\s][ABCDEFG]b*#*m*\d*[\s_]'

#BEGINNING REGEX SEARCH FOR NOIIZ AND SAMPLEPHONICS
#noiiz_regex = '^[ABCDEFG]b*#*m*\d*[_]'

#CYMATICS REGGEX SEARCH
cymatics_search = '[_\s][ABCDEFG]b*#*\sM[ia][nj]'

KSHMR_search = '[_(][ABCDEFG]b*#*m*[\.)]'

oversampled_search= '[-][ABCDEFG]b*#*\w*.'

def file_filter(file_path):
    is_file = False
    for extension in extensions:
        if (re.search(extension + '$', file_path)):
            is_file = True
    return is_file

def tag_key(sample_path, re_pattern):
    sample_name = samp.get_sample_name_from_sample_path(sample_path)
    search = re.search(re_pattern, sample_name)
    if search != None:
        key = search.group().replace('_', '').replace('(','').replace(')', '').replace('-', '').strip()
        key = key.replace('.', '').replace('#', '♯').replace('b', '♭')
        if sample_path.find('Samplephonics') != -1:
            if key.find('m') != -1:
                key = key[:key.find('m')]
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Minor', sample_path)

            elif re.search('\d+', key) != None:
                key = re.sub('\d+', '', key)
                key = 'Key|' + key
                # print(key)
                ab_tag.add_ableton_tag(key, sample_path)
            else:
                key = 'Key|' + key
                # print(key)
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Major', sample_path)
                # print('Key|Major')
                # print(key)
        elif sample_path.find('Cymatics') != -1:
            if key.find('Min') != -1:
                key = key[:key.find('Min')].strip()
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Minor', sample_path)
            elif sample_path.find('Maj') != -1:
                key = key[:key.find('Maj')].strip()
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Major', sample_path)
        elif sample_path.find('KSHMR') != -1:
            if key.find('m') != -1:
                key = key[:key.find('m')]
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Minor', sample_path)
            else:
                key = 'Key|' + key
                # print(key)
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Major', sample_path)
            #print(key)
        elif sample_path.find('Oversampled') != -1:
            if key.find('minor') != -1:
                key = key[:key.find('minor')].strip()
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Minor', sample_path)
            elif sample_path.find('major') != -1:
                key = key[:key.find('major')].strip()
                key = 'Key|' + key
                ab_tag.add_ableton_tag(key, sample_path)
                ab_tag.add_ableton_tag('Key|Major', sample_path)
            else:
                key = 'Key|' + key.strip()
                ab_tag.add_ableton_tag(key, sample_path)



for root, dirs, files in os.walk(walk_path):
    for file in files:
        sample_path = os.path.join(root, file)
        if (file_filter(sample_path)):
            tag_key(sample_path, oversampled_search)
            count += 1





        """    
            sample_name = samp.get_sample_name_from_sample_path(sample_path)
            search = re.search(noiiz_regex, sample_name)
            if search != None:
                key = search.group().replace('_', '').strip()
                key = key.replace('.', '').replace('#', '♯').replace('b', '♭')
                #print(sample_name)
                #print(key + '\n')
                #id3.set_key(sample_path, key)

                if key.find('m') != -1:
                    key = key[:key.find('m')]
                    key = 'Key|' + key
                    ab_tag.add_ableton_tag(key,sample_path)
                    ab_tag.add_ableton_tag('Key|Minor', sample_path)
                    #print(key)
                    #print('Key|Minor')
                    count += 1
                elif re.search('\d+', key) != None:
                    key = re.sub('\d+', '', key)
                    key = 'Key|' + key
                    #print(key)
                    ab_tag.add_ableton_tag(key, sample_path)
                    count += 1
                else:
                    key = 'Key|' + key
                    #print(key)
                    ab_tag.add_ableton_tag(key, sample_path)
                    ab_tag.add_ableton_tag('Key|Major', sample_path)
                    count += 1
                    #print('Key|Major')
                    #print(key)
                #ab_tag.add_ableton_tag()
                #print('Key|' + key)
        """
        print(count)
            #print(count)
