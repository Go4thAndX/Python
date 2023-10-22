# Tip and Trick 11: Convert two lists into a dictionary

# Let say you have two lists, and one list contains keys and the second contains values. Let see how can we convert those two lists into a single dictionary. Using the zip function, we can do this.

item_id = [54, 65, 76]
names = ["Hard Disk", "Laptop", "RAM"]

item_dictionary = dict(zip(item_id, names))

print(item_dictionary)

# Output:

# {54: 'Hard Disk', 65: 'Laptop', 76: 'RAM'}