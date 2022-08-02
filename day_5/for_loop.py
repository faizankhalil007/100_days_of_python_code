# on day 5 we will learn the loops
# start with for loop
fruits = ["Apple", "Peach", "Banana"]
for fruit in fruits:
    print(fruit)
sum_number = 0
for number in range(1, 101):
    sum_number += number
print(f"thi is the sum {sum_number}")
# to skip some values
# 3 will skip the 3 numbers
for new_number in range(1, 101, 3):
    print(f"thi is the numbers {new_number}")