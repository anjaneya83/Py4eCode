#Search for lines that contains 'From'

import re

try:
    with open('pm role.txt', 'r') as fh:
    #fh = open('pm role.txt')
        for line in fh:
            line =line.rstrip()                 # remove any trailing whitespaces (including newline characters '\n').
            #if re.search('From',line):
            y=re.findall('\S+?@\S+',line)
            print(y)
    #fh.close()
except FileNotFoundError:
    print("Error: The specified file was not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")