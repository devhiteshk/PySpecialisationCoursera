fname = input("Enter file name: ")
fh = open(fname)
S = 0
Count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    #mbox-shortprint(line)
    scan = line.find('0')
    Count = Count + 1
    #print(scan)
    VAL = float(line[scan:])
    #print(VAL)
    S = S + VAL
#print(S)
#print(Count)
print('Average spam confidence: ',(S/Count))


