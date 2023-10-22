"""
Instructions:
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a nonforleap year. A leap year has 29 days in February.

Hint:
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]
"""
import re


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 1:
        return 29
    else:
        return month_days[month]


# The [is_valid_year] function checks if the input consists of 4 digits and does not contain any other characters. The while loop keeps prompting the user to enter a year until a valid year is entered. Then the user is asked if they want to continue with the program. If the input is not valid, the program keeps asking for a valid input until one is given. If the user enters "no", the program is stopped using the exit() function. If the user enters "yes", the while loop is repeated and the user is asked to enter a year again. Once a valid year is entered, the program is terminated and the message "The execution of the programa has ended." is printed.

# The [import re] statement is used to import the Python library re, which stands for Regular Expression. The re module is used for working with regular expressions in Python. Regular expressions are a sequence of characters that define a search pattern. The re module provides a set of functions that can be used to manipulate strings based on regular expressions.


# Check if the input is a valid year
def is_valid_year(year):
    if re.match(r"^\d{4}$", str(year)):
        return True
    else:
        return False


print(
    "This program gives the number of days of the month for a given year and month accounting for leap years.\n"
)
# TODO Kijken of ik van de onderstaande code kan vervangen door een functie
while True:
    year = input("Enter a year: ")
    if is_valid_year(year):
        break
    else:
        print("Invalid input !")
        while True:
            execute = input(
                "Do you want to continue with the execution of the program by entering a valid year ? ('yes' or 'no'): "
            )
            if execute == "yes":
                break
            elif execute == "no":
                print("Execution of the program stopped.")
                exit()
            else:
                print("Invalid input ! Enter 'yes' or 'no': ")
            continue

month_dict = {
    "Jan": 0,
    "Feb": 1,
    "Mar": 2,
    "Apr": 3,
    "May": 4,
    "Jun": 5,
    "Jul": 6,
    "Aug": 7,
    "Sep": 8,
    "Oct": 9,
    "Nov": 10,
    "Dec": 11,
}

while True:
    print(
        "\nJan for January; Feb for February; Mar for March\nApr for April; May for May; Jun for June\nJul for July; Aug for August; Sep for September\nOct for October; Nov for November; Dec for December\n"
    )
    month_abr = input("Enter an abreviation for the month listed above: ")
    # Looking for the value for the key month_abr
    month = month_dict.get(month_abr)
    if month != None:
        break
    else:
        print("Invalid input !")
        while True:
            execute = input(
                "Do you want to continue with the execution of the program by entering a valid abreviation for the month ? ('yes' or 'no'): "
            )
            if execute == "yes":
                break
            elif execute == "no":
                print("Execution of the program stopped.")
                exit()
            else:
                print("Invalid input ! Enter 'yes' or 'no': ")
            continue

days = days_in_month(int(year), month)
print(
    f"\nThe month {month_abr} of the year {year} has {days} days\n\nThe execution of the program has ended."
)
