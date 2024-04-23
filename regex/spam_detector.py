#Spam detector detect the line which has this phrase: X_DSPAM-Confidence: 0.435

import re
hand = open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff = re.findall('^X_DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    print(stuff)
    numlist.append(num)
print('Maximum:', max(numlist))