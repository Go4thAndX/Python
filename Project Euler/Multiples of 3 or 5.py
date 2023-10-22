# Problem 1: Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# To find these numbers, we can start by listing all the natural numbers below 10:
# 1, 2, 3, 4, 5, 6, 7, 8, 9
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers_list = []
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers_list.append(i)

sum_numbers = sum(numbers_list)
print(sum_numbers)

# Output:
# 233168