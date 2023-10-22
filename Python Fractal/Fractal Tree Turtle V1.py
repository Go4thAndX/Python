import turtle
import random

# Create a turtle object
my_turtle = turtle.Turtle()
# Create a screen object
my_screen = turtle.Screen()
# Set the screen background color
my_screen.bgcolor('white')
# Set the turtle object color and width
my_turtle.color('green')
my_turtle.width(3)
# Set the turtle pen size
my_turtle.pensize(2)
# The turtle starts at the center of the screen and moves west
# The turtle direction (0 = east, 90 = north, 180 = west, 270 = south)
my_turtle.left(90)
my_turtle.backward(200)
# The turtle speed (0 = no animation, 10 = fastest)
my_turtle.speed(0.1)

# To draw a fractal tree, we use recursion
def draw_fractal_tree(length):
        
    if length < 10:
        return
    else:
        color_list_tree = ['chocolate', 'brown', 'saddle brown', 'sienna', 'peru', 'burlywood', 'tan']
        color_tree = random.choice(color_list_tree)
        color_list_leaf = ['green', 'dark green', 'forest green', 'green yellow', 'lime green', 'lime', 'olive drab']
        color_leaf = random.choice(color_list_leaf)
        my_turtle.forward(length)
        my_turtle.color(color_leaf)
        my_turtle.circle(2)
        my_turtle.color(color_tree)
        my_turtle.left(30)
        draw_fractal_tree(3 * length / 4)
        my_turtle.right(60)
        draw_fractal_tree(3 * length / 4)
        my_turtle.left(30)
        my_turtle.backward(length)
        
        
draw_fractal_tree(200)
turtle.done()