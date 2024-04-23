#Search for line tha beign with word 'From'
import re
try:
    with open('test file.txt','r') as fh:
        for line in fh:
            line=line.rstrip()
            if re.search('^From:', line):
            #if line.startswith('From:'):
                print(line)
except FileNotFoundError:
    print(" Error: The file does not exist in the mentioned path")
except Exception as e:
    print(f"There is an error {e} ")