# # In deze functie is strings_dict de dictionary met de strings en hun bijbehorende nummers, het nummer is het nummer van de string die je wilt kiezen. De functie retourneert de string die overeenkomt met dit nummer. Hieronder vind je een voorbeeld van hoe je dit kunt doen:


def kies_string(strings_dict, nummer):
    gekozen_string = strings_dict[nummer]
    return gekozen_string


user_cards = ["A", "A"]
user_score = 22
computer_cards = [10]
computer_score = 10

# Om de functie te gebruiken, maak je een dictionary aan met de strings en hun nummers en geef je deze samen met het gewenste nummer als argumenten mee aan de functie:
strings_dict = {
    1: (f"Your cards    : {user_cards}, Your current score: {user_score}"),
    2: (f"Computer cards: {computer_cards[0]}"),
    3: (f"Computer cards: {computer_cards}, Computers current score: {computer_score}"),
    4: ("\nComputer has Blackjack and wins\n"),
    5: ("\nYou have Blackjack and win\n"),
    6: ("\nComputer wins"),
    7: ("\nYou win"),
    8: ("\nIt's a draw"),
}

# Dit zal de string selecteren met het nummer 3 uit de dictionary strings_dict en deze printen. In dit voorbeeld wordt de string 'string 3' geselecteerd, omdat dit de string is met het nummer 3 in de dictionary. Je kunt het nummer aanpassen om een andere string uit de dictionary te selecteren.
nummer_van_te_kiezen_string = 1
gekozen_string = kies_string(strings_dict, nummer_van_te_kiezen_string)
print(gekozen_string)
