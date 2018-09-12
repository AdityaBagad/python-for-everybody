'''
This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
fname = input('Enter Filename: ')
# fhand = open('mbox-short.txt')
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()

count_hour = dict()
for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        hours = int(line[-2].split(':')[0])
        count_hour[hours] = count_hour.get(hours,0) + 1

hours_list = list(count_hour.items())
hours_list.sort()
for key, value in hours_list:
    print(key, value)