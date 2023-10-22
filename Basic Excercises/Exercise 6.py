# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

# My solution:

list_numbers = [10, 20, 33, 46, 55]
len_list_numbers = len(list_numbers)
print(f"Given list is {list_numbers}\nDivisible by 5")

for i in range(0, len_list_numbers):
    
    if list_numbers[i] % 5 == 0:
        print(list_numbers[i])
        
# Given solution:

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print("Divisible by 5: ")

for num in num_list:
    
    if num % 5 == 0:
        print(num)