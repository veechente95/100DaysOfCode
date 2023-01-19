bids = {}
bidding_finished = False


def highest_bidder(biding_record):
    highest_bid = 0
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")


while not bidding_finished:
    name = str(input("What is your name: "))
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = str(input("Bid again? Select 'yes' or 'no': ")).lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
