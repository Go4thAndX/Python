# Exercise 1: Convert two lists into a dictionary

# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# My solution:

dictionary = {}

for key, value in zip(keys, values):
    dictionary[key] = value

print(dictionary)

# Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Given solution 1:
# The zip() function and a dict() constructor

# Use the zip(keys, values) to aggregate two lists.
# Wrap the result of a zip() function into a dict() constructor.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

# Given solution 2:
# Using a loop and update() method of a dictionary

# empty dictionary
# res_dict = dict()
res_dict = {}

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
    
print(res_dict)