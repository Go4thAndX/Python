def calculator(getal1, getal2):
    som = getal1 + getal2
    verschil = getal1 - getal2
    product = getal1 * getal2
    quotient = getal1 / getal2
    return som, verschil, product, quotient


x = int(input("Wat is het eerste getal waarmee je een berekening wil uitvoeren ?: "))
y = int(input("Wat is het tweede getal waarmee je een berekening wil uitvoeren ?: "))
uitkomst = calculator(getal1=x, getal2=y)
print(uitkomst)
