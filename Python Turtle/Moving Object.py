import turtle

screen = turtle.Screen()
# screen.setup(500, 500)
screen.bgcolor('Green')

# tell screen to not show automatically
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(3)

# hide donatello, we only want to see the drawing
t.hideturtle()


def draw_square():
    t.fillcolor("Orange")
    t.begin_fill()
    for side in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


# set starting position of turtle within visible part of screen
half_width = screen.window_width() / 2
half_height = screen.window_height() / 4
square_size = 100
t.penup()
t.goto(-half_width + square_size / 2, half_height / 2 - square_size / 2)
t.pendown()

while True:
    t.clear()
    draw_square()

    # only now show the screen, as one of the frames
    screen.update()
    t.forward(0.1)

    # check if turtle is outside the screen
    if t.xcor() \
            < -half_width or t.xcor() > half_width or t.ycor() \
            < -half_height or t.ycor() > half_height:
        break

turtle.mainloop()
