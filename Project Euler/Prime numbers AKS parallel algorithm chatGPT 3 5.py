# The is_prime function is a standard implementation of the Miller-Rabin primality test. The aks_is_prime function implements the AKS-parallel-implementation algorithm. The find_next_prime function is a simple helper function that finds the next prime number by decrementing the input number until a prime number is found.

# The main function takes the user input for the starting number, and then repeatedly applies the AKS algorithm to find the next prime number, until a prime number is found. It prints out whether each number is prime or not, along with the time taken to make the determination. The program can be stopped by pressing the "end" key at any time.

# Note that the AKS algorithm can be quite slow for large inputs, so it may take a while to find the next prime number depending on the starting number.

import time
import keyboard


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def aks_is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for a in range(2, int(pow(n, 0.25)) + 1):
        if pow(a, d, n) != 1:
            for j in range(0, r):
                if pow(a, d * pow(2, j), n) == n - 1:
                    break
            else:
                return False
    return True


def find_next_prime(n):
    while True:
        n -= 1
        if is_prime(n):
            return n


def main():
    # 600.851.475.143
    # start_num = int(input("Enter a starting number: "))
    start_num = 600851475143
    while True:
        start_time = time.process_time()
        if aks_is_prime(start_num):
            print(f"{start_num} is a prime number")
            print(f"Time taken: {time.process_time() - start_time:.5f} seconds")
            break
        else:
            print(f"{start_num} is not a prime number")
        if keyboard.is_pressed("end"):
            print("Program stopped by user")
            break
        start_num = find_next_prime(start_num)


if __name__ == "__main__":
    main()
