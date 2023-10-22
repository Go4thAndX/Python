# draw any polygon in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the no of the sides of the polygon
number_of_sides = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
length_of_sides = int(input("Enter the length of the sides of the polygon : "))


for _ in range(number_of_sides):
    turtle.forward(length_of_sides)
    turtle.right(360 / number_of_sides)

turtle.mainloop()
