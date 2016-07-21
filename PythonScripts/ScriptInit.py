#!/usr/local/bin/python

# ScriptInit.py
# Code written by Robin Goyal
# Created on July 7, 2016
# Last Updated on July 7, 2016

# Script is used to create a file and write comments once the file is initialized

# Script accepts two arguments:
# - File name to be created
# - Name of the user accepted as a string in quotation marks

from sys import argv
import subprocess
import datetime

# Try/Except for argument inputs
try:
    script, filename, user_name = argv
    current_time = datetime.datetime.now()

    extension = filename.split(".")[1:]
    subprocess.call(["touch", filename])
    file = open(filename, 'w')

    if extension[0] == "py":
        file.write("#!/usr/bin/env/python\n\n")
        file.write("# Code written by " + user_name + "\n")
        file.write("# Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("# Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n\n")
        description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed. \n> ")

        if not(description == "No" or description == "NO" or description == "no"):
            file.write("# " + description)

    elif extension[0] == "c":
        file = open(filename, 'w')
        file.write("/* Code written by " + user_name + " */\n")
        file.write("/* Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")
        file.write("/* Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n\n")
        description = raw_input("Would you like to provide a description of our project? Enter No if a description is not needed. \n> ")
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("/* " + description + " */")

    elif extension[0] == "cpp" or extension[0] == "c++" or extension[0] == "cp":
        file.write("// Code written by " + user_name + "\n")
        file.write("// Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("// Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n\n")
        description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed. \n> ")
        if not(description == "No" or description == "NO" or description == "no"):
            file.write("// " + description)

    elif extension[0] == "sh":
        file.write("#!/bin/bash\n\n")
        file.write("# Code written by " + user_name + "\n")
        file.write("# Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        file.write("# Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + "\n")
        description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed \n> ")

        if not(description == "No" or description == "NO" or description == "no"):
            file.write("# " + description)

    elif extension[0] == "html":
        file.write("<!-- Code written by " + user_name + " -->\n")
        file.write("<!-- Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " -->\n")
        file.write("<!-- Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " -->\n")
        description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed \n> ")

        if not(description == "No" or description == "NO" or description == "no"):
            file.write("<!-- " + description + " -->")


    elif extension[0] == "css":
        file.write("/* Code written by " + user_name + " */\n")
        file.write("/* Created on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")
        file.write("/* Last updated on " + current_time.strftime("%d-%m-%Y %H:%M").split(' ')[0] + " */\n")
        description = raw_input("Would you like to provide a description of your project? Enter No if a description is not needed \n> ")

        if not(description == "No" or description == "NO" or description == "no"):
            file.write("/* " + description + " */")

    file.close()

except:
        print "Not enough arguments"
