import re

fname = open(input('File name: ',))
dat = fname.read()

#saving data in memory in variable dat

numbers = re.findall('[0-9]+', dat)
numsum = 0

#Sum loop

for num in numbers:
    num = int(num)
    numsum = numsum+num

print(numsum)
