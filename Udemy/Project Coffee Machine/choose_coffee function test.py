import pandas as pd


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


path = ("G:\Mijn Drive\GoogleMap Python\Python Udemy\Projects\Project Coffee"
       " Machine")
coffee_file = f"{path}\data_coffee.csv"
resources_file = f"{path}\data_resources.csv"
choose_coffee(choice="espresso")