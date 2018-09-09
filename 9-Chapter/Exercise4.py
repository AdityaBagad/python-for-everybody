'''
Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''
def getMaximum(email_count):
    max_count = 0
    max_email = ''

    for key in email_count:
        if email_count[key] > max_count or max_count == 0:
            max_count = email_count[key]
            max_email = key

    print(max_email,max_count)

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    exit()

email_count = dict()

for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        mail = line[1]
        email_count[mail] = email_count.get(mail,0) + 1

getMaximum(email_count)