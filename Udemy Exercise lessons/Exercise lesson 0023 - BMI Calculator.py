# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
float_height = float(height)
float_weight = float(weight)
bmi = float_weight / float_height ** 2

# The round() function in Python is used to round a number to a specified number of digits. Examples:
# round(5.6) returns 6
# round(12.45, 1) returns 12.5
# round(2.567, 2) returns 2.57
round_bmi = round(bmi)
print(round_bmi)