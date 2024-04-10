"""
Author: Stephen Shea
Date: 01/12/24


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