from replit import clear

# HINT: You can call clear() to clear the output in the console.
another_bidder = True
bid_dictionary = {}


def bidd_inputs():
    name = input("What is your name?")
    bid_price = input("What is your price?")
    want_other_bidd = input("Want to make another bidd, Type Yes to place and No to end").lower()
    bid_dictionary = {
        "name": name,
        "bid_price": bid_price,
    }
    return want_other_bidd


while another_bidder:
    if bidd_inputs() == "true":
        clear()
        bidd_inputs()
    else:
        another_bidder = False

print(bid_dictionary)