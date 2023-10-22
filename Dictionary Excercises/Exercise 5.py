# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to extract
keys = ["name", "salary"]
# Expected output: {'name': 'Kelly', 'salary': 8000}

# My solution:
# Couldn't find a simple solution

# Given solution 1 with "Dictionary Comprehension":
new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)
# Output: {'name': 'Kelly', 'salary': 8000}

# Given solution 2 with "update() method and a For loop:
new_dict = {}

for k in keys:
    # add current key with its value from sample_dict
    new_dict.update({k: sample_dict[k]})
print(new_dict)
# Output: {'name': 'Kelly', 'salary': 8000}