"""
Author: Stephen Shea
Date: 01/12/24

This class creates an object for a sample.
Each object contains:
1. The path to the associated xmp file. (The xmp file will be in the same folder as the sample.)
2. A list of tags associated with the sample.
3. The colors associated with the sample.
"""
import sampleClass as Sample
class AbletonTags(Sample):
    def __init__(self,sample_path):
        super().__init__(self, sample_path)
        self.xmp_path = self.set_xmp_path()


    def set_xmp_path(self):
        """
            Returns the POSIX path of the associated XMP file.
        :return: String
        """
        return self.sample_path[:self.sample_path.rfind('/') + 1] + 'Ableton Folder Info/dc66a3fa-0fe1-5352-91cf-3ec237e9ee90.xmp'

    def set_tags(self):
        pass

    def set_colors(self):
        pass