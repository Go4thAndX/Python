# Exercise 4: Initialize dictionary with default values

# In Python, we can initialize the keys with the same values.

# Input:
employees = ['Kelly', 'Emma']
defaults = {
    "designation": 'Developer',
    "salary": 8000,
}

# Expected output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

# My solution:

empl_def = {}
for i in employees:
    empl_def[i] = {}
    empl_def[i] = {i: defaults}
    empl_def.update(empl_def[i])
print(empl_def)

# Output:{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

# Given solution:

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])