# draw Square in Python Turtle
import turtle

t = turtle.Turtle()

s = int(input("Enter the length of the side of square: "))

for _ in range(4):
    t.forward(s) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree

turtle.mainloop()
