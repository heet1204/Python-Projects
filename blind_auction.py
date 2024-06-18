bidders_data = {}
is_continue = True


def highest_bid(bidding_records):
  highest_bid = 0
  for bidder in bidding_records:
    bid_amount = bidding_records[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} has the highest bid of {highest_bid}$")


while is_continue:
  name = input("\nEnter the bidder's Name : ").upper()
  bid_amount = int(input("Enter the bid price in $ : "))
  bidders_data[name] = bid_amount

  result = input(
      "\nType 'Yes'if any other used wants to bid or 'No' to exit: ").lower()
  if result == "yes" or result == "no":
    if result == "no":
      is_continue = False
      highest_bid(bidders_data)
  else:
    print("\nInvalid Selection")
    break
