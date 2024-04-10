"""

"""
import sqlMethods as squeel

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #keywords = ['Initiate|🎧']
    #sample_name = '121_A_DeepBass_01_SP.aiff'
    xml_string = """<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 5.6.0">
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
               <rdf:li rdf:parseType="Resource">
                  <ablFR:filePath>121_A_DeepBass_01_SP.aiff</ablFR:filePath>
                  <ablFR:colors>
                     <rdf:Bag>
                        <rdf:li>3</rdf:li>
                        <rdf:li>4</rdf:li>
                     </rdf:Bag>
                  </ablFR:colors>
                  <ablFR:keywords>
                     <rdf:Bag>
                        <rdf:li>Drums|Snare</rdf:li>
                        <rdf:li>Type|Loop</rdf:li>
                        <rdf:li>Type|MPE Preset</rdf:li>
                        <rdf:li>Type|MPE Preset|Basic</rdf:li>
                     </rdf:Bag>
                  </ablFR:keywords>
               </rdf:li>
               <rdf:li rdf:parseType="Resource">
                  <ablFR:filePath>121_A_DeepBass_02_SP.aiff</ablFR:filePath>
                  <ablFR:colors>
                     <rdf:Bag>
                        <rdf:li>3</rdf:li>
                     </rdf:Bag>
                  </ablFR:colors>
                  <ablFR:keywords>
                     <rdf:Bag>
                        <rdf:li>Type|Loop</rdf:li>
                     </rdf:Bag>
                  </ablFR:keywords>
               </rdf:li>
            </rdf:Bag>
         </ablFR:items>
         <xmp:CreatorTool>Updated by Ableton Index 12.0b21</xmp:CreatorTool>
         <xmp:CreateDate>2023-12-12T00:04:52-08:00</xmp:CreateDate>
         <xmp:MetadataDate>2023-12-12T00:12:45-08:00</xmp:MetadataDate>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
"""




    sql_create_samples_table = """CREATE TABLE IF NOT EXISTS samples (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                sample_name TEXT NOT NULL,
                                                sample_path TEXT NOT NULL,
                                                xmp_path TEXT NOY NULL,
                                                Type TEXT,
                                                Sounds TEXT,
                                                Drums TEXT,
                                                Character TEXT,
                                                Devices TEXT,
                                                Genres TEXT,
                                                Key TEXT,
                                                Grooves TEXT,
                                                Tunings TEXT,
                                                Creator TEXT,
                                                '1. Favorites',
                                                'Audio Cortex' TEXT,
                                                Clips TEXT,
                                                'Drum Machines' TEXT,
                                                Foley TEXT,
                                                label TEXT,
                                                pack TEXT,
                                                Plugins TEXT,
                                                Splice TEXT,
                                                places TEXT
                                            );"""

    database = "/Users/Shared/Music Production/Sample Database Files/Ableton Samples.db"

    # create a database connection
    conn = squeel.create_connection(database)

    # create tables
    if conn is not None:
        # create samples table
        squeel.create_table(conn, sql_create_samples_table)
    else:
        print("Error! cannot create the database connection.")
    #print(c_xml.read_xmp('/Users/Shared/Music Production/Ableton/User Library/Sample Packs/1. Noiiz/5 A.M. House/Bass/Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'))

        #print('----------')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
