# Main file of the Guess The Number project
import random

another_game = True

while another_game:

    import art
    print(art.logo)

    random_num = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type easy or hard ('e' or 'h'): ")
    if level == "e":
        attempts = 10
    else:
        attempts = 5

    guess_again = True
    while guess_again:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == random_num:
            print(f"You got it!" )
            guess_again = False
        elif guess < random_num:
            if attempts == 1:
                print("Too low.")
            else:
                print("Too low. \nGuess again")
        else:
            if attempts == 1:
                print("Too high.")
            else:
                print("Too high. \nGuess again")

        attempts -= 1
        if attempts < 1:
            print("You've run out of guesses, you lose.")
            guess_again = False

    answer = input("Do you want to play another game 'yes' or 'no' (y or n) ?: ")
    if answer != "y":
        another_game = False
