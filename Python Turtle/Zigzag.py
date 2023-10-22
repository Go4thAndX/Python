import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('red')
for x in range(10):
    if x % 2 == 0:
        turtle.forward(25)
        turtle.right(45)
    else:
        turtle.forward(25)
        turtle.left(45)

turtle.mainloop()
