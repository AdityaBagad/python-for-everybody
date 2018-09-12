'''
Write a program that reads a file and prints the letters in decreasing order of frequency. 

Your program should convert all the input to lower case and only count the letters a-z. 

Your program should not count spaces, digits, punctuation, or anything 
other than the letters a-z. 

Find text samples from several different languages and see how letter 
frequency varies between languages. 

Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
import string
# fname = input('Enter Filename: ')
# fhand = open('mbox-short.txt')
try:
    fhand = open('romeo.txt')
except:
    print('File not found')
    quit()

count_letter = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.lower().split()
    for word in line:
        for letter in word:
            count_letter[letter] = count_letter.get(letter, 0) + 1

letter_list = list(count_letter.items())
letter_list.sort()
for letter, count in letter_list:
    print(letter, count)