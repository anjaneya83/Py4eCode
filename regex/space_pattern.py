# identify a patter X-{any number of characters without space}:  in a file
# ^ denotes starting character should match or starts with
#\S means any non space character
#+ one or more times
import re
try:
    with open('random header.txt', 'r') as fh:
        for line in fh:
            y = re.findall('^X-\S+:', line)
            if y!= []:
                print(line)
            else:
                print("na")
except FileNotFoundError:
    print("Error: this file does not exist")
except Exception as e:
    print(f"There is an error: {e}")