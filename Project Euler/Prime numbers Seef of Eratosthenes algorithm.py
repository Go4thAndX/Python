import time


def sieve_of_eratosthenes(start, end):
    primes = []
    if start < 3:
        primes.append(2)
        start = 3
    if start % 2 == 0:
        start += 1
    sieve_size = (end - start) // 2 + 1
    sieve = [True] * sieve_size
    p = 3
    while p * p <= end:
        index = (p - start % p) % p
        if index == 0 and start <= p:
            index = p * 2
        while index < sieve_size:
            sieve[index] = False
            index += p * 2
        p += 2
    for i in range(sieve_size):
        if sieve[i]:
            primes.append(start + i * 2)
    return primes


# 600.851.475.143
# 600851475043
end = 600851475143
start = end - 20

start_time = time.process_time()
primes = sieve_of_eratosthenes(start, end)
end_time = time.process_time()

num_primes = len(primes)
if num_primes > 0:
    max_prime = max(primes)
else:
    max_prime = None

print(
    f"Tijd om priemgetallen te bepalen is: {round(end_time - start_time, 5)} seconden"
)
print(f"Aantal priemgetallen tussen {start} en {end} is: {num_primes}")
print(f"Het grootste priemgetal tussen {start} en {end} is: {max_prime}")

bestandsnaam = f"Priemgetallen van {start} tot {end} volgens het algoritme van de Seef of Eratosthenes.txt"
# Open het bestand om naar te schrijven
with open(bestandsnaam, "w") as bestand:
    # Schrijf de uitvoer van de print statements naar het bestand
    print("Algoritme van de Seef of Eratosthenes", file=bestand)
    print(
        f"Tijd om priemgetallen te bepalen is: {round(end_time - start_time, 5)} seconden",
        file=bestand,
    )
    print(
        f"Aantal priemgetallen tussen {start} en {end} is: {num_primes}",
        file=bestand,
    )
    print(
        f"Het grootste priemgetal tussen {start} en {end} is: {max_prime}",
        file=bestand,
    )

# Geef een bevestiging van het opslaan van de uitvoer
print("De uitvoer is opgeslagen in het bestand:", bestandsnaam)
