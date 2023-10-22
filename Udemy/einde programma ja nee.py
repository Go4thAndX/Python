first_char = input("We are going to make a string, type the first character: ")
string = first_char

while True:
    print(f'The string we made until now: "{string}"')
    execute = input(
        f'Do you want to give the string "{string}" more characters ? ("y" or "n"): '
    )
    if execute == "y":
        next_char = input("Type the next character: ")
        string = string + next_char
    elif execute == "n":
        print(f'\nThe final string is "{string}" the program has ended.\n')
        exit()
    else:
        print('\nYou didn\'t answer with "y" or "n"\n')
    continue
