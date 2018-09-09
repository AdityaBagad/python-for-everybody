# Download a copy of the file fromwww.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.
try:
    fhand = open('words.txt')
except:
    print('File not Found')
    exit()

wordmap = dict()
for line in fhand:
    line = line.split()
    for word in line:
        if word not in wordmap:
            wordmap[word] = 'value'

print(wordmap)

