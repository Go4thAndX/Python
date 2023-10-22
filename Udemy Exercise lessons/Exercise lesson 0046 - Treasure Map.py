# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis).
# print(position)
# print(type(position))
position_col = int(position[0])
position_row = int(position[1])
# print(position_col, position_row)
# print(type(position_col), type(position_row))
map[position_row - 1][position_col - 1] ="X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

