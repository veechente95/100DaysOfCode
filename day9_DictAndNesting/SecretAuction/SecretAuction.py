# create a dict - person name is the key and bid is the value
# loop through dict and see who has the highest bid

from AuctionArt import logo

print(logo)
print("Welcome to the Secret Auction!")

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    # bidding_record = {"Vicente": 123, "Jojo": 321}
    for key_bidder in bidding_record:
        bid_amount = bidding_record[key_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key_bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = str(input("Please enter your name: "))
    price = int(input("Please enter your bidding price: $"))
    bids[name] = price  # assigning key and value
    want_continue = str(input("Are there any other bidders? Type 'yes' or 'no': ")).lower()
    if want_continue == "no":
        bidding_finished == True
        highest_bidder(bids)
        break

