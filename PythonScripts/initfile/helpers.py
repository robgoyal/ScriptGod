# Name: helpers.py
# Author: Robin Goyal
# Last-Modified: June 26, 2018
# Purpose: Helper functions for files


def python_writer(file, author, date, description, challenge):
    """python_writer

    """

    content = "# Name: {}\n# Author: {}\n# Last-Modified: {}\n" \
              "# Purpose: {}".format(file, author, date, description)

    if challenge:
        content += "\n\n\ndef {0}():\n    \"\"\"{0}\n\n    \"\"\"\n\n" \
                   "if __name__ == \"__main__\"\n    main()\n".format(challenge)

    return content

def c_writer():
    pass