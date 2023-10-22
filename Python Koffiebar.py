klein = 2
normaal = 5
groot = 9

gebruikers_budget = input("Wat is uw budget in Euro ?: ")

try:
    gebruikers_budget = int(gebruikers_budget)
except:
    print("Voer een juist bedrag in aub")
    exit()

if gebruikers_budget >= 2:
    if gebruikers_budget >= groot:
        print("U heeft genoeg geld voor een grote koffie")

        if gebruikers_budget == groot:
            print("Uw koffie is gereed")
        else:
            print(f"Uw wisselgeld is ({gebruikers_budget} - {groot}) Euro")
    elif gebruikers_budget == normaal:
        print("U heeft genoeg geld voor een normale koffie")
        print("Uw koffie is gereed")
    elif gebruikers_budget >= klein:
        print("U heeft genoeg geld voor een kleine koffie")

        if gebruikers_budget == klein:
            print("Uw koffie is gereed")
        else:
            print(f"Uw wisselgeld is ({gebruikers_budget} - {klein}) Euro")
elif gebruikers_budget == 1:
    print("U heeft te weinig geld voor een kleine koffie")
    print(f"U ontvangt uw {gebruikers_budget} Euro weer terug")
else:
    print("U heeft helemaal geen geld voor koffie")
