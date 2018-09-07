# Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(mylist1):
    del mylist1[0]
    del mylist1[-1]
    return None

def middle(mylist2):
    return mylist2[1:len(mylist2)-1]

input_list1 = list(input('Enter List1: '))
chop(input_list1)
print('chop(): ',input_list1)

input_list2 = list(input('Enter List2: '))
new_list = middle(input_list2)
print('middle(): ',new_list)
