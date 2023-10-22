import pandas as pd


def choose_coffee(choice):
    print("*** choose_coffee() started ***")
    data_coffee = pd.read_csv(coffee_file)
    data_resources = pd.read_csv(resources_file)
    for i in range(0, len(data_coffee)):
        values = data_coffee.loc[i].tolist()

        if values[0] == choice:
            value_amount = (values[2])
            print(value_amount)


    #
    # print(data_coffee)
    # ingredient = (data_file.loc[i, "Ingredient"])
    # # ingredients = MENU[choice]["ingredients"]
    # resources_water = True
    # resources_milk = True
    # resources_coffee = True
    #
    # if ingredients.get("water"):
    #
    #     if resources["water"] < MENU[choice]["ingredients"]["water"]:
    #         print("Sorry, there is not enough water.")
    #         resources_water = False
    #     else:
    #         print("There is enough water")

path = ("G:\Mijn Drive\GoogleMap Python\Python Udemy\Projects\Project Coffee"
       " Machine")
coffee_file = f"{path}\data_coffee.csv"
resources_file = f"{path}\data_resources.csv"
choose_coffee(choice="espresso")