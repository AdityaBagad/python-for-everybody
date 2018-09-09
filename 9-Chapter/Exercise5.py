'''
This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''
def getDomain(mail): 
    return mail[mail.find('@')+1:]

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    exit()

domain_count = dict()

for line in fhand:
    line = line.split()
    if len(line) > 3 and line[0] == 'From':
        domain = getDomain(line[1])
        domain_count[domain] = domain_count.get(domain,0) + 1

print(domain_count)









