# Exercise 8: Print the following pattern
# 1
 
# 2 2
 
# 3 3 3
 
# 4 4 4 4
 
# 5 5 5 5 5

# My solution:

# use of range() to define a range of values
values = range(6)
# iterate from i = 0 to i = 3

for i in values:
    i = i * (str(i) + " ")
    print(f"\n {i}")

# Given solution:

for num in range(6):
    for i in range(num):
        #print number  
        print (num, end=" ")
    # new line after each row to display pattern correctly
    print("\n")