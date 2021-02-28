name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

olist = list()
final = list()
counts = dict()

for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        olist.append(line[5])  #the hour is at 5 position in words.

for item in olist:
    item = item.split(':')
    final.append(item[0])

for hour in final:
    counts[hour] = counts.get(hour,0) + 1

for k, v in sorted(counts.items()):
    print(k,v)