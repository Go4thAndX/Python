# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list are the same, if the numbers are different then return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# Expected Output:

# Given list: [10, 20, 30, 40, 10]

# numbers_x = [10, 20, 30, 40, 10]
# The result is True

# numbers_y = [75, 65, 35, 75, 30]
# The result is False

# Show Solution 

# My solution:

# def first_last_same(given_list_x, given_list_y):
#     # Start function
#     test_list = [10, 20, 30, 40, 10]
#     result_text = "The result is"
#     result_x = True
    
#     if test_list[0] == given_list_x[0] and test_list[-1] == given_list_x[-1]:        
#         result_x
#         print(f"{result_text} {result_x}")
#     else:
#         result_x = False
#         print(f"{result_text} {result_x}")
    
#     result_y = True
    
#     if test_list[0] == given_list_y[0] and test_list[-1] == given_list_y[-1]:
#         result_y
#         print(f"{result_text} {result_y}")
#     else:
#         result_y = False
#         print(f"{result_text} {result_y}")
#     # End function

# given_list_x = [10, 20, 30, 40, 10]
# given_list_y = [75, 65, 35, 75, 30]
# first_last_same(given_list_x, given_list_y)

# Given solution:

# Hier wordt de functie [first_last_same] gedefinieerd met de input parameter [number_list]
def first_last_same(number_list):
    print("Given list:", number_list)
    
    first_num = number_list[0]
    last_num = number_list[-1]
   
    if first_num == last_num:
# Hier wordt de waarde True door de functie als output teruggegeven
        return True
    else:
# Hier wordt de waarde False door de functie als output teruggegeven        
        return False

numbers_x = [10, 20, 30, 40, 10]
# Hier geven we de list met variabele naam [numbers_x] door als argument en ontvangen we de output van de functie terug
print("The result is", first_last_same(numbers_x))
# Hier geven we de list met variabele naam [numbers_y] door als argument en ontvangen we de output van de functie terug
numbers_y = [75, 65, 35, 75, 30]
print("The result is", first_last_same(numbers_y))