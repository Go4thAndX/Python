# Tip and Trick 3: Calculate memory is being used by an object in Python

# whenever you use any data structure(such as a list or dictionary or any object) to store values or records.
# It is good practice to check how much memory your data structure uses.

# Use the sys.getsizeof function defined in the sys module to get the memory used by built-in objects. sys.getsizeof(object[, default]) return the size of an object in bytes.

import sys

list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
print("size of list = ",sys.getsizeof(list1))

name = 'pynative.com'
print("size of name = ",sys.getsizeof(name))

# Output:

# ('size of list = ', 112)
# ('size of name = ', 49)

# Note: The sys.getsizeof doesn’t return the correct value for third-party objects or user defines objects.