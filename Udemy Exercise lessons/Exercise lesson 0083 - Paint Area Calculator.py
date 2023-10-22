# Instructions:

# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5 = 1.6

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# Define a function called paint_calc() so that the code below works.   

# IMPORTANT: Notice the name of the function and parameters must match those given in this code to work:
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Example Input
# test_h = 3
# test_w = 9

# Example Output
# You'll need 6 cans of paint.

# example of the rounding function in Python code.

# Round the number 5.45 to the nearest whole number
# rounded_number = round(5.45)
# print(rounded_number)
# # Output: 5

# Eerst dient men de 'math' module te importeren
# import math 
  
# Om het getal naar beneden af te ronden:
# math.floor(x)
# Dit geeft een rond getal terug dat niet kleiner is dan x

# Om het getal naar boven af te ronden:
# math.ceil(x)
# Dit geeft een getal terug dat niet groter is dan x

import math

def paint_calc(height, width, cover):
    # Exercise solution:
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You\'ll need {num_of_cans} cans of paint")

    # My solution:
    # num_of_cans = math.ceil(((height * width) / cover))
   

test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
