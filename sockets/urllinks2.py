from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


def calculateSum(numlist):
    if numlist == []:
        return numlist
    return sum(numlist)

def appendToList(numlist, nums):
    for n in nums:
        n=int(n)
        numlist.append(n)
    return numlist
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numlist = []
for tag in tags:
    # Look at the parts of a tag
    text = tag.get_text()
    if text is not None:
        line = text.rstrip()
        nums = re.findall('[0-9]+',line)
        if nums:
            appendToList(numlist,nums)
sum_list = calculateSum(numlist)
print(sum_list)