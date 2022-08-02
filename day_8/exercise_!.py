# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print('Hello')
#     print('How do you do?')
#     print("Isn't the weather nice today?")
# greet()

# function that allows the input or parameter
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name} ?")
# greet_with_name("Faizan")

# function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with("Faizan", "Lahore")
greet_with(location="Islamabad", name="Ahsan")