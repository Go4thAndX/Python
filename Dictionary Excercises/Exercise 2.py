# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50

# My solution:

# Volgens deze oplossing is het creeren van een lege dictionary niet noodzakelijk.
# dictionary = {}
dictionary = {**dict1, **dict2} 
print(dictionary) 

# Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Given solution:

dict3 = {**dict1, **dict2}
print(dict3)