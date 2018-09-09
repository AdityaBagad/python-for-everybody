'''
Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''
try:
    fhand = open('mbox-short.txt')
except:
    print('File not found')
    exit()

email_count = dict()

for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        mail = line[1]
        email_count[mail] = email_count.get(mail,0) + 1
        
print(email_count)