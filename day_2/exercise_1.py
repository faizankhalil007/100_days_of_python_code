# Write a program that adds the digits in a 2 digit number
# . e.g. if the input was 35,
# then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
# we again need to change the data type from string to integer so we can add the number
digit_1 = int(two_digit_number[0])
digit_2 = int(two_digit_number[1])
print(digit_1 + digit_2)