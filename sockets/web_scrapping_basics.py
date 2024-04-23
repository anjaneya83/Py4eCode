#web scrapping basics using Beautiful soup lib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import http.client

try:
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    #creates a BeautifulSoup object named soup by parsing the HTML content of the web page fetched in the previous step.
    #The 'html.parser' argument specifies the parser to be used for parsing the HTML content

    #Retrieve all of the anchor tags

    tags = soup('a')  #returns a list of anchor objects form the web page
    for tag in tags:
        print(tag.get('href', None))  #extracts the href attribute from the anchor tag, if attribute is not found , it returns None
except http.client.IncompleteRead as e:
    print("IncompleteRead error: ",e)
    print("The http response was incomplete.Pls check your network connection")
except Exception as e:
    print("An error occurred: ",e)