# list and dictionary are different
# List value will be accessed by index where dictionary values can be access by key
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}
print(programming_dictionary["Bug"])

# adding new items to dictionary
programming_dictionary["new_item"] = "New item can be added in dictionary using this method"

print(programming_dictionary)