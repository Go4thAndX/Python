# Kun je voor mij Python code schrijven die het meest gangbare spel Blackjack simuleert zoals het in casino's gespeeld wordt waarbij ik speel tegen de computer,
# De player krijgt een beginstack van $ 100 en mag daarvan maximaal $ 10 per ronde inzetten.
# Als de player geen geld meer heeft is het einde spel.
# Aan het eind van iedere ronde mag de speler verder spelen of besluiten te stoppen.
# Als de player geen geld meer heeft is het einde spel.
# Zowel de player als de dealer krijgen aan het begin van het spel 2 kaarten, de kaarten en de handwaarde van de player worden beiden getoond maar van de dealer wordt alleen de eerste kaart getoond maar niet de handwaarde.
# De dealer heeft Blackjack als zijn eerst twee kaarten samen een waarde van 21 hebben of 2 Azen zijn en dan heeft de dealer gewonnen, de player heeft pas Blackjack als zijn eerste twee kaarten samen een waarde van 21 hebben of 2 Azen zijn met als voorwaarde dat de dealer geen Blackjack heeft met zijn eerste twee kaarten.
# De player mag kiezen of hij na de eerste 2 kaarten nog meer kaarten wil nemen of wil passen, waarbij voor de player geldt dat als zijn kaartwaarde boven de 21 uitkomt hij heeft verloren, behalve als hij een of meerdere azen heeft want dan verandert de kaartwaarde van 1 aanwezige Aas van 11 naar 1, waarbij als er meer zen zijn eerst de waarde van de laatste aanwezige aas veranderd naar 1, waarna weer gekeken moet worden of het totaal van zijn kaarten boven de 21 uitkomt waarna pas de volgende aanwezig aas van waarde mag veranderen.
# Als de player nog meer kaarten neemt moet na elke kaart de volledige kaarthand en de handwaarde getoond worden.
# Tussen elke gegeven kaart zit een tijdsvertraging van 2 sec.
# Als de player uitgespeeld is wordt gekeken of de dealer nog kaarten moet nemen, waarbij ook voor de dealer geldt dat als zijn kaartwaarde boven de 21 uitkomt hij heeft verloren, behalve als hij een of meerdere azen heeft want dan verandert de kaartwaarde van 1 aanwezige Aas van 11 naar 1, waarbij als er meer zen zijn eerst de waarde van de laatste aanwezige aas veranderd naar 1, waarna weer gekeken moet worden of het totaal van zijn kaarten boven de 21 uitkomt waarna pas de volgende aanwezig aas van waarde mag veranderen.
# Aan het einde van elke speelronde moet mijn begin stack en het verlies of de winst aangegeven worden.

import time
import random


# functie voor het maken van een kaartendeck
def create_deck():
    deck = []
    # Hier worden Unicode-codepunten gebruikt om de vier kaartsymbolen weer te geven:

    # Harten: \u2665
    # Ruiten: \u2666
    # Klaveren: \u2663
    # Schoppen: \u2660
    # Deze symbolen zullen worden weergegeven in plaats van de tekstuele representaties van de kaarten in de deck lijst.
    suits = ["\u2665", "\u2666", "\u2663", "\u2660"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    random.shuffle(deck)
    return deck


# functie voor het berekenen van de waarde van de kaarten in de hand
def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card = card[0] + " " + card[1]
        if card[0] in ["K", "Q", "J", "T"]:
            value += 10
        elif card[0] == "A":
            aces += 1
            value += 11
        else:
            value += int(card.split()[0])
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    return value


# functie voor het tonen van kaarten en handwaarde van de speler en dealer
def show_cards(player, dealer, show_all=False):
    print("Dealer's hand: ", end="")
    if show_all:
        for card in dealer:
            print(card, end=" ")
        print("Hand value:", hand_value(dealer), end=" ")
    else:
        print(dealer[0], end=" ")
        print("Hand value:", hand_value([dealer[0]]), end=" ")
    print("\nPlayer's hand: ", end="")
    for card in player:
        print(card, end=" ")
    print("Hand value:", hand_value(player))


# functie voor het bepalen van het resultaat
def determine_winner(player_hand, dealer_hand):
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    if player_value > 21:
        return "Player Busts"
    elif dealer_value > 21:
        return "Dealer Busts"
    elif player_value == 21 and len(player_hand) == 2:
        return "Player Blackjack"
    elif dealer_value == 21 and len(dealer_hand) == 2:
        return "Dealer Blackjack"
    elif player_value > dealer_value:
        return "Player Wins"
    elif dealer_value > player_value:
        return "Dealer Wins"
    else:
        return "Push"


# functie voor het spelen van een ronde
def play_round(player_stack):
    print("\nStarting a new round")
    player_hand = []
    dealer_hand = []
    deck = create_deck()

    # beide spelers krijgen twee kaarten
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    show_cards(player_hand, dealer_hand)

    # player's beurt
    while True:
        choice = input("Do you want to hit or stand ? (h or s) ")
        if choice.lower() == "h":
            player_hand.append(deck.pop())
            show_cards(player_hand, dealer_hand)
            if hand_value(player_hand) > 21:
                print("Player Busts")
                return -10
        else:
            break

    # dealer's beurt
    print("Dealer's turn:")
    show_cards(player_hand, dealer_hand, True)  # toon dealer's hand en handwaarde
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        time.sleep(2)
        show_cards(player_hand, dealer_hand, True)

    result = determine_winner(player_hand, dealer_hand)
    print(result)

    # berekenen van het resultaat
    if result == "Player Busts" or result == "Dealer Wins":
        player_stack -= 10
    elif (
        result == "Dealer Busts"
        or result == "Player Wins"
        or result == "Player Blackjack"
    ):
        player_stack += 10
    else:
        player_stack += 0

    print("Player Stack: $" + str(player_stack))

    if player_stack == 0:
        print("Game over. You are out of money.")
    else:
        again = input("Do you want to play another round yes or no ? (y or n) ")
        if again.lower() == "y":
            play_round(player_stack)
        else:
            print("Thanks for playing. Goodbye!")


# Dit initialiseert de speler_stack op 100 en start de eerste ronde van het spel door de functie play_round aan te roepen met de parameter player_stack.
player_stack = 100
play_round(player_stack)
