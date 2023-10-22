def bereken_kwadraat(getal):
    antwoord = pow(getal, 2)
    return antwoord


print(bereken_kwadraat(5))
y = 3
uitkomst = bereken_kwadraat(getal=y)

if y > 9:
    print(f"Het kwadraat van {y} is {uitkomst} en bestaat uit 2 cijfers")
else:
    print(f"Het kwadraat van {y} is {uitkomst} en bestaat uit 1 cijfer")
