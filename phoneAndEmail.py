import re
import pyperclip 

# Creates a regex for names

nameRegex = re.compile(r"""
# First Last and optional Middle

(\b[A-Z][a-z]+\b)   # First Name
(\s+[A-Z][a-z]+\b)? # Middle Name (optional)
(\s+[A-Z][a-z]+\b)  # Last Name
""", re.VERBOSE)

# Creates a regex for phone nums

phoneRegex = re.compile(r"""
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
(\d{3}|\(\d{3}\))?               # area code (optional)
(\s|-|\.)?                       # first separator
(\d{3})                          # first 3 digits
(\s|-|\.)                        # separator
(\d{4})                          # last 3 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension word (optional)           
)                                
""", re.VERBOSE)

# Creates a regex for email addresses

emailRegex = re.compile(r"""(
# something.+_@something?.com                        

[a-zA-Z0-9._%+-]+    # name part
@                    # @ symbol
[a-zA-Z0-9._%+-]+    # domain name part                       
#(\.[a-zA-Z]{2,4})    dot something           
)""", re.VERBOSE)

# Gets the text off the clipboard
clipText = str(pyperclip.paste())

# Extracts the email/phone from this text
extractNames = nameRegex.findall(clipText)
extractPhone = phoneRegex.findall(clipText)
extractEmail = emailRegex.findall(clipText)

allNames = [name[0] + " " + name[2] for name in extractNames]
if extractNames[0][1]:
    allNames = [name[0] + " " + name[1] + " " + name[2] for name in extractNames]

allPhoneNumbers = [phoneNumber[0] for phoneNumber in extractPhone]

print(allNames)
print(allPhoneNumbers)
print(extractEmail)

# Copies the extracted email/phone to the clipboard
results = "\n".join(allNames) + "\n" + "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractEmail)
pyperclip.copy(results)

