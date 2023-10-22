# Exercise 1: Create a function in Python

# Write a program to create a function that takes two arguments, name and age, and print their value.

def name_age(par_name: str, par_age: int) -> None:
    print(f"Your name is {name} and your age is {age}")


name = input("What is your name? ")
age = int(input("What is your age? "))
name_age(par_name=name, par_age=age)

