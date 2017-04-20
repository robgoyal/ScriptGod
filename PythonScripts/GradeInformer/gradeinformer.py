#!user/bin/env/ python

## Python script to check mcmaster grades for current semester
## Courses are taken from courses.txt file
## Script requires macid and password from command line, twilio sid, auth token and phone numbers

import requests
import getpass
from twilio.rest import Client
from bs4 import BeautifulSoup

# Get username and password
username = raw_input("Username: ")
password = getpass.getpass("Password: ")


# Twilio account id and authorization setup
account_sid = {"ACCOUNT_SID"}
auth_token = {"AUTH_TOKEN"}
client = Client(account_sid, auth_token)

# Store payload data
payload = {
        'userid': username,
        'pwd': password
}

# Courses to check grades for
f = open("courses.txt", 'r')
courseList = {}

for line in f:
    courserow = line.split(': ')
    courseList[courserow[0]] = courserow[1]

f.close()

# Variable to check if any courses should be deleted from courseList
deleteCourses = []

# Initial Message
msg = "You just received marks for: \n"

# Flag to check if course grade has changed
sendmsgflag = False

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

    if ' ' in courseGrade:
        continue
    else:
        sendmsgflag = True
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

# Only send message if flag is true
if sendmsgflag:
    message = client.messages.create( 
            body=msg,
            to="",
            from_="")
    print message.sid
