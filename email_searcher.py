"""Find all email addresses in a text file"""
import re
FILE = input("ENTER TEXT FILE PATH :")
with open(FILE) as myfile:
    CONTENT = myfile.read()
REGEX = re.compile(r'(?:(?:\w*-)*(?:-\w*)*(?:\w*\.)*(?:\.\w*)*(?:\w*\+)*(?:\+\w*)*(?:\w*\")*(?:\"\w*)*)*[\w]+@[\w]+.[\w]+(?:\.\w+)')
MAILLIST = REGEX.findall(CONTENT)
print(MAILLIST)
