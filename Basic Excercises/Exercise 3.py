# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
#
# Expected Output:
#
# Original String is  pynative
# Printing only even index chars
# p
# n
# t
# v

# My solution:
# My code prints the right output to my knowledge but index 0 isn't an even index number ???

# accept input string from a user
input_string = input("Enter word ")
print("Original string is :", input_string)
# or print(f"Original String is {org_string}")

# Printing only even index chars
num_characters = len(input_string)

for i in range(0, num_characters, 2):
    print(f"Character with index {i} is the {input_string[i]}")

# Given solution 1:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

# Given solution 2:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
