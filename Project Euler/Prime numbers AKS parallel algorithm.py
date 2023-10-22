import math
import time


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def power_mod(x, y, n):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % n
        y = y // 2
        x = (x * x) % n
    return result


def poly_eval(a, n, x):
    result = 0
    for i in range(len(a)):
        result = (result * x + a[i]) % n
    return result


def inverse_mod(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return None
    if t < 0:
        t = t + n
    return t


def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def aks(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = 1
    while True:
        r += 1
        if power_mod(r, n - 1, n) != 1:
            break
    if r >= math.sqrt(n):
        return False
    m = math.ceil(math.sqrt(phi(n)) * math.log2(n))
    primes = sieve(m)
    for i in range(2, int(math.sqrt(r)) + 1):
        if primes[i]:
            if (n % i == 0) or (power_mod(r, (n - 1) // i, n) == 1):
                return False
    for i in range(1, int(math.sqrt(m)) + 1):
        if primes[i]:
            f = poly_eval([1, -i], n, r)
            gcd_value = gcd(f, n)
            if gcd_value > 1 and gcd_value < n:
                return False
            elif power_mod(r, i, n) != i:
                return False
    return True


def find_primes(start, end):
    primes = []
    max_prime = 0
    start_time = time.time()
    for n in range(start, end + 1):
        if aks(n):
            primes.append(n)
            if n > max_prime:
                max_prime = n
    end_time = time.time()

    print(
        f"Tijd om priemgetallen te bepalen is: {round(end_time - start_time, 5)} seconds"
    )
    print(f"Aantal priemgetallen tussen {start} en : {end} is: {len(primes)}")
    print(f"Het grootste priemgetal tussen {start} en {end} is: {max_prime}")

    bestandsnaam = f"Priemgetallen van {start} tot {end} volgens het algoritme van AKS parallel.txt"
    # Open het bestand om naar te schrijven
    with open(bestandsnaam, "w") as bestand:
        # Schrijf de uitvoer van de print statements naar het bestand
        print(
            f"Tijd om priemgetallen te bepalen is: {round(end_time-start_time, 5)} seconden",
            file=bestand,
        )
        print(
            f"Aantal priemgetallen tussen {start} en {end} is: {len(primes)}",
            file=bestand,
        )
        print(
            f"Het grootste priemgetal tussen {start} en {end} is: {max_prime}",
            file=bestand,
        )

    # Geef een bevestiging van het opslaan van de uitvoer
    print("De uitvoer is opgeslagen in het bestand:", bestandsnaam)

    return primes


# 600851475141 is een priemgetal volgens de Seef van Eratosthenes
# 600851475125 is een priemgetal volgens de Seef van Eratosthenes
# 600851475067 is een priemgetal volgens Miller Rabin primality

# 600.851.475.143

original = 600851475143
start = original - 40
end = start + 10
print(start, end)
find_primes(start, end)
