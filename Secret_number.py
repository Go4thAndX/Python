import random

geheim_nummer = random.randint(0, 100)
# print(geheim_nummer)

print("Raad het geheime nummer tussen 0 en 100")
print()

while True:
    nummer = input("Raad het getal: ")

    # Het geselecteerde codefragment is een try-except-blok in Python. Het wordt gebruikt om eventuele fouten op te vangen die optreden bij het proberen een variabele genaamd "nummer" om te zetten naar een geheel getal met behulp van de int() functie.

    # Binnen het try-blok probeert de code de variabele "nummer" om te zetten naar een geheel getal met behulp van de int() functie. Als de conversie succesvol is, zal de code doorgaan met de uitvoering na het try-except-blok.

    # Als er tijdens de conversie een fout optreedt, wordt het except-blok uitgevoerd. In dit geval is de fout waarschijnlijk een ValueError, wat aangeeft dat de variabele "nummer" niet kan worden omgezet naar een geheel getal. Het except-blok geeft de boodschap "Sorry dat is geen getal" weer en de continue instructie wordt gebruikt om over te gaan naar de volgende iteratie van een lus (als deze code binnen een lus wordt gebruikt).

    # Samengevat controleert deze code of een variabele genaamd "nummer" kan worden omgezet naar een geheel getal. Als dat kan, gaat de code verder met de uitvoering. Zo niet, dan wordt er een foutmelding weergegeven en gaat de code verder met de volgende iteratie.

    try:
        nummer = int(nummer)
    except:
        print("Sorry dat is geen getal")
        continue

    if nummer != geheim_nummer:
        if nummer > geheim_nummer:
            print(f"{nummer}, is groter dan het geheime getal")

        elif nummer < geheim_nummer:
            print(f"{nummer}, is kleiner dan het geheime getal")
    else:
        print(f"Je hebt het geheime nummer {geheim_nummer} geraden")
        break
