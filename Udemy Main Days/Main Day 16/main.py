# Object-Oriented Programming
# import another_module
# print(another_module.another_variable)
# Output: 12

# import turtle
# # timmy is een object van de class Turtle als een onderdeel van de turtle module
# timmy = turtle.Turtle()

# # Of op een andere manier, waarbij we van de turtle module, de class Turtle en de class Screen importeren
# from turtle import Turtle, Screen
# # timmy is een object van de class Turtle als een onderdeel van de turtle module
# timmy = Turtle()
# print(timmy)
# # De output is een object
# # Output: <turtle.Turtle object at 0x0000014C334A9A50>
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# # my_screen is een object van de class Screen als een onderdeel van de module turtle
# my_screen = Screen()
# # canvheight is een attribute van het object my_screen
# print(my_screen.canvheight)
# # Output: 300
#
# # exitonclick() is een method van het object my_screen
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# print(table)
# Output:
# ++
# ||
# ++
# ++
# add_column is een method (functie binnen een class) van het object table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# align is een attribute (variabele binnen een class) van het object table
table.align = "l"
print(table)