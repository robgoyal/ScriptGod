# Name: fileinit.py
# Author: Robin Goyal
# Last-Modified: June 26, 2018
# Purpose: Initialize coding file with a default file structure

import argparse

from datetime import date
from helpers import python_writer, c_writer


SUPPORTED_EXTENSIONS = {"py": python_writer, "c": c_writer}

class CreateFile(object):
    """CreateFile

    Create a file with a structure as specified by the extension.
    """

    def __init__(self, filename, extension, description, author, challenge):
        """

        params:
        """

        # Init variables
        self.filename = filename
        self.extension = extension
        self.description = description
        self.author = author
        self.challenge = challenge
        self.date = date.today().strftime("%B %d, %Y")

        try:
            self.writer_func = SUPPORTED_EXTENSIONS[extension]
        except KeyError:
            raise Exception("Extension {} is not supported".format(extension))


    def create(self):
        """create

        """

        content = self.writer_func(self.filename, self.author, self.date,
                                   self.description, self.challenge)

        with open(self.filename, "w") as f:
            f.write(content)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("filename", help="Name of file to create")
    ap.add_argument("extension", help="Extension of file")
    ap.add_argument("description", help="Description of file")
    ap.add_argument("-a", "--author", default="Robin Goyal", help="Author of file")
    ap.add_argument("-c", "--challenge", help="Name of function to create as part of coding challenge")

    args = vars(ap.parse_args())
    file = CreateFile(**args)
    file.create()