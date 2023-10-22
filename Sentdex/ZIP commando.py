# Het zip-commando in Python wordt gebruikt om twee of meer iterabele objecten samen te voegen
# (bijvoorbeeld lijsten, tuples, enz.) en paren van elementen te creëren op basis van hun positie.
# In dit voorbeeld zijn de elementen van lijst1 en lijst2 samengevoegd in paren op basis van hun positie.
# Let op dat zip een iterator teruggeeft. Als je het resultaat opnieuw wilt gebruiken of doorlopen,
# moet je het omzetten naar een lijst of een ander iterabel, zoals in het onderstaande voorbeeld.
# Daarnaast is het belangrijk op te merken dat als de input-iterables verschillende lengtes hebben,
# zip stopt wanneer de kortste iterabele is uitgeput. Dit betekent dat eventuele extra elementen in de langere
# iterabele genegeerd zullen worden.

# Hier is een eenvoudig voorbeeld van hoe je het zip-commando kunt gebruiken:
lijst1 = [1, 2, 3]
lijst2 = ['a', 'b', 'c']
# Gebruik van zip om de twee lijsten samen te voegen
samengevoegd = zip(lijst1, lijst2)
print(samengevoegd)
# Output: <zip object at 0x0000021A4F964B00>
# Converteer het resultaat naar een lijst (of een ander iterabel)
samengevoegde_lijst1 = list(samengevoegd)
print(samengevoegde_lijst1)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

lijst3 = [1, 2, 3, 4]
lijst4 = ['d', 'e', 'f']
# Gebruik van zip om de twee lijsten samen te voegen
samengevoegd = zip(lijst3, lijst4)
# Converteer het resultaat naar een lijst (of een ander iterabel)
samengevoegde_lijst2 = list(samengevoegd)
print(samengevoegde_lijst2)
# Output: [(1, 'd'), (2, 'e'), (3, 'f')]

# Deze code voert een iteratie uit over twee lijsten, listA en listB, waarbij de elementen op dezelfde positie in beide
# lijsten worden gekoppeld. De zip()-functie neemt de elementen van beide lijsten in volgorde en maakt paren van
# overeenkomstige elementen. Vervolgens worden deze paren gedurende elke iteratie uitgepakt in de variabelen
# iteratie1 en iteratie2.
#
# Stel dat listA gelijk is aan [1, 2, 3] en listB gelijk is aan ['a', 'b', 'c'].
listA = [1, 2, 3]
listB = ['a', 'b', 'c']
for iteratie1, iteratie2 in zip(listA, listB):
    print(iteratie1, iteratie2)
# Output:
# 1 a
# 2 b
# 3 c
