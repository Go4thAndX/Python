# Calculator


# Add function()
def add_function(number_first, number_next):
    return number_first + number_next


# Subtract function()
def subtract_function(number_first, number_next):
    return number_first - number_next


# Multiply function()
def multiply_function(number_first, number_next):
    return number_first * number_next


# Divide function()
def divide_function(number_first, number_next):
    return number_first / number_next


operations_dict = {
    "+": add_function,
    "-": subtract_function,
    "*": multiply_function,
    "/": divide_function,
}


def calculator():
    number_first = float(input("What is the first number of the calculation ?:  "))

    should_continue = True
    while should_continue:
        # for key in operations_dict:
        print("\n+ - * /\n")
        operation_symbol = input("Pick an operation from the line above: ")
        number_next = float(input("What is the next number of the calculation ?: "))
        answer = operations_dict[operation_symbol](number_first, number_next)
        print(
            f"The answer of the calculation {number_first} {operation_symbol} {number_next} = {answer}"
        )
        execute = input(
            f"Do you want to perform another calculation with {answer} ? ('y(es)' or 'n(o)'): "
        )
        if execute == "y" or execute == "yes":
            number_first = answer

        else:
            should_continue = False
            calculator()
    print("The program has ended.")


calculator()
