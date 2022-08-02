# in this exercise we will use multipule conditions to create a bill
# flow chart link https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload
print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))
age = int(input("What is your age? "))
total_bill = 0
if height >= 120:
    if age < 12:
        total_bill = int(5)
    elif age <=18:
        total_bill = int(7)
    else:
        total_bill = 12
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y" or want_photo == "y":
        total_bill += 3
        print(f"Your final bill is ${total_bill}")
    else:
        print(f"Your final bill is ${total_bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")