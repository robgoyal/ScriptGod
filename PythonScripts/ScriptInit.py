#!/usr/local/bin/python

# ScriptInit.py
# Code written by Robin Goyal
# Created on July 7, 2016
# Last Updated on July 21, 2016

# Script is used to create a file and write comments once the file is initialized

# Script accepts two arguments:
# - File name to be created
# - Name of the user accepted as a string in quotation marks

from sys import argv
import subprocess
import datetime

# Function for input of description
# Created to avoid uneccesary overflow of raw input prompt in main code
def descr_input():
    description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed. \n> ")
    return description

# Try/Except for argument inputs
try:
    # Unpacking arguments in variables
    script, filename, user_name = argv

    current_time = datetime.datetime.now()

    # Grab the extension of the file
    extension = filename.split(".")[1:]

    # Call function to create a file
    # *Could have created file from open filename function but I wanted to test the subprocess function
    subprocess.call(["touch", filename])
    file = open(filename, 'w')

# Python file code block
    if extension[0] == "py":

        file.write("#!/usr/bin/env/python\n\n")
        file.write("# Code written by " + user_name + "\n")

        # Split the current time to grab the day-month-year
        file.write("# Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("# Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n\n")

        description = descr_input()
        # Checking variations
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("# " + description)

# C file creation
    elif extension[0] == "c":

        file = open(filename, 'w')
        file.write("/* Code written by " + user_name + " */\n")
        file.write("/* Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")
        file.write("/* Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("/* " + description + " */")

# C++ file creation with multiple extension support
    elif extension[0] == "cpp" or extension[0] == "c++" or extension[0] == "cp":

        file.write("// Code written by " + user_name + "\n")
        file.write("// Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("// Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("// " + description)

# Bash script creation
    elif extension[0] == "sh":

        file.write("#!/bin/bash\n\n")
        file.write("# Code written by " + user_name + "\n")
        file.write("# Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("# Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("# " + description)

# HTML file creation
    elif extension[0] == "html":

        file.write("<!-- Code written by " + user_name + " -->\n")
        file.write("<!-- Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " -->\n")
        file.write("<!-- Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " -->\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("<!-- " + description + " -->")

# CSS file creation
    elif extension[0] == "css":

        file.write("/* Code written by " + user_name + " */\n")
        file.write("/* Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")
        file.write("/* Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("/* " + description + " */")

# Matlab file creation
    elif extension[0] == "m":

        file.write("% {\n")
        file.write("    Code written by " + user_name + "\n")
        file.write("    Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("    Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")

        description = descr_input()
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("    " + description + "\n% }")

# Else clause for all other extensions entered
    else:
        print "Not a valid extension that is supported."
    file.close()

except:
    print "Argument error: Print the correct arguments with a filename and the username which is a string"

