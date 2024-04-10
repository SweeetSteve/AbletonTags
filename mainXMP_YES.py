"""

"""
import createXMP as c_xmp
import parseXMP as p_xmp
import re

def is_sample_exists(xmp_string, sample_name):
    if (re.search(sample_name, xmp_string)):
        return True
    else:
        return False

def main(sample_path, new_keyword):
    xmp_path = sample_path[:sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    sample_name = sample_path[sample_path.rfind('/') + 1:]
    xmp_string = p_xmp.read_xmp(xmp_path)
    scratch_sample_entry = False

    tag_start = """                        <rdf:li>"""
    tag_end = '</rdf:li>\n'
    xmp_top = ''
    xmp_bottom = ''
    if (xmp_string.find(sample_name) != - 1):
        xmp_top = p_xmp.get_xmp_top(sample_name, xmp_string)
        xmp_string = xmp_string.replace(xmp_top, '')
        sample_entry = xmp_string[:xmp_string.find('</ablFR:keywords>') + 43]
        xmp_bottom = xmp_string.replace(sample_entry, '')
    else:
        scratch_sample_entry = True
        xmp_top = xmp_string[:xmp_string.rfind('</rdf:li>') + 11]
        xmp_bottom = xmp_string.replace(xmp_top, '')


    if not(scratch_sample_entry):
        keywords = p_xmp.get_keywords(sample_entry,new_keyword)
        #print(keywords)
        colors = p_xmp.get_colors(sample_entry)
    else:
        keywords = tag_start + new_keyword + tag_end
    if (scratch_sample_entry):
        new_sample_entry = c_xmp.create_sample_entry_no_color(sample_name, keywords)
    elif not(p_xmp.is_colors_exist(sample_entry)):
        new_sample_entry = c_xmp.create_sample_entry_no_color(sample_name, keywords)
    else:
        new_sample_entry = c_xmp.create_sample_entry_color(sample_name, keywords, colors)

    new_xmp_string = xmp_top + new_sample_entry + xmp_bottom
    if(scratch_sample_entry):
        c_xmp.write_xmp(xmp_path, new_xmp_string)
    elif (sample_entry.find(new_keyword) == -1):
        #print('Needs Tag!')
        #print(new_sample_entry)
        #print(new_xmp_string + '\n')
        c_xmp.write_xmp(xmp_path, new_xmp_string)
    else:
        print('✅')

    #return xmp_top
