# Write a program that switches the values stored in the variables a and b.
a = input("value of a: ")
b = input("value of b: ")

print("value of a is: "+a+"\n value of b is: "+b)
c = a
a = b
b = c

print("Manipulated value of a is: "+a+"\n Manipulated value of b is: "+b)