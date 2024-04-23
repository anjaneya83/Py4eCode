import re
'''
it fetches email form a sip msg file
From: <sip:user1@example.com>;tag=987654321
To: <sip:user2@example.com>;tag=123456789
From abce@def.com xyz
'''
try:
    with open('sip msg.txt', 'r') as fh:
        for line in fh:
            line = line.rstrip()
            # Updated regular expression to handle email addresses enclosed in angle brackets
            y = re.search(r'<sip:(\S+@\S+\.com)>', line)
            if y is not None:
                email = y.group(1)  # Extracting the email address from the first capturing group
                print(email)
                #domain =email.split('@')
                domain = re.findall('@([^ ]*)', email)
                # find me an @ sign but dont start with it. so there is a '(' used then [^ ]means not a space character, * means more such characters) 
                print(domain)
            z= re.search(r'\b(\S+@\S+\.com\b)',line)
            if z is not None:
                email=z.group(1)
                print(email)
                domain =email.split('@')
                print(domain[1])        
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(f"There is an error {e}")
