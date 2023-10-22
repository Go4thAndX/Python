# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# If the given int is 7536
# 
# Output:
# The reversed order of the integer 7536 with a space separating the digits is : 6 3 5 7 .

# My solution 1:

number_integer = 7536
number_string = str(number_integer)
number_string_reverse = []

for item in range (len(number_string)):
    item = item * -1 + 3
    number_string_reverse.append(number_string[item])
    number_string_reverse.append(" ")

string_reverse = "".join(number_string_reverse)
print(string_reverse)

# Om losse karakters samen te voegen tot een string te maken, gebruik je de .join() methode.

# Input:
# karakters = ["H", "e", "l", "l", "o"]
# tekst = "".join(karakters)
# print(tekst)

# Output:
# Hello

# My solution 2:
    
number_string_reverse = number_string[::-1]
number_string_list =[]

for i in range(len(number_string_reverse)):
    # print(i, number_string_reverse[i])
    number_string_list.append(number_string_reverse[i] + " ")

# print(number_string_list)
string_reverse = "".join(number_string_list)
print(string_reverse)

# My solution 3:

number_string_list =[]
for i in range(len(number_string) - 1, -1, -1):
    # print(i, number_string[i])
    number_string_list.append(number_string[i] + " ")

# print(number_string_list)
string_reverse = "".join(number_string_list)
print(string_reverse)

# Given solution:

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    # 7536 % 10 = 6 omdat 7536 / 10 = 753 is met als rest 6
    # 753 % 10 = 3 omdat 753 / 10 = 75 is met als rest 3
    # 75 % 10 = 5 omdat 75 / 10 = 7 is met als rest 5
    # 7 % 10 = 7 omdat 7 / 10 = 0 is met als rest 7
    digit = number % 10
    # remove the last digit and repeat the loop
    # 7536 // 10 = 753 omdat 753 / 10 = 753,6 is en afgerond naar het dichtstbijzijnde lagere gehele getal 753 is
    # 753 // 10 = 75 omdat 753 / 10 = 75,3 is en afgerond naar het dichtstbijzijnde lagere gehele getal 75 is
    # 75 // 10 = 7 omdat 75 / 10 = 7,5 is en afgerond naar het dichtstbijzijnde lagere gehele getal 7 is
    # 7 // 10 = 0 omdat 7 / 10 = 0,7 is en afgerond naar het dichtstbijzijnde lagere gehele getal 0 is
    number = number // 10
    # digit = 6
    # digit = 3
    # digit = 5
    # digit = 7 
    print(digit, end=" ")