# this exercise is to create the TIP Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay (150.00 / 5) * 1.12 = 33.6
#
# Format the result to 2 decimal places = 33.60
#
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15: "))
total_persons = int(input("How many people to split the bill?: "))
tip_amount = total_bill * (tip_percentage / 100)
each_person_bill = (total_bill + tip_amount) / total_persons
# a function alternative of round to make round figure
each_person_bill = "{:.2f}".format(each_person_bill)
# each_person_bill = round(each_person_bill, 2)
print(f"Each person should pay: ${each_person_bill}")
