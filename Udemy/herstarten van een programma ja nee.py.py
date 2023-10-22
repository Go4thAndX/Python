def deel_1():
    print("Hier start deel 1 van mijn programma.")
    start_program = True

    while start_program:
        start = input("Do you want to make a string ? ('y' or 'n'): ")
        if start == "y":
            first_string = (
                deel_2()
            )  # Voer deel 2 van het programma uit en bewaar het resultaat
            print(
                f"\nThe final string is {first_string}\n"
            )  # Gebruik het resultaat van deel 2 in deel 1

            while True:
                another_string = input(
                    "Do you want to make another string ? ('y' or 'n'): "
                )
                if another_string == "y":
                    next_string = deel_2()
                    print(f"\nThe final string is {next_string}\n")
                elif another_string == "n":
                    print("The program ended without making any more strings.\n")
                    exit()
                else:
                    continue
        elif start == "n":
            print("The program ended without making a string.\n")
            exit()
        else:
            continue


def deel_2():
    print("Hier start deel 2 van mijn programma.")
    first_char = input("We are going to make a string, type the first character: ")
    string = first_char

    make_string = True

    while make_string:
        print(f"The string we made until now: '{string}'")
        execute = input(
            f"Do you want to give the string '{string}' more characters ? ('y' or 'n'): "
        )
        if execute == "y":
            next_char = input("Type the next character: ")
            string = string + next_char
        elif execute == "n":
            return string  # Geef het uiteindelijke resultaat terug aan de functie die deel_2() heeft opgeroepen
        else:
            print("\nYou didn't answer with 'y' or 'n'\n")
        continue


deel_1()  # Voer deel 1 van het programma uit
