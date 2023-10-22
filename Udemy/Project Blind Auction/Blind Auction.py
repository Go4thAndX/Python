import os


# clear console function
def clear():
    os.system("cls" if os.name == "nt" else "clear")


from art import logo

print(logo)


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"name one": 123, "name two": 456}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(all_bids_dict)


all_bids_dict = {}
other_user = True
while other_user:
    input_name = input("What is your name ?: ")
    input_bid = int(input("What is your bid ?: $"))
    all_bids_dict[input_name] = input_bid
    input_other = input("Are there any other bidders? Type 'yes' or 'no': \n")

    if input_other != "yes":
        other_user = False
        find_highest_bid(bidding_record=all_bids_dict)
    else:
        clear()
