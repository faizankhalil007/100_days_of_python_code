# In this exercise we will find if the curent year is leap or not
year = int(input("Which year do you want to check? "))
division_4 = int(year % 4)
division_100 = int(year % 100)
division_400 = int(year % 400)
if (division_400 == 0) or (division_100 != 0) and (division_4 == 0):
    print("Leap year.")
else:
    print("Not leap year.")
print(f"this is division4 {division_4} /n this is division100 {division_100} /n and this is divison400 {division_400}")