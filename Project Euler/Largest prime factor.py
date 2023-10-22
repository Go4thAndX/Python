# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# TODO Wat is een prime factor
# TODO Hoe bepaal je de prime factors van een getal
# TODO Bepaal de grootste prime factor van dat getal

# A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. In other words, a prime number is a number that is only divisible by 1 and itself.


# def prime_number(n):
#     new_list = []
#     for i in range(1, n):
#         new_list.append(i)
#     return new_list


# number = 20
# number_until = number + 1
# number_list = prime_number(n=number_until)
# print(number_list)


def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            return is_prime


input_number = 20
# 600851475143
# prime_list = check_prime(number=input_number)
for j in range(2, input_number):
    var = check_prime(number=input_number)
    if var:
        print(var, end=" ")
    else:
        print(not var, end=" ")

# print(prime_list)
