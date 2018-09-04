"""
# Exercise 1

Run the program on your system and see what numbers you get. 
Run the program more than once and see what numbers you get.
"""
import random
print(random.randint(5, 10))
t = [1, 2, 3]
print(random.choice(t))


"""
# Exercise 2

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

Move the last line of this program to the top, so the function
call appears before the definitions. Run the program and see what error
message you get.
"""
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

"""
Traceback (most recent call last):
  File "Exercise.py", line 30, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
"""

"""
# Exercise 3

Move the function call back to the bottom and move the
definition of print_lyrics after the definition of repeat_lyrics. What
happens when you run this program?
"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

"""
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
"""

"""
# Exercise 4

What is the purpose of the “def” keyword in Python?
a) It is slang that means “the following code is really cool”
b) It indicates the start of a function
c) It indicates that the following indented section of code is to be stored for later
d) b and c are both true
e) None of the above

Answer: (c)
"""

"""
# Exercise 5

What will the following Python program print out?
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()

a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC
e) Zap Zap Zap

Answer: (d)
"""