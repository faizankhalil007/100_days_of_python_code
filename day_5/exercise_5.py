#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for characters in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for pass_numbers in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
for pass_symb in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
print(f"This will be your password {password}")
# Hard level
password_list = []
password_length = len(password_list)
difficult_password = ""
for diff_characters in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for diff_pass_numbers in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
for diff_pass_symb in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
for dif_pass in password_list:
    difficult_password += dif_pass
print(f"This will be the strong password: {difficult_password}")