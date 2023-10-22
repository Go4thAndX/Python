# Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# Expected output: {'city': 'New york', 'age': 25}

# My solution:
for k in keys:
    sample_dict.pop(k)
print(sample_dict)
# Output: {'age': 25, 'city': 'New york'}

# Given solution:
sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)
# Output: {'age': 25, 'city': 'New york'}