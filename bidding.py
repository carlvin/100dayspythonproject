art = '''  
      /(  ___________
     |  >:===========`
      )( 
'''
print(art)

# all_bids = {}
bidding = True
highest_bid = 0


def bidder(name_of_bidder, bid_placed):
    bidders = {'name': name_of_bidder, 'bid': bid_placed}
    return bidders


# all_bids.append(bidders)

winner = ""


def highest_bidder(bids_placed):
    for bidders in bids_placed:
        global winner,highest_bid
        winner = bids_placed[bidders]
        bid_amt = bids_placed[bidders]
        if bid_amt > highest_bid:
            highest_bid = bid_amt


while bidding:

    name = input("Enter you name: \n")
    bid = input("Place your bid amount: \n")

    all_bids = bidder(name, bid)
    highest_bidder(all_bids)
    others = input("are there other bidders ?, type yes or no \n")
    if others == "no":
        bidding = False
    # clear()
print(f'{winner} won: {highest_bid}')
