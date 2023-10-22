import turtle
import time

# Creating a turtle object
pen = turtle.Turtle()


# Defining method to draw a colored circle with a dynamic radius
def ring(col, rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()


# Drawing the panda
pen.up()
pen.setpos(-35, 95)
pen.down()
ring('black', 15)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(-18, 75)
pen.down()
ring('black', 8)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(0, 55)
pen.down()
ring('black', 5)

time.sleep(0.5)  # Wait for 0.5 seconds before continuing

pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)

# Hiding the turtle
pen.hideturtle()

# Waiting for the user to close the window
turtle.done()
