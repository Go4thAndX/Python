# Exercise 3: Return multiple values from a function

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# Given:
# def calculation(a, b):
#
# res = calculation(40, 10)
# print(res)
# Output
# 50, 30

def calculation(a, b):
    sum1 = a + b
    sum2 = a - b
    return sum1, sum2


res = calculation(a=40, b=10)
print(res)