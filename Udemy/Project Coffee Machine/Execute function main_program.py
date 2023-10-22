def main_program():
    print("main_program executed.")


def generate_report():
    print("generate_report executed.")


not_correct_answer = True
while not_correct_answer:
    answer = input("Type 'e', 'l' or 'c': ")

    if answer == "e":
        correct_answer = False
        print("This wil start main_program().")
        main_program()
    elif answer == "l":
        correct_answer = False
        print("This wil start main_program().")
        main_program()
    elif answer == "c":
        correct_answer = False
        print("This wil start main_program().")
        main_program()
    elif answer == "rep":
        correct_answer = False
        print("This wil start generate_report().")
        generate_report()
        main_program()
    elif answer == "off":
        print("This will end the program.")
        break
    else:
        print("You didn't type a correct answer !")

print("End program.")

