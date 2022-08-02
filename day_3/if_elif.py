# in this file we took a example
# a ticket shop has different rates for different age groups, show the price according to age group
customer_height = input("Please enter your height in CM: \n")
customer_age = input("Please enter your ag: \n")
if customer_height > '120':
    if customer_age <= '12':
        print("Please pay 7$")
    elif '12' < customer_age <= '18':
        print("Please pay 10$")
    else:
        print("Please pay 15$")
else:
    print("You are not allowed to ride")