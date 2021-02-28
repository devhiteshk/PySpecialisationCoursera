fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
handle = open(fname)
counts = dict()
lst = list()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])   #since we know that email position is at 1
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)


