# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class, to create a class, use the keyword class:

# Example: Create a class named MyClass, with two properties named x and y:

# class MijnClass:

#     x = 5
#     y = 3

# Create Object, now we can use the class named MyClass to create objects:

# Example: Create an object named p1, and print the value of x and y:

# p1 = MijnClass()
# print(p1.x, p1.y)
# Output:
# 5 3

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Example: Create a class named Person, use the __init__() function to assign values for name and age:

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# Output:
# John
# 36

# The __str__() Function, the __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

# Example: The string representation of an object WITHOUT the __str__() function:

# print(p1)
# Output:
# <__main__.Person object at 0x00000200E4EA3F10>

# Example: The string representation of an object WITH the __str__() function:


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"My name is {self.name} and I'm {self.age} years old."

# p1 = Person("John", 36)

# print(p1)
# Output:
# My name is John and I'm 36 years old.

# Object Methods, objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Example: Insert a function that prints a greeting, and execute it on the p1 object:


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc_name(self):
#         print(f"Hello my name is {self.name}")

#     def myfunc_name_age(self):
#         print(f"Hello my name is {self.name} and my age is {self.age}")


# p1 = Person("John", 36)
# p2 = Person("Andy", 25)
# p1.myfunc_name()
# p2.myfunc_name_age()
# Output:
# Hello my name is John
# Hello my name is Andy and my age is 25

# The self Parameter, the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named "self" , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example: Use the words mysillyobject and abc instead of self:


# class Person:
#     # Use mysillyobject instead of self
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     # Use abc instead of self
#     def myfunc(abc):
#         print(f"Hello my name is {abc.name} and my age is {abc.age}")


# p1 = Person("John", 36)
# p1.myfunc()
# Output:
# Hello my name is John and my age is 36

# Modify Object Properties, you can modify properties on objects like this:

# Example: Set the age of p1 to 40:

# p1.age = 40
# p1.myfunc()
# Output:
# Hello my name is John and my age is 40

# Delete Object Properties, you can delete properties on objects by using the del keyword:

# Example: Delete the age property from the p1 object:

# del p1.age
# p1.myfunc()
# Output:
# AttributeError: 'Person' object has no attribute 'age'

# Delete Objects, you can delete objects by using the del keyword:

# Example: Delete the p1 object:

# del p1
# p1.myfunc()
# Output:
# NameError: name 'p1' is not defined

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# Example:


class Person:
    pass


# Output:
