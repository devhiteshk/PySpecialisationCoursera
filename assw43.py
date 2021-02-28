from urllib import request
import xml.etree.ElementTree as ET

url = input("Enter Location: ", )

print ("Retrieving: ", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved: ",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
Count=len(results)
SUM=0

for result in results:
    SUM = SUM + float(result.find('count').text)
print(Count)
print(SUM)