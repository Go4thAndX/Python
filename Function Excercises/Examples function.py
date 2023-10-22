# Exercise 0: Defining a function

# Note: While defining a function, we use two keywords, def (mandatory) and return (optional).


def add_function(par_number_1, par_number_2):
    print(f"The first number is : {par_number_1}")
    print(f"The second number is: {par_number_2}")
    addition = par_number_1 + par_number_2

    return addition


number_1 = int(input("Give the first number : "))
number_2 = int(input("Give the second number: "))
print()
result = add_function(par_number_1=number_1, par_number_2=number_2)
print(f"The result of the addition is: {result}")

# def add_function(par_number1, par_number2):
#     par_number1: int = int(input("Give the first number : "))
#     print(f"The first number is : {par_number1}")
#     par_number2: int = int(input("Give the second number: "))
#     print(f"The second number is: {par_number2}")
#     addition = par_number1 + par_number2
#
#     return addition
#
# print()
# par_number1 = 0
# par_number2 = 0
# result = add_function(par_number1=par_number1, par_number2=par_number2)
# print(f"The result of the addition is: {result}")

# def add_function(par_number1: int, par_number2: int) -> int:
#     addition = par_number1 + par_number2
#     return addition
#
#
# par_number1 = int(input("Give the first number: "))
# par_number2 = int(input("Give the second number: "))
# result = add_function(par_number1=par_number1, par_number2=par_number2)
# print(f"The result of the addition is: {result}")

# from typing import List
#
#
# def is_even(par_list: List[int]) -> List[int]:
#     even_nums = []
#     for n in par_list:
#         if n % 2 == 0:
#             even_nums.append(n)
#     return even_nums

# even_nums: List[int] = is_even(par_list=[2, 3, 42, 51, 62, 70, 5, 9])
# print("Even numbers are:", even_nums)

from typing import List


# def arithmetic(par_number1: object, par_number2: object) -> object:
#     add: object = par_number1 + par_number2
#     subtract: object = par_number1 - par_number2
#     multiply: object = par_number1 * par_number2
#     divide: object = par_number1 / par_number2
#     # return four values
#     return add, subtract, multiply, divide
#
#
# # read four return values in four variables
# number1 = 11
# number2 = 3
# result_add, result_subtract, result_multiply, result_division = arithmetic(par_number1=number1, par_number2=number2)
# print(f"Addition {number1} + {number2} = {result_add}")
# print(f"Subtraction {number1} - {number2} = {result_subtract}")
# print(f"Multiplication {number1} * {number2} = {result_multiply}")
# result_division = str(int(result_division))
# print(f"Division {number1} / {number2} = {result_division} broken to the integer")


# def addition(num1, num2):
#     add = num1 + num2
#     # Implementation of addition function in coming release
#     # Pass statement
#     pass
#
#
# calc_add = addition(10, 2)
# print(calc_add)

# Output:
# None

# Local and Global variables
# def function1():
#     # local variable
#     loc_var = 888
#     print("Value is :", loc_var)
#
#
# def function2():
#
#     print("Value is :", loc_var)
#
#
# function1()
# function2()
#
# # Output:
# # Value is : 888
# # print("Value is :", loc_var) # gives error,
# # NameError: name 'loc_var' is not defined
#
# global_var = 999
#
#
# def function1():
#     print("Value in fst function :", global_var)
#
#
# def function2():
#     print("Value in sec function :", global_var)
#
#
# function1()
# function2()

# Output
# Value in fst function : 999
# Value in sec function : 999

# Global variable
# global_var = 5
#
#
# def function1():
#     print("Value in 1st function :", global_var)
#
#
# def function2():
#     # Modify global variable
#     # function will treat it as a local variable
#     global_var = 555
#     print("Value in 2nd function :", global_var)
#
#
# def function3():
#     print("Value in 3rd function :", global_var)
#
#
# function1()
# function2()
# function3()
#
# # Output
# # Value in 1st function : 5
# # Value in 2nd function : 555
# # Value in 3rd function : 5


# # Global variable
# x = 5
#
#
# # defining 1st function
# def function1():
#     print("Value in 1st function :", x)
#
#
# # defining 2nd function
# def function2():
#     # Modify global variable using global keyword
#     global x
#     x = 555
#     print("Value in 2nd function :", x)
#
#
# # defining 3rd function
# def function3():
#     print("Value in 3rd function :", x)
#
#
# function1()
# function2()
# function3()
#
# # Output
# #
# # Value in 1st function : 5
# # Value in 2nd function : 555
# # Value in 3rd function : 555


# def outer_func():
#     x = 777
#
#     def inner_func():
#         # local variable now acts as global variable
#         nonlocal x
#         x = 700
#         print("value of x inside inner function is :", x)
#
#     inner_func()
#     print("value of x inside outer function is :", x)
#
#
# outer_func()
#
# # Output
# # value of x inside inner function is : 700
# # value of x inside outer function is : 700

# Default Arguments

# In a function, arguments can have default values. We assign default values to the argument using the ‘=’
# (assignment) operator at the time of function definition. You can define a function with any number of default arguments.
# The default value of an argument will be used inside a function if we do not pass a value to that argument at the time of the function call.
# Due to this, the default arguments become optional during the function call.
# It overrides the default value if we provide a value to the default arguments during function calls.
# Let us understand this with an example.
# Let’s define a function student() with four arguments name, age, grade, and school. In this function, grade and school are default arguments with default values.
#
# If you call a function without school and grade arguments, then the default values of grade and school are used.
# The age and name parameters do not have default values and are required (mandatory) during a function call.


# function with 2 keyword arguments grade and school
def student(name, age, grade="Five", school="ABC School"):
    print("Student Details:", name, age, grade, school)


# without passing grade and school
# Passing only the mandatory arguments
student("Jon", 12)
# Output:
# Student Details: Jon 12 Five ABC School
