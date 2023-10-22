# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# print(names)
# Aantal items in de list
number_names = len(names)
# print(number_names)

# aanpassen random aan aantal items in de list
random_int_number = random.randint(0, number_names - 1)
# print(random_int_number)
print(f"{names[random_int_number]} is going to buy the meal today!")
# de code kan gemakkelijker als we de choice functie gebruiken
print(f"{random.choice(names)} is going to buy the meal today!")