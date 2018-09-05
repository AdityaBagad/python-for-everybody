# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
def readStringRev(str):
    length = len(str) - 1
    while length >= 0:
        print(str[length],end="")
        length -= 1

line = input('Enter string: ')
readStringRev(line)
