# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')

#input for position and count respectively.

position = int(input("Enter position:")) - 1     #real position in array is 1 less than real
count = int(input("Enter count:"))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

name = list()

# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
   # print(tag.get('href', None))


for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving: ",link)
    name.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)

print(name[-1])       #-1 denotes the end element in an array/list