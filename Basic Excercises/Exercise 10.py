# Exercise 10: Create a new list from two lists using the following condition

# Create a new list from a two list using the following condition

# Given two lists of numbers, write a program to create a new list in such a way that the new list contains the odd numbers from the first list and the even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:
# result list: [25, 35, 40, 60, 90]


# My solution:

list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]

list_1_odd_2_even = []

for items in list_1:
    
    if (items % 2 != 0):
        list_1_odd_2_even.append(items)
        
for items in list_2:
    
    if (items % 2 == 0):
        list_1_odd_2_even.append(items)
        
print(f"Result list: {list_1_odd_2_even}")

# My solution as a function():

def function_list_1_odd_2_even(list_1, list_2):
    list_1_odd_2_even = []

    for items in list_1:
        
        if (items % 2 != 0):
            list_1_odd_2_even.append(items)
            
    for items in list_2:
        
        if (items % 2 == 0):
            list_1_odd_2_even.append(items)
            
    return list_1_odd_2_even

list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]
print(f"Result list: {function_list_1_odd_2_even(list_1, list_2)}")

# Given solution:

def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))