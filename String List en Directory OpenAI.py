# Python biedt een reeks standaardfuncties die gebruikt kunnen worden voor het zoeken, samenvoegen, toevoegen en verwijderen van items in strings, lijsten en dictionaries. Hieronder volgen een aantal voorbeelden:

# String:

# - len() om de lengte van een string te bepalen. 
# - index() om een item in een string te zoeken. 
# - replace() om een item in een string te vervangen. 
# - join() om strings samen te voegen. 
# - split() om een string in delen te splitsen. 

# List:

# - len() om de lengte van een lijst te bepalen. 
# - index() om een item in een lijst te zoeken. 
# - append() om een item aan een lijst toe te voegen. 
# - extend() om meerdere items aan een lijst toe te voegen. 
# - insert() om een item op een specifieke index in een lijst toe te voegen. 
# - remove() om een item uit een lijst te verwijderen. 
# - pop() om een item uit een lijst te verwijderen en op te halen. 
# - sort() om een lijst op alfabetische volgorde te sorteren. 

# Dictionary:

# - len() om de lengte van een dictionary te bepalen. 
# - get() om een item in een dictionary te zoeken. 
# - update() om een item in een dictionary te vervangen. 
# - setdefault() om een item aan een dictionary toe te voegen. 
# - items() om de items in een dictionary op te halen. 
# - popitem() om een item uit een dictionary te verwijderen. 
# - clear() om alle items uit een dictionary te verwijderen.

# Hieronder volgen een aantal voorbeelden:

# String:

# De lengte van de string bepalen
string = "Hello World!"
length = len(string)
print(length)

# Een item in een string zoeken
string = "Hello World!"
index = string.index("W")
print(index)

# Een item in een string vervangen
string = "Hello World!"
new_string = string.replace("World", "Universe")
print(new_string)

# List:

# De lengte van de lijst bepalen
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)

# Een item in een lijst zoeken
my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)

# Een item aan een lijst toevoegen
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# Dictionary:

# De lengte van de dictionary bepalen
my_dict = {
    "name": "John",
    "age": 30
}
length = len(my_dict)
print(length)

# Een item in een dictionary zoeken
my_dict = {
    "name": "John",
    "age": 30
}
name = my_dict.get("name")
print(name)

# Een item in een dictionary vervangen
my_dict = {
    "name": "John",
    "age": 30
}
my_dict.update({"name": "Jack"})
print(my_dict)