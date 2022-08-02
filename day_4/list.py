# we will learn about "LIST"
# list can be stored same as variables but right side will be different
# list start with "[" and end with "]"

states_in_pakistan = ["punjab", "sindh", "kpk", "balochistan", "GB", "AJK"]
print(states_in_pakistan[2])
# negative index will start from end
print(states_in_pakistan[-1])
# to update the data
states_in_pakistan[2] = "KPK"
print(states_in_pakistan[2])
#  to add new value in list use append()
states_in_pakistan.append("Delhi")
print(states_in_pakistan)
for i in states_in_pakistan:
    print(i)