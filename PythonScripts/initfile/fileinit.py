# Name: fileinit.py
# Author: Robin Goyal
# Last-Modified: June 25, 2018
# Purpose: Initialize coding file with a default file structure

import datetime
import argparse


class CreateFile(object):
    """CreateFile

    Create a file with a structure as specified by the extension.
    """

    pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="Naame of file to create")
    ap.add_argument("-e", "--extension", required=True, help="Extension of file to create")

    args = vars(ap.parse_args())

    CreateFile(args)