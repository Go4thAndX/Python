# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# Expected Output:
#
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

# My solution:

print("Printing current and previous number sum in a range(10)")
previous_number = 0
current_number = 0
# sum_number = current_number + previous_number
# print(f"Current Number {current_number} previous Number  {previous_number}  Sum:  {sum_number}")
for i in range(10):
    sum_number = current_number + previous_number
    print(f"Current Number {current_number} previous Number  {previous_number}  Sum:  {sum_number}")
    previous_number = current_number
    current_number += 1
print("\n")

# Given solution:
# The output from the given solution is wrong !!!

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i
