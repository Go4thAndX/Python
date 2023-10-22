'''
# Section 4: Day 4

# 41. Random Module

# De Random module die Python gebruikt wordt de Mersenne Twister genoemd.
# Om een willekeurig(random) geheel getal(integer) te genereren gebruiken we bijvoorbeeld de volgende code:

import random
# randint(a, b) genereert een willekeurig(random) geheel getal(integer) tussen a en b inclusief a en b
random_integer_1_10 = random.randint(1, 10)
print(random_integer_1_10)

In Python is het gebruikelijk om de code op te splitsen in afzonderlijke modules, waarbij elke afzonderlijke module verantwoordelijk is voor een ander deel van de funtionaliteit van ons programma of onze applicatie
Tot nu toe hebben we alleen nog maar code geschreven in de hoofdmodule met de file naam main.py maar we kunnen heel gemakkleijk onze eigen modules maken door nieuwe files toe te voegen aan onze applicatie en hier in onze hoofdmodule naar te laten verwijzen
In het volgende voorbeeld voegen we een nieuwe module toe, in deze module schrijven we onze code en in onze hoofdmodule verwijzen we naar deze nieuwe module en laten daar de code uitvoeren

import my_module

print(my_module.test_variable)

# Om een willekeurig(random) decimaal getal(float) te genereren gebruiken we de volgende code:
# random() genereert een willekeurig(random) decimaal getal(float) tussen 0.0 en 1.0 exclusief 0.0 en 1.0
random_float_0_1 = random.random()
print(random_float_0_1)

# Om nu een willekeurig(random) decimaal getal(float) te genereren met een ander bereik gebruiken we de volgende code:
# Hier gaan we een willekeurig decimaal getal genereren tussen 0.0 en 5.0
random_float_0_5 = random.random() * 5
print(random_float_0_5)

love_score_randint_1_100 = random.randint(1, 100)
print(f"Your love score love_score_randint_1_100)
'''

# 43. Understanding the Offset and Appending Items to Lists

# Lijsten(Lists) worden gebruikt om lijsten te genereren van items. Deze lijsten kunnen items van elk gegevenstype bevatten ook items met verschillende gegevenstypen. In Python beginnen en eindigen lijsten(lists) altijd met een vierkante haak(square bracket [ ] ) en in de lijst worden de verschillende items van elkaar gescheiden door een komma ( , ). Een voorbeeld van een lijst als code is:
fruits = ["Cherry", "Apple", "Pear"]

# Om een lijst van alle staten van de USA te krijgen kunnen we de namen van alle staten individueel aan een variabele toekennen zoals:
state1 = "Delaware"
state2 = "Pennsylvania"
state3 = "New Jersey"

# Maar het veel gemakkelijker om dit te doen met een lijst, waarvan elke naam van alle staten individueel eem item is met item nummer, dus met een gegeven volgorde structuur  in een lijst, waarbij het eerste item de index nul( 0 ) bezit en het tweede item de index een( 1 ) bezit en zo verder tot aan het einde van de lijst en omdat elk item een indexnummer heeft kunnen we met de behulp van de code in Python nu heel gemakkelijk bewerkingen uitvoeren met een lijst zoals het wijzigen van een item, het toevoegen van een item, het verwijderen van een item, de volorde wijzigen van de lijst, het aantal items bepalen in de lijst, de lijst sorteren volgens bepaalde criteria en sub-lijsten maken als een deelverzameling van de oorspronkelijke lijst.
# Een voorbeeld van zo'n lijst is een lijst van alle namen van de staten van de USA in de volgorde van wanneer deze staat deel geworden is van de unie der staten, waarbij dus in dit geval de staat Delaware het eerste item in de lijst is met als index 0 en het tweede item is de staat Pennsylvania met als index 2 en zo verder.
states_names_usa_order_date_admission = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Om nu te weten te komen welke staat dus de eerste is in deze lijst kan ik de volgende code gebruiken:
print(states_names_usa_order_date_admission[0])

# En het tiende item in de lijst heeft dus index 9.
print(states_names_usa_order_date_admission[9])

# Om nu te weten te komen welke staat de laatste in de lijst is kan ik de volgende code gebruiken:
print(states_names_usa_order_date_admission[-1])

# En het elfde item in de lijst teruggerekend vanaf het laatste item in de lijst met index -1 heeft dus index -11.
print(states_names_usa_order_date_admission[-11])

# Om een item te wijzigen bijvoorbeeld de naam van de staat Pennsylvania te wijzigen in Pencilvana kunnen we de volgende code gebruiken.
states_names_usa_order_date_admission[1] = "Pencilvana"
print (states_names_usa_order_date_admission)

# Om eem item aan de lijst toe te voegen en meestal doen we dat aan het einde van een lijst, gebruiken we de de functie toevoegen(append) met de volgende code.
states_names_usa_order_date_admission.append("Janus Georgia")
print (states_names_usa_order_date_admission)
# Een ander voorbeeld van zo'n lijst is een lijst van alle namen van de staten van de USA in alfabetische volgorde, waarbij dus in dit geval de staat Alabama het eerste item in de lijst is met als index 0. 
states_names_usa_order_alphabet = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Omdat je heel veel verscheiden functies hebt die je kunt gebruiken met lijsten binnen de Python code is het veel gemakkelijke om deze te bestuderen maar niet perse te onthouden op het internet en deze worden beschreven via https://docs.python.org/3/tutorial/datastructures.html

# Als voor beeld gebruiken we de funtie uitbreiden(extend) waarbij onze lijst wordt uigebreid(extended) met als het ware een tweede of extra lijst aan het einde van de eerste of originele lijst.
states_names_usa_order_date_admission.extend(["Gerard Land", "Trans Sylviatus"])
print (states_names_usa_order_date_admission)
