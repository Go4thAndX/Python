# draw Rectangle in Python Turtle
import turtle

t = turtle.Turtle()

l = int(input("Enter the length of the Rectangle: "))
w = int(input("Enter the width of the Rectangle: "))

for _ in range(4):

    # drawing length
    if _% 2 == 0:
        t.forward(l) # Forward turtle by l units
        t.left(90) # Turn turtle by 90 degree

    # drawing width
    else:
        t.forward(w) # Forward turtle by w units
        t.left(90) # Turn turtle by 90 degree

turtle.mainloop()
