#!/usr/bin/env/python

# ScriptInit.py
# Code written by Robin Goyal
# Created on July 7, 2016
# Last Updated on July 7, 2016

# Script is used to create a file and write comments once the file is initialized

# Script accepts two arguments:
# - File name to be created
# - Name of the user

from sys import argv
import subprocess
import datetime

try:
    script, filename, user_name = argv
    current_time = datetime.datetime.now()

    extension = filename.split(".")[1:]

    if extension[0] == "py":
        subprocess.call(["touch", filename])

        file = open(filename, 'w')
        file.write("#!/usr/bin/env/python\n\n")
        file.write("# Code written by " + user_name + "\n")
        file.write("# Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("# Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n\n")
        description = raw_input("Would you like to provide a description of your project? Press RETURN if no description is needed. \n> ")
        file.write("# " + description)
        file.close()

    elif extension[0] == "c":
        subprocess.call(["touch", filename])

        file = open(filename, 'w')
        file.write("/* Code written by " + user_name + "*/\n")
        file.write("/* Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "*/\n")
        file.write("/* Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "*/\n\n")
        description = raw_input("Would you like to provide a description of our project? Press RETURN if no description is needed. \n> ")
        file.write("/* " + description + " */")

except:
        print "Not enough arguments"

