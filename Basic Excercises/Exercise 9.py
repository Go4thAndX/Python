# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example 545, is a palindrome

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

# My solution:

test_number_string = (input("Type in number 121 to check if it is a palindrome "))
if test_number_string[0] == test_number_string[2]:
    print(f"original number {test_number_string}")
    print("Yes. given number is a palindrome")
else:
    print(f"original number {test_number_string}")
    print("No. given number is not a palindrome")

test_number_string = (input("Type in number 125 to check if it is a palindrome "))
if test_number_string[0] == test_number_string[2]:
    print(f"original number {test_number_string}")
    print("Yes, given number is a palindrome")
else:
    print(f"original number {test_number_string}")
    print("No, given number is not a palindrome")
    
# Given solution:

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

palindrome(121)
palindrome(125)