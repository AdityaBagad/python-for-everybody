# Read the documentation of the string methods at
# https://docs.python.org/3.5/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you
# understand how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. For example,
# in find(sub[, start[, end]]), the brackets indicate optional arguments.
# So sub is required, but start is optional, and if you include start, then
# end is optional.

word = 'Hello World'

# Get Index of the character
print('find(W): ',word.find('W'))

# Get the Index of the character after a specified position
print('find(o,5): ',word.find('o',5))