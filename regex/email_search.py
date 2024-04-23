import re

try:
    with open('sip msg.txt', 'r') as fh:
        for line in fh:
            line = line.rstrip()
            # Updated regular expression to handle email addresses with or without angle brackets
            #y = re.search(r'(?<=From: <sip:)?(\S+@\S+\.com)(?:>;| )', line)
            y = re.search(r'(?<=From: <sip:)?(\S+@\S+\.com)', line)
            if y is not None:
                email = y.group(1)  # Extracting the email address from the first capturing group
                print(email)
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(f"There is an error {e}")

            
            