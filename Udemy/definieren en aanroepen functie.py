# Hier een voorbeeld van hoe je een functie kunt aanroepen en de waarde van de functie kunt terugkrijgen:

# In dit voorbeeld hebben we een functie verdubbel_getal() gedefinieerd die een getal verdubbelt en de verdubbelde waarde retourneert. Om de functie aan te roepen, moeten we het gewenste getal als argument doorgeven tussen de haakjes. In dit geval hebben we 5 doorgegeven.
# De geretourneerde waarde wordt vervolgens opgeslagen in de variabele resultaat. We kunnen deze waarde afdrukken door de print() functie te gebruiken. In dit voorbeeld zal de uitvoer 10 zijn, omdat we het getal 5 hebben verdubbeld.


# Definieer de functie
def verdubbel_getal(getal):
    verdubbeld = getal * 2
    return verdubbeld


# Roep de functie aan en krijg de geretourneerde waarde terug
resultaat = verdubbel_getal(5)

# Print de geretourneerde waarde
print(resultaat)

# Hier een voorbeeld van een functie die twee verschillende bewerkingen uitvoert:

# In dit voorbeeld hebben we een functie bereken() gedefinieerd die twee getallen als argumenten accepteert. De functie voert twee verschillende bewerkingen uit: het berekenen van de som en het verschil van de twee getallen. Vervolgens retourneert de functie beide waarden als een tuple.
# Om de functie aan te roepen, geven we twee getallen (10 en 5 in dit geval) door als argumenten. De geretourneerde waarden worden vervolgens opgeslagen in de variabelen resultaat1 en resultaat2. We kunnen deze waarden afdrukken door de print() functie twee keer te gebruiken. In dit voorbeeld zal de uitvoer 15 en 5 zijn, omdat we de som en het verschil van 10 en 5 hebben berekend.


# Definieer de functie
def bereken(getal1, getal2):
    som = getal1 + getal2
    verschil = getal1 - getal2
    return som, verschil


# Roep de functie aan en krijg de geretourneerde waarden terug
resultaat1, resultaat2 = bereken(10, 5)

# Print de geretourneerde waarden
print(resultaat1)
print(resultaat2)
