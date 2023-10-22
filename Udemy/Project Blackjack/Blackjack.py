# TODO code schrijven die reageert op het niet intypen van een 'y' of een 'n' bij de vraag of de user nog een kaart wil
# TODO de code aanpassen zodat het programma nogmaals uitgevoerd kan worden als de gebruiker dat wil
# TODO code schrijven die er voor zorgt dat de terminal ieder keer ververst wordt als we een nieuw spel beginnen.

import random
import time


def deal_card():
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards_list)
    return random_card


print_string_1 = "Your cards    : "
print_string_2 = "Your current score: "
print_string_3 = "Computer cards: "
print_string_4 = "Computer current score: "

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = sum(user_cards)
computer_score = sum(computer_cards)

if computer_score == 21:
    print(print_string_1, user_cards, print_string_2, user_score)
    print(print_string_3, computer_cards, print_string_4, computer_score)
    print("\nComputer has Blackjack and wins\n")
    exit()
elif user_score == 21:
    print(print_string_1, user_cards, print_string_2, user_score)
    print(print_string_3, computer_cards, print_string_4, computer_score)
    print("\nYou have Blackjack and win\n")
    exit()

if user_cards[0] == 11 and user_cards[1] == 11:
    user_cards[0] = 1
    user_score -= 10

if computer_cards[0] == 11 and computer_cards[1] == 11:
    computer_cards[0] = 1
    computer_score -= 10

# TODO Deze code moet verwijdert worden na het testen
print(
    f"user    : {user_cards}, {user_score}\ncomputer: {computer_cards}, {computer_score}\n"
)
print(print_string_1, user_cards, print_string_2, user_score)
print(print_string_3, computer_cards[0])

card_user = True

while card_user:
    answer = input("Type 'y' to get another card, type 'n' to pass: ")

    if answer == "y":
        user_cards.append(deal_card())
        user_score = sum(user_cards)

        if user_score > 21 and 11 in user_cards:
            card_index = user_cards.index(11)
            user_cards[card_index] = 1
            user_score -= 10

        if user_score > 21:
            print(print_string_1, user_cards, print_string_2, user_score)
            print(print_string_3, computer_cards, print_string_4, computer_score)
            print("\nYour score exeeds 21, computer wins")
            exit()

        print(print_string_1, user_cards, print_string_2, user_score)
    elif answer == "n":
        card_user = False
    else:
        print('\nYou didn\'t answer with "y" or "n": \n')
    continue

print(print_string_3, computer_cards, print_string_4, computer_score)
card_computer = True

while card_computer:
    if computer_score <= 16:
        print("Computer takes an other card")
        computer_cards.append(deal_card())
        computer_score = sum(computer_cards)

        if computer_score > 21 and 11 in computer_cards:
            card_index = computer_cards.index(11)
            computer_cards[card_index] = 1
            computer_score -= 10

        if computer_score > 21:
            print(print_string_3, computer_cards, print_string_4, computer_score)
            print("\nComputer score exeeds 21, you win")
            exit()

        print("Be patient while the computer takes an other card")
        time.sleep(2)
        print(print_string_3, computer_cards, print_string_4, computer_score)

    else:
        if computer_score <= 16:
            print(print_string_3, computer_cards, print_string_4, computer_score)
        card_computer = False

print("Your final score: ", user_score)
if user_score < computer_score:
    print("\nComputer wins\n")
elif user_score > computer_score:
    print("\nYou win\n")
else:
    print("\nIt's a draw\n")
