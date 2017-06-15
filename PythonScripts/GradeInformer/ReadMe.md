## Grade Informer

### Purpose

This script enables users to retrieve notifications through text when new grades have come in on McMaster's Mosaic system. The main reason for creating this script was saving the few minutes that it would take to check for grades on the website. 

### Setup

This script requires users to setup an account on Twilio's website required the Account ID and an Authorization Token. It is also required to setup the username and password of Mosaic and the to and from phone numbers in the text message. 

### Procedure

This was my first independent coding project and there were a lot of difficulties to overcome. The first issue was understanding how to use the requests modules to connect to a website. Fortunately, the requests module proved to be very simple with retreiving the data. The next issue was that Mosaic doesn't use separate links for the default homepage and the course grades page. It took a lot of time viewing the page sources to understand where the difference in links came from which was that McMaster used frames for different pages within Mosaic. Once I understood how to connect to the course grades page, the most difficult step was finding how they organized their course names and their course grades. Each row in the table had an id with CRSE_GRADE which I used to retrieve data from using Beautiful Soup. The next step was matching to see if any of the current courses had grade values with the retrieved data. The final step was sending a message using twilio and the message only got sent if any course actually changed. 

### Dependencies

This project requires several files to run this script:

- requests
- getpass
- twilio
- bs4

Use ``` pip install <filename>  ``` to install the required module/dependency. A cronjob can be set to automatically run the file. 