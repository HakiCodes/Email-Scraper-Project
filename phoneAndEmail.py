import re
import pyperclip 

# Created a regex for phone nums

phoneRegex = re.compile(r"""
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(\d{3}|\(\d{3}\))?               # area code (optional)
(\s|-|\.)?                       # first separator
(\d{3})                          # first 3 digits
(\s|-|\.)                        # separator
(\d{4})                          # last 3 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension word (optional)           
                                
""", re.VERBOSE)

print(phoneRegex.search("my number is 985-555-3468, what's yours?"))
#TODO: create a regex for email addresses



#TODO: Get the text off the clipboard



#TODO: Extract the email/phone from this text




#TODO: Copy the extracted email/phone to the clipboard

