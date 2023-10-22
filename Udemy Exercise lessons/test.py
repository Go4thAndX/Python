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
        "Jan for January, Feb for February, Mar for March, Apr for April, May for May, Jun for June, Jul for July, Aug for August, Sep for September, Oct for October, Nov for November and Dec for December"
    )
    month_abr = input("Enter an abreviation for the month : ")
    # Looking for the value for the month key
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
print(month)
