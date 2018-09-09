'''
Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).

Sample Line:
    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
    python dow.py
    Enter a file name: mbox-short.txt
    {'Fri': 20, 'Thu': 6, 'Sat': 1}
'''
try:
    fhand = open('mbox-short.txt')
except:
    print('File not found')
    exit()

days_count = dict()

for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        day = line[2]
        days_count[day] = days_count.get(day,0) + 1
        
print(days_count)










