"""
Author: Stephen Shea
Date: 01/12/24

Creates an object for an audio sample.
"""


class Sample:
    def __init__(self, sample_path):
        self.sample_path = sample_path
        self.sample_name = self.set_sample_name()
        self.pack_name = self.set_pack_name()
        self.pack_path = self.set_pack_path()
        self.extension = self.set_extention()

    #SET METHODS
    def set_sample_name(self):
        """
            Sets the name of the sample.
        :return: String
        """
        return self.sample_path[self.sample_path.rfind('/') + 1:]

    def set_pack_name(self):
        """
            Sets the name of the associated sample pack.
        :return: String
        """
        pack_name = self.sample_path
        if pack_name.find('/Artists/') != -1:
            pack_name = pack_name.replace('/Users/Shared/Music Production/Ableton/User Library/Sample Packs/Artists/','')
            pack_name = pack_name[pack_name.find('/') + 1:]
            pack_name = pack_name[:pack_name.find('/')]
        else:
            pack_name = pack_name.replace('/Users/Shared/Music Production/Ableton/User Library/Sample Packs/', '')
            pack_name = pack_name[pack_name.find('/') + 1:]
            pack_name = pack_name[:pack_name.find('/')]
        return pack_name

    def set_pack_path(self):
        """
            Sets the POSIX path of the associated sample pack.
        :return: String
        """
        pack_path = self.sample_path[:self.sample_path.find(self.pack_name) + len(self.pack_name)]
        return pack_path

    def set_extention(self):
        """

        :return:
        """
        return self.sample_path[self.sample_path.rfind('.') + 1:]

    #GET METHODS
    def get_sample_path(self):
        return self.sample_path

    def get_sample_name(self):
        return self.sample_name

    def get_pack_name(self):
        return self.pack_name

    def get_pack_path(self):
        return self.pack_path

    def get_extention(self):
        """
            Returns the extention that indicates the type of audio file.
        :return:
        """
        return self.extension