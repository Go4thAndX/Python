# TODO Fouten nog proberen op te lossen
import random


def create_deck(num_decks=1):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♣", "♥", "♦"]
    deck = []
    for _ in range(num_decks):
        for rank in ranks:
            for suit in suits:
                card = rank + suit
                deck.append(card)
    random.shuffle(deck)
    return deck


def deal_cards(deck):
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            score += int(rank)
        elif rank in ["J", "Q", "K"]:
            score += 10
        elif rank == "A":
            aces += 1
            score += 11
    while aces > 0 and score > 21:
        score -= 10
        aces -= 1
    return score


def player_turn(deck, player_hand, dealer_hand, player_stack):
    """
    The player's turn in Blackjack.

    Parameters:
    deck (list): A list of playing cards.
    player_hand (list): A list of cards in the player's hand.
    dealer_hand (list): A list of cards in the dealer's hand.
    player_stack (int): The player's current stack.

    Returns:
    bool: True if the player chooses to stand or bust, False if the player gets Blackjack.
    """
    while calculate_score(player_hand) < 21:
        action = input("Do you want to hit or stand? ")
        if action.lower() == "hit":
            player_hand.append(deck.pop())
            print(f"Your hand: {player_hand}, score: {calculate_score(player_hand)}")
        elif action.lower() == "stand":
            return True
        else:
            print("Invalid action, try again.")
    if calculate_score(player_hand) == 21:
        print("Blackjack!")
        return False
    else:
        print(f"Busted! Your score is {calculate_score(player_hand)}.")
        return False


def dealer_turn(deck, dealer_hand):
    while calculate_score(dealer_hand) < 17:
        card = deck.pop()
        dealer_hand.append(card)
    print(f"Dealer's hand: {dealer_hand}, score: {calculate_score(dealer_hand)}")


def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    if player_score > 21:
        return "Dealer"
    elif dealer_score > 21:
        return "Player"
    elif player_score > dealer_score:
        return "Player"
    elif dealer_score > player_score:
        return "Dealer"
    else:
        return "Tie"


def play_again():
    while True:
        answer = input("Do you want to play again? (y/n) ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Invalid input, try again.")


def main():
    # Define the player's starting stack
    initial_stack = 100

    # Set the player's current stack to the starting stack
    player_stack = initial_stack

    while True:
        print("Welcome to Blackjack!")
        deck = create_deck()
        player_hand = deal_cards(deck)
        dealer_hand = deal_cards(deck)
        player_stack = int(input("Enter your beginning stack amount: "))
        while True:
            bet = int(
                input(
                    f"Enter your bet amount (you have {player_stack} in your stack): "
                )
            )
            if bet > player_stack:
                print("Invalid bet, try again.")
            else:
                player_stack -= bet
                break
        print(f"Your hand: {player_hand}, score: {calculate_score(player_hand)}")
        print(f"Dealer's hand: {dealer_hand[0]}")
        player_turn_result = player_turn(deck, player_hand, dealer_hand, player_stack)
        if player_turn_result:
            dealer_turn(deck, dealer_hand)
            # TODO Remove this line from the main() function
            # print(f"Dealer's hand: {dealer_hand}, score: {calculate_score(dealer_hand)}")
            winner = determine_winner(player_hand, dealer_hand)
            if winner == "Player":
                print("You win!")
                player_stack += 2 * bet
            elif winner == "Dealer":
                print("Dealer wins!")
            else:
                print("It's a tie!")
                player_stack += bet
        else:
            print("Game over!")
            player_stack -= bet
        if player_stack <= 0:
            print("You're out of money!")
            break
        if not play_again():
            break


# Calculate the difference between the player's starting stack and their current stack
stack_difference = player_stack - initial_stack

# Display the player's final stack and win/loss amount
if stack_difference > 0:
    print(f"You won {stack_difference} chips! Your final stack is {player_stack}.")
elif stack_difference == 0:
    print(f"You broke even. Your final stack is {player_stack}.")
else:
    print(f"You lost {-stack_difference} chips. Your final stack is {player_stack}.")


if __name__ == "__main__":
    main()
