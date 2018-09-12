'''
Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. 

Then sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''
fname = input('Enter Filename: ')
# fhand = open('mbox-short.txt')
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()

email_dict = dict()
count = 0
for line in fhand:
  line = line.split()
  if len(line) > 3 and line[0] == 'From': 
    from_email = line[1]
    email_dict[from_email] = email_dict.get(from_email,0) + 1

count_list = list()
for count, email in email_dict.items():
    count_list.append((count, email))

count_list.sort(reverse=True)
max_email, max_count = count_list[0]
print(max_email, max_count)
