#!user/bin/env/ python

# Purpose: Script to automatically check for recently updated grades from 
#          McMaster Website
# Author: Robin Goyal
# Last Updated: May 2, 2017
# Usage: python gradeinformer.py

# Notes: List of courses should be stored in courses.txt (same directory as
#        script). Script requires macID, password as input and twilio account
#        info and phones numbers must be added to script manually

import requests
import getpass
from twilio.rest import Client
from bs4 import BeautifulSoup

# Get username and password
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

# Twilio account id and authorization setup
accountSid = {"ACCOUNT_SID"}
authToken = {"AUTH_TOKEN"}
client = Client(accountSid, authToken)

# Store payload data
payload = {
        'userid': username,
        'pwd': password
}

# Courses to check grades for
f = open("courses.txt", 'r')
courseList = {}

# Store courses in courseList
for line in f:
    courseRow = line.split(': ')
    courseList[courseRow[0]] = courseRow[1]

f.close()

# List storing any courses for which grades were found
deleteCourses = []

# Initial Message
msg = "You just received marks for: \n"

# Flag to check if course grade has changed
msgFlag = False

# Request session to receive course history page data
with requests.Session() as s:
    
    # Login with payload and login url
    p = s.post('https://epprd.mcmaster.ca/psp/prepprd/?&cmd=login&languageCd=ENG&', data=payload)
    
    # Redirect to course history page
    r = s.get('https://csprd.mcmaster.ca/psc/prcsprd/EMPLOYEE/HRMS_LS/c/SA_LEARNER_SERVICES.SSS_MY_CRSEHIST.GBL?Page=SSS_MY_CRSEHIST&Action=U&TargetFrameName=None')
    
    # Parse data 
    soup = BeautifulSoup(r.text, 'html.parser')
        
# Retrieve course grade from parsed data
for course in courseList.iterkeys():
    courseSoupId = soup.find("span", string = course).get("id")
    dollarIndex = courseSoupId.index('$')

    courseSoupNumber = courseSoupId[dollarIndex:]
    courseGrade = soup.find(id="CRSE_GRADE" + str(courseSoupNumber)).text.replace(u'\xa0', ' ')
    courseGrade = courseGrade.encode('utf-8')

    # Append course info to message if grade was found
    if ' ' in courseGrade:
        continue
    else:
        msgFlag = True
        courseList[course] = courseGrade
        msg += "You got a mark of %s in %s.\n" % (courseGrade, course)
        deleteCourses.append(course)

# Delete courses whose grades are modified
for course in deleteCourses:
    del courseList[course]

# Reopen file and write the courses that don't have grades yet
f = open("courses.txt", 'w')
for course in courseList.iterkeys():
    f.write("%s: %s" % (course, courseList[course]))
f.close()

# Only send message if flag is true (course was found)
if msgFlag:
    message = client.messages.create( 
            body=msg,
            to="",
            from_="")
    print message.sid
