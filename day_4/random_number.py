# In this exercise we will learn how to generate the random number
# first we need to import the random module
# information about random module https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
import random
random_integer = random.randint(1, 999)
print(f"this is random integer number {random_integer}")
random_float = random.random()
print(f"this is random float number {random_float}")
# 3 will be any value which you want to use
random_decimal = random.random() * 3
print(f"this is random decimal number {random_decimal}")
