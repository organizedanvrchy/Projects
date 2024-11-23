import time
import logo
import os

auction_dict = {}

print(logo.logo)

bidders = True
while(bidders):
    name = input("Enter your name: ")
    
    try:
        bid = float(input("Enter your bid: "))
    except ValueError: 
        print("Invalid Bid. Please enter a number.")
        continue

    # Add bidder's name and bid to dictionary
    auction_dict[name] = bid

    other_bidders = input("Are there any other bidders? Y or N: ").lower()
    if other_bidders == "y":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        winning_name = max(auction_dict, key=auction_dict.get)
        winning_bid = auction_dict[winning_name]

        os.system("cls" if os.name == "nt" else "clear")
        print(f"The winner is {winning_name} with a bid of {winning_bid}!")
        time.sleep(2)
        bidders = False
