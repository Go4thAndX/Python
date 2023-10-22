# Het gebruiken van de random functie
import random

# Het genereren van een willekeurig geheel getal tussen 0 en 9:
random_number = random.randint(0, 9)
print(random_number)

# Het genereren van een willekeurig zwevendekomma-getal tussen 0 en 1:
random_number = random.randint(0, 9)
print(random_number)

# Het genereren van een willekeurige keuze uit een lijst:
my_list = ['a', 'b', 'c', 'd']
random_choice = random.choice(my_list)
print(random_choice)

# Het mengen van een lijst op een willekeurige volgorde:
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
