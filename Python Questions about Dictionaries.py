'''
# Write a line of code will change the starting_dictionary to the final_dictionary?

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }

# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)

# Output:
# {'a': 9, 'b': 8, 'c': 7}


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# dict["c"] = [1, 2, 3]
# print(dict)

# # Output:
# {'a': 1, 'b': 2, 'c': [1, 2, 3]}

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] += 1
print(dict)

# Output:
# {'a': 2, 'b': 3, 'c': 4}

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
    
dict[1] = 4
print(dict)

# Output:
# {'a': 1, 'b': 2, 'c': 3, 1: 4}

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
    
print(dict[1])

# Output:
# KeyError: 1

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

# print(order["main"][2])

# Output:
# ["Steak"]

# print(order["dessert" - 1][2][0])

# Output:
# TypeError: unsupported operand type(s) for -: 'str' and 'int'

# print(order[main][2][0])

# Output:
# NameError: name 'main' is not defined.

# print(order["main"][2][0])

# Output:
# Steak

print(order["main"][1][0])

# Output:
# Burger
'''