# this program extracts ip address
#The group() method is a method provided by the re.Match object in Python's re module.
#When you use the re.search() function, it returns a match object if a match is found.
#The group() method is then used to retrieve the actual matched text
'''
\b: This is a word boundary anchor, which ensures that the match occurs at the beginning or end of a word. It helps to avoid matching partial IP addresses within larger words.

(?: ... ): This is a non-capturing group. It groups the enclosed pattern without capturing the matched text. In this case, it groups \d{1,3}\..

\d{1,3}: This matches one to three digits. It's used to match each segment of the IP address, which can range from 0 to 255.

\.: This matches the dot (.) character, which separates the segments in a standard IPv4 address.

{3}: This specifies that the preceding non-capturing group (?:\d{1,3}\.) should be repeated exactly three times, matching the first three segments of the IP address.

\d{1,3}: This matches the fourth segment of the IP address.

\b: Another word boundary anchor, ensuring that the match occurs at the end of a word.
'''

import re
try:
    with open('sip msg.txt', 'r') as fh:
        for line in fh:
            #y = re.findall('[0-9]+:[0-9]+', line)
            y = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if y is not None:
                eip = y.group()
                print(eip)
except FileNotFoundError:
    print("Error: The file does not exist")
except Exception as e:
    print(" There is an error {e} ")
        