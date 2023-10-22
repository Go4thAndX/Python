from lists import MENU, resources, coins
import pandas as pd


def main_program():
    print("*** main_program() started ***")
    result_price = choose_coffee(choice=coffee_choice)
    print(f"Please insert quarters and other coins to match the price.")
    # TODO Overweeg om code te schrijven die aangeeft dat er teveel tijd is
    #  verstreken met het invoeren van munten waardoor de munten weer
    #  teruggegeven worden en de coffee machine zich weer naar de beginstatus
    #  reset.
    money = ["quarter", 0.25]
    money, enough = calculate_money(cost=result_price, coin=money)
    rounded_money = round(money, 2)

    if not enough:
        print("Please insert dimes and other coins to match the price.")
        money = ["dime", 0.1]
        money, enough = calculate_money(cost=rounded_money, coin=money)

    if not enough:
        print("Insert nickels and other coins to match the price.")
        money = ["nickel", 0.05]
        money, enough = calculate_money(cost=rounded_money, coin=money)
        rounded_money = round(money, 2)

    if not enough:
        print("Insert pennies to match the price.")
        money = ["penny", 0.01]
        money, enough = calculate_money(cost=rounded_money, coin=money)

    if not enough:
        print(f"Sorry you didn't insert enough money to buy {coffee_choice}")
        # TODO schrijf code om het betaalde geld terug te geven aan de klant


def replenish_resources(resources):
    print("*** replenish_resources() started ***")
    # TODO schrijf code om de resources aan te kunnen vullen


def choose_coffee(choice):
    print("*** choose_coffee() started ***")
    data_coffee = pd.read_csv(coffee_file)

    for i in range(0, len(data_coffee)):
        values_coffee = data_coffee.loc[i].tolist()

        if values_coffee[0] == choice and values_coffee[1] == "water":
            amount_water = (values_coffee[2])
        elif values_coffee[0] == choice and values_coffee[1] == "coffee":
            amount_coffee = (values_coffee[2])
        else:
            amount_milk = (values_coffee[2])

    data_resources = pd.read_csv(resources_file)

    for i in range(0, len(data_resources)):
        values_resource = data_resources.loc[i].tolist()

        if values_resource[0] == "water":
            resource_water = (values_resource[1])
        elif values_resource[0] == "coffee":
            resource_coffee = (values_resource[1])
        else:
            resource_milk = (values_resource[1])

    if amount_water > resource_water:
        print("Sorry, there is not enough water.")

    if amount_coffee > resource_coffee:
        print("Sorry, there is not enough coffee.")

    if amount_milk > resource_milk:
        print("Sorry, there is not enough milk.")

    data_cost = pd.read_csv(cost_file)

    for i in range(0, len(data_cost)):
        values_cost = data_cost.loc[i].tolist()

        if values_cost[0] == choice:
            price = (values_cost[1])

    if amount_water <= resource_water and amount_coffee <= resource_coffee \
            and amount_milk <= resource_milk:
        print(f"The price of {choice} is ${price:.2f}")
    else:
        print("One of the ingredients needs to be replenished, please "
              "replenish !")
        # TODO Schrijf code om de ingredienten weer bij te vullen

    return price


def calculate_money(cost, coin):
    '''Deze functie zorgt voor de noodzakelijke berekeningen voor het
        betalen van de koffie'''
    print("*** calculate_money() started ***")
    amount_coins_input = int(input(f"Amount of {coin[0]} (${coin[1]:.2f}): "))
    value_coins = amount_coins_input * coin[1]
    money = cost
    enough = False

    if cost - value_coins < 0:
        print(f"You paid too much. Your change is $"
              f"{(value_coins - cost):.2f}"
              f" Your {coffee_choice} is being processed, enjoy !")
        enough = True
        # TODO Schrijf code om de data_money aan te passen voor het
        #  betaalde geld
        # TODO Schrijf code om de data_resources aan te passen door het
        #  verbruik van de resources.
    elif cost - value_coins == 0:
        print(f"You paid enough."
              f" Your {coffee_choice} is being processed, enjoy!")
        enough = True
        # TODO Schrijf code om de data_money aan te passen voor het
        #  betaalde geld
        # TODO Schrijf code om de data_resources aan te passen door het
        #  verbruik van de resources.
    else:
        money = cost - value_coins
        print(f"You'll need another: ${money:.2f}")

    return money, enough


path = ("G:\Mijn Drive\GoogleMap Python\Python Udemy\Projects\Project Coffee"
        " Machine")
cost_file = f"{path}\data_cost.csv"
coffee_file = f"{path}\data_coffee.csv"
money_file = f"{path}\data_money.csv"
resources_file = f"{path}\data_resources.csv"

not_correct_answer = True
while not_correct_answer:
    answer = input(
        "What would you like? espresso/latte/cappuccino)"
        " type 'e', 'l' or 'c': ")

    if answer == "e":
        coffee_choice = "espresso"
        print("*** This wil start main_program() ***\n")
        main_program()
    elif answer == "l":
        coffee_choice = "latte"
        print("*** This wil start main_program() ***\n")
        main_program()
    elif answer == "c":
        coffee_choice = "cappuccino"
        print("*** This wil start main_program() ***\n")
        main_program()
    elif answer == "rep":
        print()
        data_resources = pd.read_csv(resources_file)

        for i in range(0, len(data_resources)):
            values = data_resources.iloc[i, [0, 1]].values.tolist()
            print(f"{values[0]} amount: {values[1]}")
        print()
        data_money = pd.read_csv(money_file)

        for i in range(0, len(data_money)):
            values = data_money.iloc[i, [0, 2]].values.tolist()
            print(f"{values[0]} amount: {values[1]}")
        print()
    elif answer == "off":
        print("*** This will end the program ***\n")
        break
    else:
        print("You didn't make a right choice !")

print("End program.")
# TODO Overweeg om code te schrijven die de output naar de terminal screen
#  verwijdert
