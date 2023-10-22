# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# My solution:

number1 = 20
number2 = 30
if number1 * number2 <= 1000:
    product = number1 * number2
    print(f"The result is {product}")
else:
    sum = number1 + number2
    print (f"The result is {sum}")

number1 = 40
number2 = 30
if number1 * number2 <= 1000:
    product = number1 * number2
    print(f"The result is {product}")
else:
    sum = number1 + number2
    print (f"The result is {sum}")

# Given solution:

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    sum = num1 + num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return sum

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)