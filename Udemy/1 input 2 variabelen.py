# Hier is een voorbeeld in Python waarbij één input wordt gebruikt om twee getallen in te voeren door middel van een scheidingsteken:

input_str = input("Voer twee getallen gescheiden door een spatie in: ")
# splits de input-string op, op basis van spaties
getallen = input_str.split()

if len(getallen) == 2:
    getal1 = int(getallen[0])
    getal2 = int(getallen[1])
    print("De twee getallen zijn:", getal1, "en", getal2)
else:
    print("Ongeldige invoer. Voer twee getallen gescheiden door een spatie in.")

# Dit programma vraagt om een ​​input-string waarin twee getallen gescheiden zijn door een spatie. De split()-methode wordt gebruikt om de string op de spaties te splitsen en de individuele getallen als afzonderlijke strings in een lijst op te slaan.

# Hier is hetzelfde voorbeeld als hierboven, maar met een komma als scheidingsteken:
input_str = input("Voer twee getallen gescheiden door een komma in: ")
# splits de input-string op, op basis van komma's
getallen = input_str.split(",")

if len(getallen) == 2:
    getal1 = int(getallen[0])
    getal2 = int(getallen[1])
    print("De twee getallen zijn:", getal1, "en", getal2)
else:
    print("Ongeldige invoer. Voer twee getallen gescheiden door een komma in.")

# Als er precies twee getallen in de lijst zitten, worden ze omgezet naar gehele getallen met de int()-functie en toegewezen aan de variabelen getal1 en getal2. Vervolgens worden de getallen geprint. Als er geen of meer dan twee getallen in de lijst zitten, wordt een foutmelding weergegeven.
