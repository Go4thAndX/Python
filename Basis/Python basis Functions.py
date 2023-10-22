# Python Function: hoe ga je te werk met functies?

# De Python function is een van de meest fundamentele bouwblokken die je als Data Scientist tot je beschikking hebt binnen Python. Als je Python leert is kennis opdoen van functions daarom essentieel.

# Wat is een Python function?

# Een Python function is een samenhangend stukje code dat een specifieke taak uitvoert. Je voert een input in, vervolgens voert de functie de taak uit en geeft een bepaalde output terug.

# Python functions zijn zo handig om de volgende redenen:

# 1. Functies zijn herbruikbaar. Als je een specifieke taak vaker uit moet voeren dan leveret het gebruik van functies je veel tijdswinst op.
# 2. Functies breken grote programma's of modellen op in kleinere delen. Dit maakt lange stukken code overzichtelijker en makkelijker te begrijpen. Zelfs bijvoorbeeld complexe machine learning modellen zijn dankzij functies relatief makkelijk te doorgronden.

# Welke ingebouwde functions heeft Python?

# Er is standaard een aantal Python functions ingebouwd. Het is goed om je bewust te zijn van de ingebouwde mogelijkheden van Python.

# Ingebouwde functies zijn over het algemeen basale functies als het optellen van waarden met [sum()], het creëren van een lijst met [list()], of het aanpassen van data types van variables met bijvoorbeeld [int()], [float()], of [str()].

# Een ander argument om de built in functies te kennen is omdat er conflicten op kunnen treden als je eigen functies in het leven roept met dezelfde naam als built-in functies. Echter, in de meeste software krijgen ingebouwde functies een highlight-kleur waardoor je ze makkelijk herkent.

# Wanneer je bepaalde Python packages importeert komen er nieuwe functies vanuit het package beschikbaar. Bekijk dus ook altijd goed de documentatie die hoort bij verschillende data science packages.

def functienaam(parameter):
    taak = parameter * parameter
    return taak

# 1. De term [def] gebruik je om een functie header te starten. Je sluit de header altijd af met een dubbelepunt [:].
# 2. De [functienaam] is een unieke naam voor de functie waarmee deze aangeroepen kan worden.
# 3. Tussen haakjes [( )] zet je nul, één of meerdere parameters (ook wel input variabelen genoemd), gescheiden door een comma [ , ].
# 4. Dan volgt de body van de functie. Hier voert de functie de specifieke taak uit en worden de argumenten die zijn ingegeven omgezet in een bepaalde output. Na start van de functie spring je steeds 4 spaties in (indenteren) totdat de functie eindigt.
# 5. Met een [return] statement geeft je een output waarde uit een functie.

# Keyword arguments vs. positional arguments: We kunnen de argumenten in een functie op verschillende manieren ingeven. Als voorbeeld nemen we de volgende functie:

def twee_kwadraten_aftrekken(a,b):
    kwadraat_1 = a * a
    kwadraat_2 = b * b
    return kwadraat_1 - kwadraat_2

# Je kunt op twee manieren argumenten in deze functie stoppen:

# 1. twee_kwadraten_aftrekken(a=10,b=100) en twee_kwadraten_aftrekken(b=100,a=10) zullen hetzelfde resultaat geven, namelijk -9900. We noemen dit keyword arguments omdat duidelijk aangegeven wordt welk argument bij welke parameter hoort.
# 2. Het is ook mogelijk om positional arguments te gebruiken. Je geeft een argument in en op basis van de positie gaat de functie er op een bepaalde manier mee om. twee_kwadraten_aftrekken(10,100) en twee_kwadraten_aftrekken(100,10) zullen dus wel degelijk andere antwoorden geven, namelijk -9900 en 9900. Bij positional arguments hoef je minder te schrijven waardoor je sneller kunt programmeren en code sneller kan runnen. Het vergt echtere wel meer oplettendheid.

# Meerdere return variabelen of meerdere return statements

# Stel je wilt meerdere variabelen als output uit jouw Python function, hoe doe je dat? Dat is eigenlijk vrij simpel. Je kunt gewoon twee variabelen achter jouw return statement zetten, gescheiden door een comma [ , ].

def twee_kwadraten(a, b, oplopend = True):
    kwadraat_1 = a * a
    kwadraat_2 = b * b
    kwadraten = [kwadraat_1, kwadraat_2]
    if oplopend:
        return sorted(kwadraten)
    else:
        return kwadraten
    
print(twee_kwadraten(100, 10, oplopend = False))
print(twee_kwadraten(100, 10, oplopend = True))

# Global en local scope

# Wanneer je werkt met functies is het goed om het onderscheid tussen global en local scope te begrijpen. Het zit namelijk zo dat variabelen die je in een functie definieert in een tijdelijk geheugen worden opgeslagen. Dit geheugen wordt gewist wanneer de functie volledig gerund is. Om deze reden zijn variabelen van binnen een functie niet beschikbaar buiten een functie. Dit noemt men ook wel 'memory isolation'.

# Het omgekeerde is wat ingewikkelder. Variabelen uit de global scope kunnen wel beschikbaar zijn in een functie (local scope). Het is echter zo dat Python altijd eerst binnen de functie kijkt of de variabele is gedefinieerd. Is dit niet zo dan zoekt Python in de global scope of de variabele bekend is. Als een variabele zowel in de local scope als in de global scope beschikbaar is dan geeft Python prioriteit aan de local scope, dus binnen de Python function.

# Memory isolation is handig omdat je bij grotere programma's vaak niet meer weet welke variabelen allemaal bestaan in het volledige programma (global scope). Je kunt met een gerust hart nieuwe variabelen introduceren in functies en deze worden dan alleen binnen de functie gebruikt (local scope).

# Nog wat voorbeelden van het gebruik van functies:

def voorbeeld():
    print("Hallo allemaal")
    print("Ik ben een voorbeeldfunctie")

# allerlei slimme dingen (Python code)
voorbeeld()
# nog meer slimme dingen (Python code)
voorbeeld()

def groet(naam):
    print("Hallo", naam)
    print("Moge vele appeltaarten uw pad kruisen vandaag !")

groet("Henk")
groet("Frits")

invoer = input("Geef je naam ")
groet(invoer)

def kwadraat(getal):
    antwoord = getal * getal
    return antwoord

# allerlei slimme dingen (Python code)
print(kwadraat(3))
# nog meer slimme dingen (Python code)
x = kwadraat(5)
print(x + 10)

if x < 30:
    print("Joepie")
else:
    print("Hoera")
    