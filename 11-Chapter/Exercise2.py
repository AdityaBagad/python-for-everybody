# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and 
# print out the average.

# Enter file:mbox.txt
# 38444.0323119

# Enter file:mbox-short.txt
# 39756.9259259

import re

handle = open('mbox.txt')

toSearch = 'New Revision: ([0-9]+)'
matchCount = 0
sum = 0

for line in handle:
    line = line.strip()
    number = re.findall(toSearch, line)
    if len(number) > 0:
        sum = int(number[0]) + sum
        matchCount += 1
        
average = sum/matchCount
print(average)
