# Project Higher Lower

# TODO Kijken of een deel van de code nog vereenvoudigd kan worden.
# TODO Er mogen random geen gelijke items gekozen worden.

import random

from game_data import data
from art import logo, vs


def get_random_item():
    item = random.choice(data)
    return item


score = 0
change_second = False
answer_right = True

while answer_right:
    if change_second:
        print(logo)
        print(
            f"Compare first: {first_item['name']}, a {first_item['description']}, from {first_item['country']}."
        )

        # answer_equal = True

        # while answer_equal:
        second_item = {}
        second_item = get_random_item()
        # if first_item != second_item:
        #     answer_equal = False
        print(vs)
        print(
            f"Against second: {second_item['name']}, a {second_item['description']}, from {second_item['country']}."
        )
    else:
        first_item = {}
        first_item = get_random_item()
        print(logo)
        print(
            f"Compare first: {first_item['name']}, a {first_item['description']}, from {first_item['country']}."
        )

        # answer_equal = True

        # while answer_equal:
        second_item = {}
        second_item = get_random_item()
        # if first_item != second_item:
        #     answer_equal = False
        print(vs)
        print(
            f"Against second: {second_item['name']}, a {second_item['description']}, from {second_item['country']}."
        )

    answer = True
    while answer:
        answer_more = input("Who has more followers ? Type first 'F' or second 'S': ")
        uppercase_answer_more = answer_more.upper()
        if uppercase_answer_more == "F" or uppercase_answer_more == "S":
            answer = False
        else:
            print("You didn't answer with 'F' or 'S'")

    if (
        first_item["follower_count"] > second_item["follower_count"]
        and uppercase_answer_more == "F"
    ):
        change_second = True
        score += 1
        print(f"You're right ! Current score: {score}")
    elif (
        first_item["follower_count"] > second_item["follower_count"]
        and uppercase_answer_more == "S"
    ):
        print(f"Sorry, that's wrong. Final score: {score}")
        answer_right = False
    elif (
        first_item["follower_count"] < second_item["follower_count"]
        and uppercase_answer_more == "F"
    ):
        print(f"Sorry, that's wrong. Final score: {score}")
        answer_right = False
    elif (
        first_item["follower_count"] < second_item["follower_count"]
        and uppercase_answer_more == "S"
    ):
        change_second = True
        score += 1
        print(f"You're right ! Current score: {score}")
        first_item = second_item
    else:
        print()
