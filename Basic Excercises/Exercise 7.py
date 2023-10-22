# # Exercise 7: Return the count of a given substring from a string

# # Write a program to find how many times substring “Emma” appears in the given string.

# # How to Use find() with No Start and End Parameters Example
# # The following examples illustrate how to use the find() method using the only required parameter – the substring you want to search.
# # You can take a single word and search to find the index number of a specific letter:

# string_1 = "Hello world!"

# # find the index of the letter 'w'
# search_string = string_1.find("w")
# print(search_string)

# # How to Use find() with Start and End Parameters Example
# # Using the start and end parameters with the find() method lets you limit your search.

# # For example, if you wanted to find the index of the letter 'w' and start the search from position 7 and not earlier, you would do the following:

# string_2 = "Hello wild world!"

# # find the index of the letter 'w' starting from position 3
# search_string = string_2.find("w",7)
# print(search_string)

# string_3 = "Hello wild world!"

# # find the index of the letter 'w' between the positions 3 and 8
# search_string = string_3.find("w",3,8)
# print(search_string)

# # As mentioned earlier, if the substring you specify with find() is not present in the string, then the output will be -1 and not an exception.

# # search for the index of the letter 'a' in "Hello world"
# search_string = string_1.find("a")
# print(search_string)

# # Is the find() Method Case-Sensitive?
# # What happens if you search for a letter in a different case?

# # search for the index of the letter 'W' capitalized
# search_string = string_1.find("W")
# print(search_string)
# # So, the search will be case-sensitive.

# # Use the "in" keyword to check if the substring is present in the string in the first place, the "in" keyword returns a Boolean value – a value that is either True or False.
# # The in operator returns True when the substring is present in the string.
# boolean_substring = "w" in "Hello world!"
# print(boolean_substring)

# # If the substring is not present, it returns False:

# boolean_substring = "a" in "Hello world!"
# print(boolean_substring)

# # Using the in keyword is a helpful first step before using the find() method.
# # You first check to see if a string contains a substring, and then you can use find() to find the position of the substring. That way, you know for sure that the substring is present.
# # So, use find() to find the index position of a substring inside a string and not to look if the substring is present in the string.

# # Given:

# # str_x = "Emma is a good developer. Emma is a writer"

# # Expected Output:

# # Emma appeared 2 times

# My solution:

str_x = "Emma is a good developer. Emma is a writer"
int_count = str_x.count("Emma")
print(f"Emma appeared {int_count} times")

# Given solution 1: Use the count() method

str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
cnt = str_x.count("Emma")
print("Emma appeared ", cnt, "times")

#  Given solution 2: Without string method

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")