# Voorbeeld van de shuffle functie in Python
# 
# list = [1, 2, 3, 4, 5]
# random.shuffle(list)
# print(list)  # [5, 2, 1, 4, 3]

'''Proberen zelf de shuffle functie te coderen
Random een keuze te maken uit de items uit een lijst1, dit item dan in een andere lijst2 plaatsen, het huidige item dan uit lijst1 verwijderen en dit herhalen met een for loop totdat alle items in de andere lijst zitten.
'''
import random

#Lijst met getallen
list1 = [1, 2, 3, 4, 5]
print(f"\nDe originele lijst was  {list1}")
# len_list1 = len(list1)
list2 = []

# Kies een random getal uit lijst1
# for i in range(0, len_list1):
for i in range(0, len(list1)):
    # index = random.randint(0, len_list1 - 1)
    index = random.randint(0, len(list1) - 1)
    # plaats het getal in lijst2
    list2.append(list1[index])
    del list1[index]

print(f"\nDe geshuffelde lijst is {list2}")

# lijst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lijst2 = []

# # Kies een random getal uit lijst1
# for i in range(0, len(lijst1)):
#     index = random.randint(0, len(lijst1)-1)
#     # Plaats het getal in lijst2
#     lijst2.append(lijst1[index])
#     # Verwijder het getal uit lijst1
#     del lijst1[index]

# print(lijst2)