# This code checks if a given number is a prime number

# A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
# Write a function that checks whether if the number passed into it is a prime number or not


# Definieer de functie: [check_prime] met de Parameter: [number]
def check_prime(number):
    # Definieren van de varibele: [is_prime] en het toekennen van de waarde: [True] aan de variabele
    is_prime = True
    for i in range(2, number):
        # Output controle van alle waardes van i die gebruikt worden om te controleren of het nummer een priem-getals is
        # print(f"{number} / {i} = {number / i}")
        if number % i == 0:
            is_prime = False
    # Onderstaande code kan ook vervangen worden door:
    # if is_prime:
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Definieren van de variabele: [input_number] en het toekennen van de input waarde als integer aan de variabele
input_number = int(
    input(
        "Give a number greater then 1 as input and check if this number is a prime number: "
    )
)
# Controleren of de input een nummer groter als 1 is
if input_number <= 1:
    print("You didn't gave a correct number as input")
    # Het aanroepen van de functie: [check_prime] waarbij we de waarde van de variabele: [input_number] als Argument: [number = input_number] doorgeven aan de Parameter: [number] van de functie
else:
    check_prime(number=input_number)
