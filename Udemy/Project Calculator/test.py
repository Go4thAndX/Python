first_char = input("We are going to make a string, type the first character: ")
string = first_char

while True:
    print(f'The string we made until now: "{string}"')
    execute = input(
        f'Do you want to give the string "{string}" more characters ? ("yes" or "no"): '
    )
    if execute == "yes":
        next_char = input("Type the next character: ")
        string = string + next_char
    elif execute == "no":
        print(f'\nThe final string is "{string}" the program has ended.\n')
        exit()
    else:
        print('\nYou didn\'t answer with "yes" or "no": \n')
    continue
