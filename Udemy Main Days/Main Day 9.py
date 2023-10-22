# Een dictionary in Python is een verzameling van key-value paren. De dictionary is een variabele en de inhoud van de dictionary wordt omgeven door accolades [{}] Meerdere key-value paren worden van elkaar gescheiden door comma's [,]. Een key is een unieke identificatie die aan een waarde gekoppeld is. De waarde kan van elk type zijn. Dictionaries worden gebruikt om data op te slaan en te organiseren. Een voorbeeld is:

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing someting over and over again",
}

# # Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# # Adding new items to a dictionary
# programming_dictionary["Dictionary"] = "The collection of key-value pares"
# print(programming_dictionary)

# # Create an empty dictionary
# empty_value = ""
# empty_list = []
# empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# # Loop through a dictionary
# for key_value in programming_dictionary:
#     print(key_value)
    
# Maar als we deze loop uitvoeren dan krijgen we alleen de key's als output dus om de zowel de sleutel [key] als de waarde [value] als output te krijgen moeten we de loop voor een dictionary wijzigen in:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
# Nesting a list or a dictionary in a dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

["A", "B",["c", "D"]]

# Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 14},
}

travel_log = {
    "France": {
        "cities_visited":
            ["Paris", "Lille", "Dijon"],
        "total_visits": 12},
    "Germany": {
        "cities_visited": 
            ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5},
}

# Nesting a dictionary in a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
    },    
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5
    },
]