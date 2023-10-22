'''
# Section 2: Day 2
# 19. Pythons Primitive Data Types

print(len("Hello"))
# Maar als we als argument een nummer ingeven zoals:
print(len(12345))
# Dan veroorzaken we een zogenaamde TypeError:
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     print(len(12345))
# TypeError: object of type 'int' has no len()

# Python heeft verschillende primaire data typen

# Data Types

# String
print("Hello"[0])
print("Hello"[4])
# We willen graag twee nummers bij elkaar optellen kan dat met de volgende code regel ?:
print("123" + "456")
# Nee want in feite voegen we hier twee nummers als string samen (concatenate) en is het resultaat "123456"

# Integer

# Een integer is een getal zonder komma ( , ) let heel erg op dat Python een op de Engelse of Amerikaanse cultuur gebaseerde programmeer taal is waar ze een punt ( . ) gebruiken waar wij een komma ( , ) gebruiken
123
print(123)
123 + 456
print(123 + 456)

# Als we grote getallen gebruiken in code zoals:
123456789
print(123456789)
# Python, gebruikt als een op de Engelse of Amerikaanse cultuur gebaseerde programmeer taal de komma ( , ) als scheidingsteken tussen de 1000-tallen waar wij in Europa (met uitzondering van Engeland dus) een punt ( . ) gebruiken het getal 123456789 wordt in Python 123,456,789 en niet 123.456.789 maar omdat te voorkomen kent Python de volgende oplossing:
123_456_789
print(123_456_789)

# Float

# Getallen die een decimaal karakter hebben, bevatten dus een punt ( . ) in hun notatie die aangeeft dat achter deze punt het decimale gedeelte van het getal aanvangt
3.14159
print(3.1459)

# Boolean
# Elke programmertaal kent zogenaamde variabelen van het Boolean-type en deze kunnen of waar ( True ) of onwaar, fout ( False ) zijn en worden gebruikt in zogenaamde Booleaanse code waarbij wordt afgevraagd of iets waar ( True ) of onwaar, fout ( False ) is en waarvan op basis van deze waarden beslissingen in de code genomen kunnen worden
True
print(True)
False
print(False)

number_fir = 123
number_sec = 456
number_sum = number_fir + number_sec
# Als we nu de volgende print regel zouden willen uitvoeren 
# print("The sum of the number " + number_fir + "and number " + number_sec + "= " + number_sum)
# Dan veroorzaken we een foutcode ( error )
# Traceback (most recent call last):
#   File "main.py", line 35, in <module>
#     print("The sum of the number " + number_fir + "and number " + number_sec +"= " + number_sum)
# TypeError: can only concatenate str (not "int") to str
# We kunnen geen tekst (string) samenvoegen (concatenate) met een getal (string), daarvoor moeten we ervoor zorgen dat alle variabelen van een gelijk type zijn dus in dit geval moeten we de getallen (integers) omzetten in tekst (string) en om een string om te zetten in een integer gebruiken we het volgende code voorbeeld:

length_name = len(input("What is your name ?\n"))
print(length_name)
# Om te zien met welk type variabele we te makken hebben kunnen we de volgende code gebruiken:
type(length_name)
# De code 'type' geeft ons dus in dit geval als waarde: <class 'int'>, we kunnen dus 'type' gebruken in onze code om te achterhalen van welke "soort" onze variabele is
print(type(length_name))
# Om nu een getal om te zetten in een string gebruiken we:
str(length_name)
new_length_name = str(length_name)
print(type(new_length_name))
print(new_length_name)

# Dus nu kunnen we onze vorige code die niet werkte omdat we verschillende types van variabelen wilden combineren omzetten in de volgende code:
new_number_fir = str(number_fir)
new_number_sec = str(number_sec)
new_number_sum = str(number_sum)
print("The sum of the number " + new_number_fir + " and the number " + new_number_sec + " is " + new_number_sum)

a = 123
print(a)
print(type(a))
a = float(123)
print(a)
print(type(a))

b=100
print(b)
print(type(b))
c=100.0
print(c)
print(type(c))

new_b = (70 + float("100"))
print(new_b)
# Ik zou verwachten dat een variabele opgebouwd uit een 'integer' en een 'float', het type 'float' zou krijgen maar volgens dit voorbeeld blijft het een 'integer' ????
print(type(b))

# 22. Mathematical Operations in Python

# 3+5 optellen
# 7-4 aftrekken
# 3*2 vermenigvuldigen
# 6/3 delen
# 2**3 tot de macht verheffen

# Let op de volgorde waarin de rekenkundige bewerkingen gaan plaatsvinden die gebonden is aan de regels die in deze versie van Python gelden
PE(MD)(AS)L>R
Parentheses (haakjes)
Exponents (machtsverheffen)
Multiplication Division 
Addition Subtraction 
From Left to Right
# Hieronder wat voorbeelden van het toepassen van wat de volgorde van uitvoering betekend:

# Dus volgorde van de berekening van links naar rechts begint met 3*3=9 dan 3/3=1 dan 9+1=10 dan 10-3=7 en omdat er een deling in de berekening voorkomt is het resultaat van het type float dus 7=7.0
print(3*3+3/3-3)
# Dus volgorde van de berekening van links naar rechts begint met 3+3=6 dan 3*6=18 dan 18/3=6 dan 6-3=3 en omdat er een deling in de berekening voorkomt is het resultaat van het type float dus 3=3.0
print(3*(3+3)/3-3)

# 24. Number Manipulation and F Strings in Python

# Hier krijgen we als antwoord een getal van het type float
num=(8/3)
print(num)
print(type(num))
# Als antwoord krijgen we een getal van het type int waarbij alle decimalen = cijfers achter de comma (.) verloren gaan
num_int=int(num)      
print(num_int)
print(type(num_int))
# Om een getal af te ronden gebruiken we de functie round Als antwoord krijgen we "vreemdgenoeg" een getal van het type int waarbij het getal wordt afgerond naar het dichtsbijzijnde gehele getal
num_round=round(num)
print(num_round)
print(type(num_round))
# Om een getal af te ronden tot 2 decimalen gebruiken we 
num_round_two=round(num, 2)
print(num_round_two)
print(type(num_round_two))
# Om een getal af te ronden naar het dichtstbijzijnde gehele getal, gebruiken we "vloerdelen" ( // )
num_floordivision=8//3
print(num_floordivision)
print(type(num_floordivision))

# Om een rekenkundige bewerking te herhalen kunnen we de volgende code gebruiken:
result=10/3
print(result)
result/=3
print(result)
# En dit geldt voor de volgende rekenkundige bewerkingen: +=, -=, *=, /= en **=
score=2
score**=3
print(score)
# Om meerdere type variabelen te kunnen combinere in een print opdracht, zonder iedere variabele te moeten wijzigen in een overeenkomend type gebruiken we de zogenaamde "f-String"
age=61
height=1.8
pension=True
print(f"Your age is {age}, your height is {height}m and it is {pension} that you recieve a pre-pension income.")
'''