# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero up to n and return a new string.
#
# For example:
#
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.

# My solution:

my_string = input("Type hier een regel tekst: ")
len_string = len(my_string)

# You could use the textwrap module to divide a string into one or more segments. The textwrap.fill() function can be used to wrap a single paragraph of text to a given width, breaking it into one or more segments.

# Example:
#
# import textwrap
#
# input_string = "This is the text string that needs to be divided into segments if it does not fit on the screen."
#
# wrapped_string = textwrap.fill(input_string, width=50)
#
# print(wrapped_string)
#
# Output:
#
# This is the text string that needs
# to be divided into segments if it
# does not fit on the screen.

num_remove = input(f"Geef hier het aantal tekens in waarmee de tekst aan het begin van de tekst moet worden ingekort, dit aantal moet moet minder zijn als de lengte van de tekst die {len_string} tekens lang is: ")
num_remove_int = int(num_remove)
new_string = (my_string[num_remove_int:len_string])
print(f"De tekst die overblijft van de oorspronkelijk tekst is: {new_string}")

def som(num1, num2):
  resultaat = num1 + num2
  return resultaat


# Given solution:

def remove_chars(word, n):
    print("Original string:", word)
    # Deze code betekent dat de variabele x wordt ingesteld op de waarde van het woord beginnend vanaf de n-de positie. Bijvoorbeeld, als de variabele [word] gelijk is aan "Hello" en de variabele [n] gelijk is aan 2, dan zal x gelijk zijn aan "llo".
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
