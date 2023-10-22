# Python biedt een reeks standaardfuncties die gebruikt kunnen worden voor het invoeren, zoeken, samenvoegen, toevoegen en verwijderen van items in strings, lijsten en dictionaries. Hieronder volgen een aantal voorbeelden:

# Invoeren van items {[key]: [value]} in een dictionary methode 1
naam_1 = "Jan"
bedrag_1 = 123

dict = {naam_1: bedrag_1}
print(dict)

naam_2 = "George"
bedrag_2 = 321

dict[naam_2] = bedrag_2
print(dict)
# Output: {'Jan': 123, 'George': 321}

# Invoeren van items {[key]: [value]} in een dictionary methode 2
dict = {}
meer_invoer = True
while meer_invoer:
    input_name = input("Wat is je naam ?: ")
    input_bedrag = int(input("Wat is je bedrag ?: $"))
    dict[input_name] = input_bedrag
    input_meer = input(
        "Wil je nog meer namen en bedragen invoeren ? Type 'ja' of 'nee': \n"
    )

    if input_meer != "ja":
        meer_invoer = False
print(dict)
# Output: {'Jan': 123, 'George': 321}

# Maak van een [string] een [list] en omgekeerd

# Van een string naar een list, gebruik de functie [.split]
string = "Dit is een test"
list = string.split()
print(list)
# Output: ['Dit', 'is', 'een', 'test']

# Van een list naar een string, gebruik de functie [.join]
list = ["Dit", "is", "een", "test"]
string = " ".join(list)
print(string)
# Output: Dit is een test

# Maak van twee lists een dictionary en omgekeerd ?

# Van twee lists naar een dictionary:
list_dieren = [
    "leeuw",
    "tijger",
    "giraffe",
    "olifant",
    "beren",
    "gibbon",
    "struisvogel",
]
list_continenten = [
    "Afrika",
    "Azië",
    "Afrika",
    "Afrika",
    "Noord-Amerika",
    "Azië",
    "Afrika",
]
dict = dict(zip(list_dieren, list_continenten))
print(dict)
# Output: {'leeuw': 'Afrika', 'tijger': 'Azië', 'giraffe': 'Afrika', 'olifant': 'Afrika', 'beren': 'Noord-Amerika', 'gibbon': 'Azië', 'struisvogel': 'Afrika'}

# Van een dictionary naar twee lists:
dict_dieren = {
    "leeuw": "Afrika",
    "tijger": "Azië",
    "giraffe": "Afrika",
    "olifant": "Afrika",
    "beren": "Noord-Amerika",
    "gibbon": "Azië",
    "struisvogel": "Afrika",
}
list_dieren = list(dict.keys())
list_continenten = list(dict.values())
print(list_dieren, list_continenten)
# Output: ['leeuw', 'tijger', 'giraffe', 'olifant', 'beren', 'gibbon', 'struisvogel'] ['Afrika', 'Azië', 'Afrika', 'Afrika', 'Noord-Amerika', 'Azië', 'Afrika']

# String lengte bepalen
string = "Hello World!"
len_string = len(string)
print(len_string)
# Output: 12

# List lengte bepalen
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)
# Output: 5

# Dictionary lengte bepalen
my_dict = {"name": "John", "age": 30}
length = len(my_dict)
print(length)
# Output: 2

# String item zoeken voorbeeld 1
string = "Hello World!"
index = string.index("W")
print(index)
# Output: 6

# String item zoeken voorbeeld 1
string = "Hello World!"
index = string.index("o")
print(index)
# Output: 4

# List item zoeken
my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)
# Output: 2

# Dictionary key zoeken
my_dict = {"name": "John", "age": 30}
name = my_dict.get("name")
print(name)
# Output: John

# Dictionary value zoeken
my_dict = {"name": "John", "age": 30}
get_values = my_dict.values()

if "John" in my_dict.values():
    print("Value found!")
# Output: Value found

# String item vervangen
string = "Hello World!"
new_string = string.replace("World", "Universe")
print(new_string)
# Output: Hello Universe!

# List item vervangen
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)
# Output: [1, 2, 10, 4, 5]

# Dictionary item vervangen
my_dict = {"name": "John", "age": 30}
my_dict.update({"name": "Jack"})
print(my_dict)
# Output: {'name': 'Jack', 'age': 30}

# Strings samenvoegen manier 1
string_1 = "Hello"
string_2 = " "
string_3 = "World!"
string_samen = string_1 + string_2 + string_3
print(string_samen)
# Output: Hello World!

# Strings samenvoegen manier 2
# De join()-methode wordt gebruikt om een lijst van strings samen te voegen tot één string. Deze methode verwacht een lijst als argument en retourneert een string.
my_list = ["Hello", "World"]
string = "My".join(my_list)
print(string)
# Output: HelloMyWorld!

# Lists samenvoegen
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_samen = []
list_samen.extend(list_1)
list_samen.extend(list_2)
print(list_samen)
# Output: [1, 2, 3, 4, 5, 6]

# Dictionaries samenvoegen
dict_1 = {"name": "John", "age": 30}
dict_2 = {
    "city": "New York",
}
dict_samen = {}
dict_samen.update(dict_1)
dict_samen.update(dict_2)
print(dict_samen)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Een belangrijk punt dat nieuwe Python-programmeurs parten speelt, is dat strings in Python onveranderlijk zijn: Je kunt ze nooit van op hun "huidige" plaats wijzigen. In plaats daarvan moet je jezelf trainen dat wanneer je met strings in Python werkt bedenken, hoe kan ik een "nieuwe string maken" met behulp van de de "oude string" die al bestaat, in plaats van hoe kan ik deze "oude string wijzigen",

# String, een of meerdere karakters toevoegen
string = "Hello World!"
karakters = "My "
# Bepaal de index van het eerste karakter van de string [World!] in de string [string]
index = string.find("World!")
# De nieuwe string bestaat uit het eerste deel van de oude string [string], beginnend bij index [0] en eindigend bij index [index], samengevoegd met de string [karakters] en het laatste deel van de oude string [string] beginnend bij index [index] en eindigend bij het laatste karakter
new_string = string[:index] + karakters + string[index:]
print(new_string)
# Output Hello My World!

# List, een of meerdere items toevoegen op een specifieke index voorbeeld 1
list = [1, 2, 3, 4]
# Voeg 5 toe aan de list [list] op index [1]
list.insert(1, 5)
print(list)
# List, een of meerdere items toevoegen op een specifieke index voorbeeld 2
# Voeg "Aap" toe aan de list [list] op index [3]
list.insert(3, "Aap")
print(list)
# Output:
# [1, 5, 2, 3, 4]
# [1, 5, 2, 'Aap', 3, 4]

# List, het toevoegen van een item aan het einde van een lijst met de append() methode
list = [1, 2, 3]
# Voeg A toe aan list [list]
list.append("A")
print(list)
# Output: [1, 2, 3, "A"]

# Dictionary, een of meerdere items toevoegen
dict = {
    "Naam": "Jan George",
    "Geboorte jaar": 1961,
}
# Stel als key "Geboorteplaats" in met als value "Amsterdam" als de key "Geboorteplaats" niet al bestaat
dict.setdefault("Geboorteplaats", "Amsterdam")
print(dict)
# Output: {'Naam': 'Jan George', 'Geboorte jaar': 1961, 'Geboorteplaats': 'Amsterdam'}

# Dictionary, de fromkeys() methode wordt gebruikt om een nieuwe dictionary te creëren met de opgegeven sleutels en met elke sleutel die een standaard waarde heeft.
# Creëer een nieuwe dictionary met sleutels en waarden, voorbeeld 1:
my_dict = dict.fromkeys(["Naam", "Leeftijd", "Geslacht"], "onbekend")
print(my_dict)
# Output: {'Naam': 'onbekend', 'Leeftijd': 'onbekend', 'Geslacht': 'onbekend'}
# Creëer een nieuwe dictionary met sleutels en waarden, voorbeeld 2:
my_dict = dict.fromkeys(["Tijger", "Gier", "Olifant"], {"Continent": "Afrika"})
print(my_dict)
# Output: {'Tijger': {'Continent': 'Afrika'}, 'Gier': {'Continent': 'Afrika'}, 'Olifant': {'Continent': 'Afrika'}}

# String, een of meerdere karakters verwijderen
string = "Hello My World!"
karakters = "My "
# Bepaal de lengte van de string [karakters]
len_karakters = len(karakters)
# Bepaal de index van het eerste karakter van de string [karakters] in de string [string]
index = string.find(karakters)
# De nieuwe string bestaat uit het eerste deel van de oude string [string], beginnend bij index [0] en eindigend bij index [index], samengevoegd met het laatste deel van de oude string [string] beginnend bij index [index] + het aantal karakters van de string [karakters]
new_string = string[:index] + string[index + len_karakters :]
print(new_string)
# Output Hello World!

# List, een of meerdere items uit een list verwijderen
# Er zijn drie manieren waarop je een item uit een list in Python kunt verwijderen:
# 1. De remove() methode:
list = [1, "Aap", 2, "Noot", 3]
# Verwijder het item [2] uit de list [list]
list.remove(2)
print(list)
# Output: [1, 'Aap', 'Noot', 3]

# 2. Het gebruik van het keyword [del].
list = ["Aap", 1, "Noot", 2, "Mies"]
# Verwijder het item ["Noot"] met index [2]
del list[2]
print(list)
# Output: ['Aap', 1, 2, 'Mies']

# 3. De pop() methode
list = [1, "Aap", 2, "Noot", 3]
# Verwijder het item "Aap" met index [1]uit de list [list]
verwijderd_item = list.pop(1)
print(list)
# Het element dat is verwijderd wordt geretourneerd
print(verwijderd_item)
# Als de index niet wordt opgegeven, wordt het laatste item [-1] van de list [list] verwijderd.
verwijderd_item = list.pop()
print(list)
print(verwijderd_item)
# Output:
# [1, 2, 'Noot', 3]
# Aap
# [1, 2, 'Noot']
# 3

# Dictionary, willekeurig een item uit een dictionary verwijderen
dict = {"name": "John", "age": 30, "city": "New York"}
# Verwijder een willekeurig key-value paar uit de dictionary (het laatste keu_value paar)
verwijderd_item = dict.popitem()
print(dict)
print(verwijderd_item)
# Output:
# {'name': 'John', 'age': 30}
# ('city', 'New York')

dict = {"Aap": 1, "Noot": 3, "Mies": 5, "Teun": 2, "Zus": 4}
verwijderd_item = dict.popitem()
print(dict)
print(verwijderd_item)
# Output:
# {'Aap': 1, 'Noot': 3, 'Mies': 5, 'Teun': 2}
# ('Zus', 4)

# String, splits een string in delen
string = "Hello, My, Pretty, World!"
# De string [string] wordt gesplitst op basis van het scheidingsteken [separator]: komma [","] en het maximum aantal splitsingen [maxsplit] = [2] die door het scheidingsteken gemaakt moeten worden, het resultaat is de list [split_string]
split_string = string.split(",", 2)
print(split_string)
# Output: ['Hello', ' My', ' Pretty, World!']

# List, sorteer een lijst op alfabetische of oplopende volgorde, de list mag geen combinatie zijn van srings en integers
list_string = ["Teun", "Aap", "Zus", "Noot", "Mies"]
# Sorteer de lijst in alfabetische oplopende volgorde:
list_string.sort()
print(list_string)
# Sorteer de lijst in alfabetische aflopende volgorde:
list_string.sort(reverse=True)
print(list_string)

list_integer = [1, 3, 5, 2, 4]
# Sorteer de lijst in oplopende volgorde:
list_integer.sort()
print(list_integer)
# Sorteer de lijst in aflopende volgorde:
list_integer.sort(reverse=True)
print(list_integer)
# Output:
# ['Aap', 'Mies', 'Noot', 'Teun', 'Zus']
# ['Zus', 'Teun', 'Noot', 'Mies', 'Aap']
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]

# Dictionary, sorteren op key en op value
dict_dieren = {
    "leeuw": "Afrika",
    "tijger": "Azië",
    "giraffe": "Afrika",
    "olifant": "Afrika",
    "beren": "Noord-Amerika",
    "gibbon": "Azië",
    "struisvogel": "Afrika",
}
# Sorteren op key:
sorted_dict_key = sorted(dict_dieren.items(), key=lambda x: x[0])
print(sorted_dict_key)
# Output: [('beren', 'Noord-Amerika'), ('gibbon', 'Azië'), ('giraffe', 'Afrika'), ('leeuw', 'Afrika'), ('olifant', 'Afrika'), ('struisvogel', 'Afrika'), ('tijger', 'Azië')]

# Sorteren op value:
sorted_dict_value = sorted(dict_dieren.items(), key=lambda x: x[1])
print(sorted_dict_value)
# Output: [('leeuw', 'Afrika'), ('giraffe', 'Afrika'), ('olifant', 'Afrika'), ('struisvogel', 'Afrika'), ('tijger', 'Azië'), ('gibbon', 'Azië'), ('beren', 'Noord-Amerika')]

# Dictionary, alle items uit een dictionary verwijderen
dict_dieren = {
    "leeuw": "Afrika",
    "tijger": "Azië",
    "giraffe": "Afrika",
    "olifant": "Afrika",
    "beren": "Noord-Amerika",
    "gibbon": "Azië",
    "struisvogel": "Afrika",
}
# Gebruik de clear() methode om alle items uit de dictionary te verwijderen
dict_dieren.clear()
# Controleer of de dictionary leeg is
print(dict_dieren)
# Output: {}
