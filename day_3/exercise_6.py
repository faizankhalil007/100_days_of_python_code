# create pizza ordering system
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = pepperoni_price = total_price = int(0)
if size == "S" or size == "M" or size == "L":
    if size == "S":
        price = int(15)
        pepperoni_price = int(2)
    elif size == "M":
        price = int(20)
        pepperoni_price = int(3)
    elif size == "L":
        price = int(25)
        pepperoni_price = int(3)
    if add_pepperoni == "Y":
        price += pepperoni_price
    if extra_cheese == "Y":
        price += 1

    print(f"Your final bill is: ${price}")
else:
    print("Try next time")
