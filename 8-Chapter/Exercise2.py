# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#   words = line.split()
#   # print 'Debug:', words
#   if len(words) == 0 : continue
#   if words[0] != 'From' : continue
#   print(words[2])
#
# Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

'''
1. For the program to fail we can use IndexError (Refer demo.txt). demo.txt causes the program to fail.

2. The program is heavily safeguarded by the condition:  len(words) < 3. 
The length of the words is 7.
But the data we want is at 2nd index so if the len(word) is less than 3 than we skip the word.
'''

fname = input('Enter Filename: ')
# fhand = open('mbox-short.txt')
fhand = open(fname)
count = 0
for line in fhand:
  words = line.split()
  # print 'Debug:', words
  if len(words) < 3: 
    continue
  if words[0] != 'From' : 
    continue
  print(words[2])
