# Exercise 14:

# Print downward Half-Pyramid Pattern with Star (asterisk)

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# My solution:
    
for i in range (1, 6):
    i = i * -1 + 6
    print("* " * i)
    
# Given solution:

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
    