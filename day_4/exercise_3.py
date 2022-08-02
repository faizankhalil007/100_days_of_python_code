# treasure map
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
#
# https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5
#
# First your program must take the user input and convert it to a usable format.
#
# Next, you need to use it to update your nested list with an "x".

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter two digit number")
horizontal = position[0]
vertical = position[1]
map[int(vertical) - 1][int(horizontal) - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")