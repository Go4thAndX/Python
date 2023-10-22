# Exercise 13: A nested for Loop

# In Python, the for loop is used to iterate over a sequence such as a list, string, tuple, or other iterable objects such as range.

# Syntax of using a nested for loop in Python

# outer for loop
# for element in sequence 
# inner for loop
#   for element in sequence:
#       body of inner for loop
#   body of outer for loop

# In this example, we are using a for loop inside a for loop. In this example, we are printing a multiplication table of the first ten numbers.

# The outer for loop uses the range() function to iterate over the first ten numbers
# The inner for loop will execute ten times for each outer number
# In the body of the inner loop, we will print the multiplication of the outer number and current number
# The inner loop is nothing but a body of an outer loop.

# Print multiplication table form 1 to 10

# outer loop
for i in range(1, 11):
# nested loop to iterate from 1 to 10
    for j in range(1, 11):
# print multiplication
        print(i * j, end = " ")
    print("\t\t")

# Output:

# 1 2 3 4 5 6 7 8 9 10 
# 2 4 6 8 10 12 14 16 18 20 
# 3 6 9 12 15 18 21 24 27 30 
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100

