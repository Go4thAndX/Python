import csv
import decimal
# Dit script maakt gebruik van een oneindige while-lus om de koffiemachine
# actief te houden totdat je het "off(-line)" commando geeft. Je kunt andere
# commando's zoals "bij(vullen)", "geld( verzamelen)" en "rap(portage)"
# gebruiken.

# TODO Het script aanpassen zodat als er te lang gewacht wordt met betalen,
#  het geld geretourneerd word en de machine weer een nieuwe klant kan helpen

# Pad naar CSV-bestanden
coffee_data_file = "coffee_data.csv"
inventory_file = "inventory.csv"
money_file = "money.csv"

# Munten en hun waarden
coins = {
    "dollar": decimal.Decimal("1.00"),
    "quarter": decimal.Decimal("0.25"),
    "dime": decimal.Decimal("0.10"),
    "nickel": decimal.Decimal("0.05"),
    "penny": decimal.Decimal("0.01")
}

# Laden van koffiegegevens uit CSV
def load_coffee_data():
    coffee_data = {}
    with open(coffee_data_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            coffee_data[row["type"]] = {
                "price": float(row["price"]),
                "water": int(row["water"]),
                "coffee": int(row["coffee"]),
                "milk": int(row["milk"])
            }
    return coffee_data

# Laden van voorraadgegevens uit CSV
def load_inventory():
    inventory = {}
    with open(inventory_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            inventory[row["ingredient"]] = int(row["quantity"])
    return inventory

# Laden van geldgegevens uit CSV
def load_money():
    with open(money_file, newline="") as file:
        reader = csv.reader(file)
        return float(next(reader)[0])

# Opslaan van voorraadgegevens naar CSV
def save_inventory(inventory):
    with open(inventory_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ingredient", "quantity"])
        for ingredient, quantity in inventory.items():
            writer.writerow([ingredient, quantity])

# Opslaan van geldgegevens naar CSV
def save_money(money):
    with open(money_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([money])

# Koffiemachine simulatie
def coffee_machine_simulation():
    global amount, coin
    coffee_data = load_coffee_data()
    inventory = load_inventory()
    money = load_money()

    while True:
        choice = input("Welke koffie wilt u hebben ? (espresso, latte, "
                       "cappuccino): ")

        if choice == "e":
            choice = "espresso"
        elif choice == "l":
            choice = "latte"
        elif choice == "c":
            choice = "cappuccino"

        if choice in coffee_data:
            coffee = coffee_data[choice]
            if (
                coffee["water"] <= inventory["water"]
                and coffee["coffee"] <= inventory["coffee"]
                and coffee["milk"] <= inventory["milk"]
            ):
                print(f"Voordat uw {choice} bereid wordt is het noodzakelijk"
                      f" om ${coffee['price']:.2f} te betalen:")

                # Munten tellen
                total_paid = decimal.Decimal(0)
                while total_paid < coffee["price"]:

                    not_coin_kind = True
                    while not_coin_kind:
                        coin = input("Met welke munt gaat u betalen "
                                     "dollar [1.00], "
                                     "quarter [0.25], "
                                     "dime [0.10], "
                                     "nickel [0.05], "
                                     "penny [0.01]\n"
                                     "Voer een '$', 'q', 'd', 'n', 'p' in: ")

                        if coin == '$':
                            coin = "dollar"
                            not_coin_kind = False
                        elif coin == "q":
                            coin = "quarter"
                            not_coin_kind = False
                        elif coin == 'd':
                            coin = "dime"
                            not_coin_kind = False
                        elif coin == 'n':
                            coin = "nickel"
                            not_coin_kind = False
                        elif coin == 'p':
                            coin = "penny"
                            not_coin_kind = False
                        else:
                            print("U heeft geen juiste munt ingevoerd !")

                    amount_not_positif_integer = True
                    while amount_not_positif_integer:
                        amount = (input(f"Hoeveel {coin} gaat u betalen ?: "))
                        # Controleren of de invoer een geheel getal is
                        if amount.isdigit():
                            amount = int(amount)
                            amount_not_positif_integer = False
                        else:
                            print("De invoer is geen geheel positief getal.")

                    if coin in coins:
                        total_paid += coins[coin] * amount
                        print(f"U heeft tot nu toe ${total_paid} betaald.",
                              end=" ")

                        if total_paid != coffee["price"]:

                            if total_paid <= coffee["price"]:
                                to_pay = decimal.Decimal(coffee["price"])\
                                         - total_paid
                                print(f"U moet nog ${to_pay} betalen.")

                if total_paid >= coffee["price"]:
                    change = total_paid - decimal.Decimal(coffee["price"])
                    if change > 0:
                        print("Uw wisselgeld is: $", change)
                    else:
                        print("Bedankt voor uw betaling!")

                    # Voorraad bijwerken
                    inventory["water"] -= coffee["water"]
                    inventory["coffee"] -= coffee["coffee"]
                    inventory["milk"] -= coffee["milk"]
                    save_inventory(inventory)

                    # Geld bijwerken
                    money += coffee["price"]
                    save_money(money)

                else:
                    print("Onvoldoende betaling. Geld wordt teruggestort.")

            else:
                print("Sorry, er is onvoldoende water, koffie of melk voor "
                      "deze koffie.")

        elif choice == "off":
            print("Koffiemachine gaat offline.")
            break

        elif choice == "bij":
            print("Het water, de koffie en de melk worden bijgevuld")
            inventory["water"] = 1000
            inventory["coffee"] = 300
            inventory["milk"] = 500
            save_inventory(inventory)

        elif choice == "geld":
            print(f"Het totaal aan ontvangen geld {money} "
                  "wordt aan de machine onttrokken")
            money = 0
            save_money(money)

        elif choice == "rap":
            print("----- Rapportage -----")
            print("Voorraad koffie ingrediënten:")
            for ingredient, quantity in inventory.items():
                print(ingredient.capitalize() + ":", quantity)
            # for coffee_type, data in coffee_data.items():
            #     print(coffee_type.capitalize() + ":", data["price"])
            print("Huidige hoeveelheid geld opgeslagen: $", load_money())
            print("----------------------")

        else:
            print("Ongeldige keuze. Probeer opnieuw.")


# Koffiemachine starten
coffee_machine_simulation()
