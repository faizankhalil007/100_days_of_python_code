# create love calculator
# in this exercise we will use 2 new functions, (1) count() to count the number of letters (2) lower() to convert string to lower
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both_name = name1 + name2
both_name = both_name.lower()
love_counts = true_counts = int(0)
love_counts += both_name.count("l")
love_counts += both_name.count("o")
love_counts += both_name.count("v")
love_counts += both_name.count("e")
true_counts += both_name.count("t")
true_counts += both_name.count("r")
true_counts += both_name.count("u")
true_counts += both_name.count("e")
final_score = str(true_counts) + str(love_counts)
if final_score < "10" or final_score > "90":
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif "40" < final_score < "50":
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}")