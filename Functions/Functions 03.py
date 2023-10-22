def print_groet(voornaam, achternaam):
    print(f"Hallo {voornaam} {achternaam}")
    print("Deze functie print een groet met een gegeven voor- en achternaam")


print_groet("Jan George", "Koomen")
print_groet("Sylvia", "Lusink")
input_voornaam = input("Wat is je voornaam ?: ")
input_achternaam = input("Wat is je achternaam ?: ")
print_groet(input_voornaam, input_achternaam)
