"""

"""
import os
import re
import parseXMP as parse

def ensure_xmp_path(xmp_path):
    """

    :param xmp_path:
    :return:
    """
    if (os.path.isfile(xmp_path)):
        return 'XMP-YES'
    elif (os.path.isdir(xmp_path[:xmp_path.rfind('Ableton Folder Info')] + '/Ableton Folder Info')):

        return 'XMP-NO'
    else:
        create_ableton_folder(xmp_path[:xmp_path.rfind('Ableton Folder Info')])
        return 'XMP-NO'


def create_xml_string(sample_name):
    """

    :param sample_name:
    :return:
    """
    beginning = """<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 5.6.0">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:ablFR="https://ns.ableton.com/xmp/fs-resources/1.0/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <dc:format>application/vnd.ableton.folder</dc:format>
         <ablFR:resource>folder</ablFR:resource>
         <ablFR:platform>mac</ablFR:platform>
         <ablFR:items>
            <rdf:Bag>
"""

    #Replace '©' char with sample name
    sample_entry = """               <rdf:li rdf:parseType="Resource">
                  <ablFR:filePath>©</ablFR:filePath>
                  <ablFR:colors>
                     <rdf:Bag>
                        <rdf:li>3</rdf:li>
                     </rdf:Bag>
                  </ablFR:colors>
               </rdf:li>
"""

    end = """            </rdf:Bag>
         </ablFR:items>
         <xmp:CreatorTool>Updated by Ableton Index 11.3.10</xmp:CreatorTool>
         <xmp:CreateDate>2023-02-11T23:05:32-08:00</xmp:CreateDate>
         <xmp:MetadataDate>2023-10-04T12:11:48-07:00</xmp:MetadataDate>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
"""

    return beginning + sample_entry.replace('©', sample_name) + end

def create_ableton_folder(path):
    """

    :param path:
    :return:
    """
    folder = 'Ableton Folder Info'
    path = os.path.join(path, folder)
    if (not os.path.isdir(path)):
        os.mkdir(path)

def is_xml_exist(path):
    """

    :param path:
    :return:
    """
    folder = 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'
    path = os.path.join(path, folder)
    if (os.path.isfile(path)):
        return True
    else:
        return False

def create_sample_entry_no_color(sample_name, keywords):
    sample_entry = '               <rdf:li rdf:parseType="Resource">\n' + '                  <ablFR:filePath>ß</ablFR:filePath>\n' + '                  <ablFR:keywords>\n' + '                     <rdf:Bag>\n˚                     </rdf:Bag>\n                  </ablFR:keywords>\n               </rdf:li>\n'
    sample_entry = sample_entry.replace('˚', keywords).replace('ß', sample_name)
    return sample_entry

def create_sample_entry_color(sample_name, keywords, colors):
    sample_entry = '               <rdf:li rdf:parseType="Resource">\n' + '                  <ablFR:filePath>ß</ablFR:filePath>\n                  <ablFR:colors>\n                     <rdf:Bag>\nç                     </rdf:Bag>\n                  </ablFR:colors>\n                  <ablFR:keywords>\n                     <rdf:Bag>\n˚                     </rdf:Bag>\n                  </ablFR:keywords>\n               </rdf:li>\n'
    sample_entry = sample_entry.replace('˚', keywords).replace('ß', sample_name).replace('ç', colors)
    return sample_entry

#def create_new_sample_entry():


def read_xmp(xmp_path):
    f = open(xmp_path, 'r')
    xmp_string = f.read()
    f.close()
    return xmp_string

def write_xmp(xmp_path,xmp_string):
    f = open(xmp_path, 'w')
    f.write(xmp_string)
    f.close()

def create_new_xml_string(xml_string, keywords, sample_name):
    """

    :param xml_string: String
    :param keywords: list
    :param sample_name: String
    :return:
    """
    count = 0

    xml_list = re.split('<rdf:li rdf:parseType="Resource">\n', xml_string)

    for sec in xml_list:
        if (re.search('ablFR:filePath', sec)):
            if (re.search(sample_name, sec)):

                xml_list.pop(count)
                xml_list.insert(count, parse.create_new_sample_entry(sec, keywords, sample_name))


        count = count + 1
    new_xml_string = ''
    count = 0
    # print(xml_list)
    for sec in xml_list:
        if count >= 1:
            new_xml_string = new_xml_string + '<rdf:li rdf:parseType="Resource">\n' + sec
        else:
            new_xml_string = new_xml_string + sec
        count = count + 1
    return new_xml_string

def create_xmp_string_from_scratch(sample_name, keywords):
    sample_entry = '               <rdf:li rdf:parseType="Resource">\n                  <ablFR:filePath>ß</ablFR:filePath>\n                  <ablFR:keywords>\n                     <rdf:Bag>\n˚                     </rdf:Bag>\n                  </ablFR:keywords>\n               </rdf:li>\n'
    entry_start = """<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 5.6.0">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:ablFR="https://ns.ableton.com/xmp/fs-resources/1.0/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <dc:format>application/vnd.ableton.folder</dc:format>
         <ablFR:resource>folder</ablFR:resource>
         <ablFR:platform>mac</ablFR:platform>
         <ablFR:items>
            <rdf:Bag>\n"""
    entry_end = """            </rdf:Bag>
         </ablFR:items>
         <xmp:CreatorTool>Updated by Ableton Index 12.0b21</xmp:CreatorTool>
         <xmp:CreateDate>2023-12-12T00:04:52-08:00</xmp:CreateDate>
         <xmp:MetadataDate>2023-12-12T02:45:05-08:00</xmp:MetadataDate>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>"""
    tag_start = """                        <rdf:li>"""
    tag_end = '</rdf:li>\n'
    keywords = tag_start + keywords + tag_end
    sample_entry = sample_entry.replace('˚', keywords).replace('ß', sample_name)
    new_xmp_string = entry_start + sample_entry + entry_end
    return new_xmp_string