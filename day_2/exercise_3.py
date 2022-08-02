# life in weeks
#  create a program which takes input from the user as current age and assume the end age will be 90 years
# now convert the remaining years into days, weeks and months
age = input("What is your current age?")
end_age = 90
# create the difference
age_difference_in_years = end_age - int(age)
# calculate months
remaining_months = age_difference_in_years * 12
# remaining weeks
remaining_weeks = age_difference_in_years * 52
# remaining days
remaining_days = age_difference_in_years * 365
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")