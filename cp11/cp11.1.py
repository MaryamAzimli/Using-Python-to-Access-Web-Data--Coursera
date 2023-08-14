import re

#fh=open('C:\\SampleData.txt')
fh=open('C:\\ActualData.txt')
lst=list()
for line in fh:
    line=line.rstrip()
    lst+=re.findall('[0-9]+', line)

sum=0
for el in lst:
    sum+=int(el)
print(sum)
