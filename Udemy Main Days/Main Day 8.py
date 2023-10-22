# Simple Function

# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello World!")
#     print("My name is Jan George Koomen")
#     print("And this is day 8 of the course 100 Days of code")

# greet()

# Function that allows for input

# We definieren hier de Functie: [greet_with_name] met de Parameter: [name]
# def greet_with_name(name):
#     print("Hello World!")
#     print(f"My name is {name}")
#     print("And this is day 8 of the course \"100 Days of code\"")

# Het Argument: ["Jan George Koomen"] is de data die we doorgeven aan de Parameter: [name] van de Functie: [greet_with_name]
# greet_with_name("Jan George Koomen")

# Functions with more than 1 input: Positional Arguments

def greet_with(name, number):
    print("Hello World!")
    print(f"My name is {name}")
    print(f"And this is day {number} of the course \"100 Days of code\"")

greet_with("Jan George Koomen", 8)

# En wat gebeurd er als ik deze twee Argumenten omwissel ?

greet_with(8, "Jan George Koomen")

# Functions with keyword arguments

greet_with(name = "Jan George Koomen", number = 8)

# En wat gebeurd er nu als ik deze twee Keyword Argumenten omwissel ?

greet_with(number = 8, name = "Jan George Koomen")

