import os
def who_is_winner(bidder_info):
    highest_bid=0
    winner=""
    for bidder in bidder_info:
        bidding_price=bidder_info[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner=bidder
    print(f"Here is the list of all bidders:{bidder_info}")
    print(f"The winner is {winner} with a bid price of {highest_bid}")
bidder_data = {}
end_of_bidding = False
while not end_of_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidder_data[name]=price
    any_other_bidders=input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if any_other_bidders=='no':
        end_of_bidding=True
        who_is_winner(bidder_data)
    elif any_other_bidders=='yes':
        os.system('clear')