# Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 2520 is het kleinste getal dat door elk van de getallen van 1 tot 10 gedeeld kan worden zonder rest.

# Dit betekent dat 2520 een gemeenschappelijk veelvoud is van de getallen van 1 tot 10. Dit komt omdat 2520 gelijk is aan 2^3 x 3^2 x 5 x 7. Alle getallen van 1 tot 10 zijn factoren van 2520, wat betekent dat het volledig deelbaar is door elk van hen zonder rest.

# Om het kleinste positieve getal te vinden dat gelijkmatig deelbaar is door alle getallen van 1 tot 20, moeten we hun gemeenschappelijke veelvouden vinden. Dit kunnen we doen door hun priemfactoren te vinden en de grootste macht van elke priemfactor te gebruiken.

# De getallen van 1 tot 20 zijn: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20.

# De priemfactoren van elk van deze getallen zijn:
# - 16: 2^4
# - 9: 3^2
# - 5: 5 - 7: 7 - 11: 11 - 13: 13 - 19: 19

# - 6: 2 x 3
# - 10: 2 x 5
# - 12: 2^2 x 3
# - 14: 2 x 7
# - 15: 3 x 5
# - 17: 17
# - 18: 2 x 3^2
# - 20: 2^2 x 5

# Om het kleinste positieve getal te vinden dat gelijkmatig deelbaar is door alle getallen van 1 tot 20, moeten we de grootste macht van elke priemfactor nemen en deze vermenigvuldigen. Dit geeft ons 2^4 x 3^2 x 5 x 7 x 11 x 13 x 17 x 19, wat gelijk is aan 232792560.

# Dus het kleinste positieve getal dat gelijkmatig deelbaar is door alle getallen van 1 tot 20 is 232792560.

# Hier is een voorbeeld van Python-code die het kleinste positieve getal berekent dat gelijkmatig deelbaar is door alle getallen van 1 tot 20:


def smallest_multiple(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = 1
    for prime in primes:
        i = 1
        while prime**i <= n:
            i += 1
        result *= prime ** (i - 1)
    return result


print(smallest_multiple(20))

# De functie `smallest_multiple` neemt een argument `n` als de grootste waarde van de getallen waarvoor we het kleinste positieve getal willen vinden dat gelijkmatig deelbaar is door alle getallen van 1 tot `n`.

# De functie initialiseert een lijst `primes` met alle priemgetallen tussen 1 en `n`. Vervolgens wordt er door elk priemgetal gelopen en de grootste macht van elke priemfactor wordt berekend die kleiner is dan of gelijk is aan `n`. De functie vermenigvuldigt deze machten van elke priemfactor om het kleinste positieve getal te vinden dat gelijkmatig deelbaar is door alle getallen van 1 tot `n`.

# De functie retourneert dit resultaat.

# De `print`-verklaring roept de functie op met `n = 20` en drukt het resultaat af. Het resultaat is 232792560, zoals we eerder hebben gevonden.
