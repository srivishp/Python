# -*- coding: utf-8 -*-
import re
import pyperclip
# Create a regex object for phone numbers
phoneRegex = re.compile(r''' 
# +91 9876543210 +91 98765 43210  020 87654321 020 8765 4321  020-87654321 (020) 8765 4321                       
(
((\+\d{2})|(\d{2,3})|(\(\d{2,3}\)))?         #+91 or 91 or 020 or (020)
(\s|-)#hyphen or space separator
(\d{8,10})|(\d{4,5}\s\d{4,5}) #phone number mobile or landline
)
''', re.VERBOSE)

# Create a regex object for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+] +            #name part
@                           #@symbol
[a-zA-Z0-9_.+]+             #domain name part

''', re.VERBOSE)

# Get text from the clipboard
text = pyperclip.paste()

# Extract phone and email from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

    
print (allPhoneNumbers)
print (extractedEmail)

# Copy the extracted phone and email to the clipboard
results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)
