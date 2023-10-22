#  Dictionaries

dict = {
    "a": 1,
    "b": "test",
}
print(dict)
# Output:
# {'a': 1, 'b': 'test'}

dict = {
    "a": 1,
    "b": "test",
    "a": 2,
    "b": "Test",
}
print(dict)
# Output:
# {'a': 2, 'b': 'Test'}

a = ""
b = 0
dict = {
    a: 1,
    b: "test",
}
print(dict)
# Output:
# {'': 1, 0: 'test'}

dict = {
    "Land": "Nederland",
    "Provincie": "Zeeland",
    "Stad": "Goes",
}
print(dict)
# Output:
# {'Land': 'Nederland', 'Provincie': 'Zeeland', 'Stad': 'Goes'}

dict = {
    "Land": "Nederland",
    "Provincie": "Zeeland",
    "Stad": "Goes",
}

persoon = {
    "Voornaam": "Jan George",
    "Achternaam": "Koomen",
    "Geboortedatum": "29-03-1961",
    "Leeftijd": 62,
    "Mannelijk": True,
}
print(persoon)

# Output:
# {'Voornaam': 'Jan George', 'Achternaam': 'Koomen', 'Geboortedatum': '29-03-1961', 'Leeftijd': 62, 'Mannelijk': True}

print(persoon["Voornaam"])
# Output:
# Jan George

persoon["Beroep"] = "Stralings deskundige"
print(persoon)
# Output:
# {'Voornaam': 'Jan George', 'Achternaam': 'Koomen', 'Geboortedatum': '29-03-1961', 'Leeftijd': 62, 'Mannelijk': True, 'Beroep': 'Stralings deskundige'}

persoon["Beroep"] = "Geen (vroeg pensioen)"
print(persoon)
# Output:
# {'Voornaam': 'Jan George', 'Achternaam': 'Koomen', 'Geboortedatum': '29-03-1961', 'Leeftijd': 62, 'Mannelijk': True, 'Beroep': 'Geen (vroeg pensioen)'}

# Create a dictionary using {}
persoon = {
    "naam": "Jan George",
    "land": "Nederland",
    "mobiele_nummer": "+31 6 29575554",
}
print(persoon)
# Output:
# {'naam': 'Jan George', 'land': 'Nederland', 'mobiele_nummer': '+31 6 29575554'}

# create a dictionary using dict()
person = dict(
    {
        "name": "Jessa",
        "country": "USA",
        "telephone": 1178,
    }
)
print(person)
# Output
# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# create a dictionary from sequence having each item as a pair
persoon = dict(
    [("naam", "Gerard"), ("land", "Spanje"), ("mobiele_nummer", "+34 722 51 05 35")]
)
print(persoon)
# Output:
# {'naam': 'Gerard', 'land': 'Spanje', 'mobiele_nummer': '+34 722 51 05 35'}

# create dictionary with mixed "key" keys, first key is a string and the second key is an integer
sample_dict = {"name": "Jessa", 10: "Mobile"}
print(sample_dict)
# Output:
# {'name': 'Jessa', 10: 'Mobile'}

# create dictionary with value as a list
persoon = {
    "naam": "Sylvia & Andre",
    "mobiele_nummers": [
        "+1(727)470-3021",
        "+1(727)470-3013",
    ],
}
print(persoon)
# Output:
# {'naam': 'Sylvia & Andre', 'mobiele_nummers': ['+1(727)470-3021', '+1(727)470-3013']}

# When we create a dictionary without any elements inside the curly brackets then it will be an empty dictionary.

emptydict = {}
print(type(emptydict))
# Output:
# class 'dict'

# A dictionary value can be of any type, and duplicates are allowed in that.
# Keys in the dictionary must be unique and of immutable types like string, numbers, or tuples.
# Accessing elements of a dictionary
# There are two different ways to access the elements of a dictionary.
# 1 Retrieve value using the key name inside the square brackets []
# 2 Retrieve value by passing key name as a parameter to the get() method of a dictionary.

# Example:
# create a dictionary named person
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# access value using key name in []
print(person["name"])
# Output
# 'Jessa'

#  get key value using key name in get()
print(person.get("telephone"))
# Output:
# 1178

# Get all keys and values

# Use the following dictionary methods to retrieve all key and values at once

# Method: keys() Description: Returns the list of all keys present in the dictionary.
# Method: values() Description: Returns the list of all values present in the dictionary
# Method: items()	Description: Returns all the items present in the dictionary. Each item will be inside a tuple as a key-value pair.

# We can assign each method’s output to a separate variable and use that for further computations if required.

# Example:

person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Get all keys
print(person.keys())
# Output:
# dict_keys(['name', 'country', 'telephone'])

print(type(person.keys()))
# Output:
# class 'dict_keys'

# Get all values
print(person.values())
# Output:
# dict_values(['Jessa', 'USA', 1178])

print(type(person.values()))
# Output:
# class 'dict_values'

# Get all key-value pair
print(person.items())
# Output:
# dict_items([('name', 'Jessa'), ('country', 'USA'), ('telephone', 1178)])

print(type(person.items()))
# Output:
# class 'dict_items'

# Iterating a dictionary

# We can iterate through a dictionary using a for-loop and access the individual keys and their corresponding values. Let see this with an example.

person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
}

# Iterating the dictionary using for-loop
for key in person:
    print(key, ":", person[key])
# Output:
# name : Jessa
# country : USA
# telephone : 1178

# using items() method
print("key", ":", "value")

for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])
# Output:
# key : value
# name Jessa
# country USA
# telephone 1178

# Find a length of a dictionary

# In order to find the number of items in a dictionary, we can use the len() function. Let us consider the personal details dictionary which we created in the above example and find its length.

person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
}

# count number of keys present in  a dictionary
print(len(person))
# Output:
# 3

# Adding items to the dictionary
# We can add new items to the dictionary using the following two ways.
# Using key-value assignment: Using a simple assignment statement where value can be assigned directly to the new key.
# Using update() Method: In this method, the item passed inside the update() method will be inserted into the dictionary. The item can be another dictionary or any iterable like a tuple of key-value pairs.

# Example:
person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
}

# update dictionary by adding 2 new keys
person["weight"] = 50
person.update({"height": 6})

# print the updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# You can also add more than one key using the update() method.

# Example:
person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
}

# Adding 2 new keys at once
# pass new keys as dict
person.update({"weight": 50, "height": 6})
# print the updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6}

# pass new keys as as list of tuple
person.update(
    [
        ("city", "Texas"),
        (
            "company",
            "Google",
        ),
    ]
)
# print the updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6, 'city': 'Texas', 'company': 'Google'}

# Set default value to a key
# Using the setdefault() method default value can be assigned to a key in the dictionary. In case the key doesn’t exist already, then the key will be inserted into the dictionary, and the value becomes the default value, and None will be inserted if a value is not mentioned. In case the key exists, then it will return the value of a key.

# Example:
person_details = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
}

# set default value if key doesn't exists
person_details.setdefault("state", "Texas")

# key doesn't exists and value not mentioned. Default: None
person_details.setdefault("zip")

# key exists and value mentioned. Doesn't change value
person_details.setdefault("country", "Canada")

# Display dictionary
for key, value in person_details.items():
    print(key, ":", value)
# Output:
# name : Jessa
# country : USA
# telephone : 1178
# state : Texas
# zip : None

# Modify the values of the dictionary keys
# We can modify the values of the existing dictionary keys using the following two ways.
# Using key name: We can directly assign new values by using its key name. The key name will be the existing one and we can mention the new value.
# Using update() method: We can use the update method by passing the key-value pair to change the value. Here the key name will be the existing one, and the value to be updated will be new.

# Example:
person = {
    "name": "Jessa",
    "country": "USA",
}

# updating the country name
person["country"] = "Canada"
# print the updated country
print(person["country"])
# Output:
# 'Canada'

# updating the country name using update() method
person.update({"country": "USA"})
# print the updated country
print(person["country"])
# Output:
# 'USA'

# Removing items from the dictionary
# There are several methods to remove items from the dictionary. Whether we want to remove the single item or the last inserted item or delete the entire dictionary, we can choose the method to be used.
# Use the following dictionary methods to remove keys from a dictionary.
# Method: pop(key[,d]) Description: Return and removes the item with the key and return its value. If the key is not found, it raises KeyError.
# Method: popitem() Description: Return and removes the last inserted item from the dictionary. If the dictionary is empty, it raises KeyError.
# Method: del key	Description: The del keyword will delete the item with the key that is passed
# Method: clear()	Description: Removes all items from the dictionary. Empty the dictionary
# Method: del dict_name Description: Delete the entire dictionary

# Example:
person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178,
    "weight": 50,
    "height": 6,
}

# Remove last inserted item from the dictionary
deleted_item = person.popitem()
print(deleted_item)  # output ('height', 6)
# display updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50}

# Remove key 'telephone' from the dictionary
deleted_item = person.pop("telephone")
print(deleted_item)
# Output:
# 1178

# display updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA', 'weight': 50}

# delete key 'weight'
del person["weight"]
# display updated dictionary
print(person)
# Output:
# {'name': 'Jessa', 'country': 'USA'}

# remove all item (key-values) from dict
person.clear()
# display updated dictionary
print(person)
# Output:
# {}

# Delete the entire dictionary
del person
