"""Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1166621.txt (There are 69 values and the sum ends with 660)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers."""

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
