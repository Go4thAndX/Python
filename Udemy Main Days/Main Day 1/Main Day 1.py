'''
# Section 1: Beginner - Working with Variables in Python to Manage Data.
# 
# 06. Printing to the console in Python
# print() drukt de tekst tussen de haakjes in de console af
# tekst moet tussen aanhalingstekens (" " of ' ') geplaats worden
print("Hello world!")

# 09. String Manipulation and Code Intelligence
# \n zorgt er voor dat de tekst op een nieuwe regel afgedrukt wordt.
print("Hello world!\nHello world!")
# met de + kunnen we tekst aan elkaar koppelen (concatenate)
print("Hello" + " " + "Angela")

# 11. The Pyton Input Funtion
# input() zorgt voor gebruiker invoer in de console en print() drukt de tekst samen met gebruiker invoer af
print("Hello " + input("What is your name ? "))
# len bepaald uit hoeveel karakters de string is opgebouwd
print( len( input("What is your name ? ") ) )

# 13. Python Variables
# name is de naam van de variabele die de waarde van input("What is your name ? ") meekrijgt of gaat bevatten
name = input("What is your name ? ")
print(name)

name = "Jack"
print(name)

name = "Angela"
print(name)

# We gaan nu de code regel voorzien van variabelen:
print( len( input("What is your name ? ") ) )
# de variabele naam (string) wordt toegekend aan de input op de vraag What is your name ?:
name = input("What is your name ? ")
# de variabele length (integer) wordt toegekend aan de lengte (totaal aantal karakters inclusief spaties) van de variabele naam (string):
length = len(name)
# print zorgt voor de "output" van de lengte van de naam van de verkregen "input":
print(length)

# We gaan code schrijven om de waardes van de variabelen omwisselen met als voorbeeld hoe we de inhoud van een glas melk en kopje koffie omwisselen en daarvoor gebruiken we als extra variabele de beker:
In het glas zit melk
In het kopje zit koffie
Pak een lege beker
Giet de melk in de beker
Giet nu de koffie uit het kopje in het glas
Giet nu de melk uit de beker in het kopje

Glas_inhoud = ("Melk")
Kopje_inhoud = ("Koffie")
print(Glas_inhoud)
print(Kopje_inhoud)
Beker_inhoud = Glas_inhoud
Glas_inhoud = Kopje_inhoud
Kopje_inhoud = Beker_inhoud
print(Glas_inhoud)
print(Kopje_inhoud)

# 15. Varible Naming
Maak code leesbaar en dat geldt zeker voor het declareren van variabelen, de afspraak hierover in Python is dat je geen hoofdletters gebruikt en een "underscore" ( _ ) tussen de verschillende woorden waaruit je variabelen mogelijk bestaan.
Je kunt cijfers gebruiken in variabelen maar die mogen niet als "eerste" teken gebruikt worden in de namen van je variabelen.
Ook kun je beter niet dezelfde namen voor variabelen gebruiken die ook als gereserveerde code in Pytnon gebruikt worden, dit is verwarrend en leidt soms tot errors.
# Onleesbare code, het is onduidelijk wat de variabel voorsteld:
n = 10
# Beter is:
first_choice_number = 10
# Niet toegestaan is en veroorzaakt een "syntax error"
1name = "Jan George
# Toegestaan is:
name1 = "Jan George"
name2 = "Gerard"
# Maar beter is:
first_name_person_one = "Jan George"
first_name_person_two = "Gerard"
# En de volgende variabele naam is wel toegestaan maar kan problemen veroorzaken in de code:
input = input("What is your first name ? ")
# Beter is:
first_name_input = input("What is your first name ?")
'''