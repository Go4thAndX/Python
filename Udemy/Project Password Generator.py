# Password Generator

# Instructions:

# The program will ask:
# ```
# How many letters would you like in your password?
# ```
# ```
# How many symbols would you like?
# ```
# ```
# How many numbers would you like?
# ```
# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge. 

#Easy Version (Step 1)

# Generate the password in sequence. If the user wants 
# * 4 letters
# * 2 symbols and
# * 3 numbers

# then the password might look like this: 

# ```
# fgdx$*924
# ```
# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first. 

# Hard Version (Step 2)

# When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
# ```
# x$d24g*f9
# ```
# And every time you generate a password, the positions of the symbols, numbers, and letters are different. 


print("Password Generator Project\n")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

import random

# Om vergissingen te voorkomen in het onderscheid tussen de letter "o" of "O" en het cijfer "0" is het mogelijk verstandig om deze items uit de lijsten te halen.
list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lijst password_letters (leeg)
password_letters = []
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lijst password_numbers (leeg)
password_numbers = []
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# lijst password_symbols (leeg)
password_symbols = []

input_letters = int(input("How many letters would you like in your password?\n")) 
total_letters = len(list_letters)
input_numbers = int(input("How many numbers would you like in your password?\n")) 
total_numbers = len(list_numbers)
input_symbols = int(input("How many symbols would you like in your password?\n")) 
total_symbols = len(list_symbols)

for index in range(input_letters):
# random nummer tussen nul en total_letters 
    random_letters = random.randint(0, total_letters - 1)
# letters toevoegen aan lijst    
    password_letters.append(list_letters[random_letters]) 
#   print(password_letters)
    
# samenvoegen items tot een string
password_string_letters = ("".join(password_letters))
# print(password_string_letters)

for index in range(input_numbers):
# random nummer tussen nul en total_numbers 
    random_numbers = random.randint(0, total_numbers - 1)
# numbers toevoegen aam lijst    
    password_numbers.append(list_numbers[random_numbers]) 
#   print(password_numbers)
    
# samenvoegen items tot een string
password_string_numbers = ("".join(password_numbers))
# print(password_string_numbers)

for index in range(input_symbols):
# random nummer tussen nul en total_symbols 
    random_symbols = random.randint(0, total_symbols - 1)
# numbers toevoegen aam lijst    
    password_symbols.append(list_symbols[random_symbols]) 
#   print(password_symbols)
    
# samenvoegen items tot een string
password_string_symbols = ("".join(password_symbols))
# print(password_string_symbols)

password_part_easy_level = (password_string_letters + password_string_numbers + password_string_symbols)
total_characters = len(password_part_easy_level)
print(total_characters)
print(f"\nThe new generated {total_characters} character password is {password_part_easy_level}")
    
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_password_easy = []

for item in password_string_letters:
    list_password_easy.append(item)

for item in password_string_numbers:
    list_password_easy.append(item)

for item in password_string_symbols:
    list_password_easy.append(item)
# print(list_password_easy)

# Ik ga in dit gedeelte gebruik maken van een random functie die de volgorde van alle items in een list wijzigt 
# The function random.shuffle() shuffles all items in a given list.
# Example

# import random
# 
# list = [1, 2, 3, 4, 5]
# random.shuffle(list)
# print(list)  # [5, 2, 1, 4, 3]

random.shuffle(list_password_easy)
# print(list_password_easy)
# samenvoegen items tot een string
password_part_hard_level = ("".join(list_password_easy))
# print(password_part_hard_level)
print(f"\nThe new generated {total_characters} character \"hard\" password is: {password_part_hard_level}")

# You can use the built-in Python function "extend" to combine two lists into one.
# 
# Example:
# 
# list1 = [1, 2, 3] 
# list2 = [4, 5, 6] 
# list1.extend(list2) 
# 
# print(list1) 
# 
# # Output: [1, 2, 3, 4, 5, 6]

# You can use the built-in Python function "zip" to combine two or more lists into a new list.
# 
# Example:
# 
# list1 = [1, 2, 3] 
# list2 = [4, 5, 6] 
# list3 = [7, 8, 9]
# 
# new_list = list(zip(list1, list2, list3)) 
# 
# print(new_list) 
# 
# # Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#Eazy Level course solution

# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level course solution

# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")