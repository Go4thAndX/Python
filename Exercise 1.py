'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out
the year (and therefore be out of date the next year).

Extras:

Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
'''

user_name = input("What is your name ? ")
user_age = input("What is your age ? ")
user_age_int = int(user_age)
number = input("Please pick a number between 0 and 10 ? ")
number_int = int(number)
year_now = 2023
year_age_hundred = year_now - user_age_int + 100
message = (
    f"Hello {user_name} in the year {year_age_hundred} you will become 100 years old !!!\n")
print(message)
for i in range(number_int):
    print(message)
