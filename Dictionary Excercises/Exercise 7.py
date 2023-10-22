# Exercise 7: Check if a value exists in a dictionary

# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present, write a Python program to check if value [200] exists in the following dictionary.

sample_dict = {
    "a": 100,
    "b": 200,
    "c": 300,
}
# Expected output: 200 present in the dict [sample_dict]

# My solution:
check_value = 200
get_values = sample_dict.values()

if check_value in sample_dict.values():
    print(f"{check_value} present in the dict [sample_dict]")
# Output: 200 present in the dict [sample_dict]

# Given solution:
if 200 in sample_dict.values():
    print('200 present in the dict [sample_dict]')
# Output: 200 present in the dict [sample_dict]
