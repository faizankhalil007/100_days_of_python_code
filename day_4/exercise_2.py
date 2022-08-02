# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
list_length = len(names)
to_pay = random.randint(0, list_length - 1)
payer_name = names[to_pay]
print(f"{payer_name} is going to buy the meal today!")