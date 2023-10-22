# Exercise 4: Create a function with a default argument

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# See: Default arguments in function
# Given:
# showEmployee("Ben", 12000)
# showEmployee("Jessa")

def show_employee(name, salary=9000):
    print("Name: ", name, "salary: ", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

# Output:
# Name:  Ben salary:  12000
# Name:  Jessa salary:  9000
