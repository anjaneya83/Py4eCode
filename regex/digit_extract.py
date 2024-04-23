#This program extracts digit patterns from a string
import re

try:
    with open('test file.txt','r') as fh:
        for line in fh:
            y=re.findall('[0-9]+',line)
            if y != []:
                print(y)
            else:
                print("no digit in this line")
except FileNotFoundError:
    print("Error: file does not exists")
except Exception as e:
    print(f"There is an error {e}")