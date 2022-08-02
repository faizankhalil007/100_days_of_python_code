# in this file we will discuss different data types

# print a string part from specific position
my_name = "Faizan"
print(my_name[4])

# integer
# as we separate the thousand or hundred with "," in Python we can do this with "_" and interprater will digonse and remove the "_"
first_number = 124_786_90
print(first_number)
# float
first_float = 3.45
print(first_float)

# Boolean
True
False
# to find the data type of variable
# can print as many statements as many you want with single print statement
print(type(first_number),type(my_name),type(first_float))

# string concat to string only not with integer like the code below will through a error
name_length = len(input("What is your name?\n"))
# for type casting use this code, to check the error simply remove str() from print statement
print("Your name has "+str(name_length)+" characters")
# waht happen when we use this
print(100 + float("70.5"))