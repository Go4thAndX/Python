def calculator(nummer1, nummer2, bewerking):
    if bewerking == "+":
        return nummer1 + nummer2
    elif bewerking == "-":
        return nummer1 - nummer2
    elif bewerking == "*":
        return nummer1 * nummer2
    elif bewerking == "/":
        return nummer1 / nummer2


print("Welkom bij de rekenmachine !")
bewerking_list = ["+", "-", "*", "/"]
operand_true = True

while operand_true:
    # input_bewerking = input(f"Kies een bewerking {bewerking_list}: ")
    # input_bewerking = input(f"Kies een bewerking: {' '.join(bewerking_list)} > ")
    input_bewerking = input("Kies een bewerking + , - , * , / : ")

    if input_bewerking in bewerking_list:
        operand_true = False

    else:
        print("Geen juiste bewerking gekozen !!!")

# input_nummer1 = int(input("Voer het eerste getal in waarmee je een berekening wil uitvoeren: "))
# input_nummer2 = int(input("Voer het tweede getal in waarmee je een berekening wil uitvoeren: "))
while True:
    try:
        input_nummer1 = float(input("Voer het eerste getal in waarmee je een berekening wil uitvoeren: "))
        input_nummer2 = float(input("Voer het tweede getal in waarmee je een berekening wil uitvoeren: "))
    except ValueError:
        print("Ongeldige invoer. Voer alleen gehele getallen in.")
        continue
    else:
        break

antwoord = calculator(input_nummer1, input_nummer2, input_bewerking)
print(f"Het antwoord is: {antwoord}")
