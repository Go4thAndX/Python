import time
import random


def miller_rabin_primality_test(n, k=10):
    """
    Gebruikt de Miller-Rabin-primatiteitstest om te bepalen of een gegeven
    getal waarschijnlijk een priemgetal is.
    n: het te testen getal
    k: het aantal iteraties van de test (standaard 10)
    retourneert: True als het getal waarschijnlijk een priemgetal is, False als het zeker een samengesteld getal is
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Bepaal r en d zodat n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Voer de test k keer uit
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


starttijd = time.time()

# 600.851.475.143
# 600851475143
end = 600851475143
start = end - 20

priemgetallen = []
for i in range(start, end):  # Let op 1 is per defenitie geen priemgetal
    if miller_rabin_primality_test(i):
        priemgetallen.append(i)

eindtijd = time.time()

# Let op, het bepalen van de priemgetallen kost aan procesortijd ongeveer 1.5 s voor de priemgetallen tussen 0 en 1000 met een k(= aantal iteraties) van 1
print(f"Tijd om priemgetallen te bepalen is: {round(eindtijd - starttijd, 5)} seconden")
print(f"Aantal priemgetallen tussen {start} en {end} is: ", len(priemgetallen))
if len(priemgetallen) == 0:
    print(f"Het grootste priemgetal tussen {start} en {end} is: ", 0)
else:
    print(f"Het grootste priemgetal tussen {start} en {end} is: ", max(priemgetallen))
bestandsnaam = f"Priemgetallen van {start} tot {end} volgens het algoritme van Miller Rabin primality.txt"
# Open het bestand om naar te schrijven
with open(bestandsnaam, "w") as bestand:
    # Schrijf de uitvoer van de print statements naar het bestand
    print("Algoritme van Miller Rabin primality", file=bestand)
    print(
        f"Tijd om priemgetallen te bepalen is: {round(eindtijd-starttijd, 5)} seconden",
        file=bestand,
    )
    print(
        f"Aantal priemgetallen tussen {start} en {end} is: {len(priemgetallen)}",
        file=bestand,
    )
    if len(priemgetallen) == 0:
        print(f"Het grootste priemgetal tussen {start} en {end} is: 0", file=bestand)
    else:
        print(
            f"Het grootste priemgetal tussen {start} en {end} is: {max(priemgetallen)}",
            file=bestand,
        )

# Geef een bevestiging van het opslaan van de uitvoer
print("De uitvoer is opgeslagen in het bestand:", bestandsnaam)
