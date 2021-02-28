import json
import urllib.request

counts = list()


web = input('Enter location: ')
print('Retrieving: ', web)
C = urllib.request.urlopen(web)
data = C.read()
print('Retrieved',len(data),'characters')

try: js = json.loads(data)
except: js = None

comments = js['comments']
for comment in comments:
    counts.append(comment['count'])
print('Count', len(comments))
print('Sum', sum(counts))