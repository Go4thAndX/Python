from turtle import Screen, Turtle

TRUE_WIDTH, TRUE_HEIGHT = 300, 300

CHROME = 14  # magic number possibly derivable from tkinter

WIDTH, HEIGHT = TRUE_WIDTH + CHROME, TRUE_HEIGHT + CHROME # need to be slightly larger

IMAGE_SIZE = 20  # cursor size for this example; for your code, the size of the gif images

game_objects = [
    {'t': Turtle(), 'y': 0, 'image': 'circle', 'type':'harm', 'direction':'left', 'speed': 0.4},
    {'t': Turtle(), 'y': -80, 'image': 'square', 'type':'harm', 'direction':'right', 'speed': 0.8}
]

def initialize(game_object):
    # screen.addshape(game_object['image'])

    turtle = game_object['t']
    turtle.shape(game_object['image'])
    turtle.penup()

    direction = game_object['direction']

    if direction == 'right':
        turtle.goto(-100, game_object['y'])
    elif direction == 'left':
        turtle.goto(100, game_object['y'])

    screen.update()

def animate(game_object):
    if game_object['type'] == 'harm':
        turtle = game_object['t']

        if game_object['direction'] == 'right':
            if turtle.xcor() < IMAGE_SIZE + TRUE_WIDTH/2:
                turtle.forward(game_object['speed'])
            else:
                turtle.goto(-IMAGE_SIZE - TRUE_WIDTH/2, game_object['y'])
        elif game_object['direction'] == 'left':
            if turtle.xcor() > -IMAGE_SIZE - TRUE_WIDTH/2:
                turtle.backward(game_object['speed'])
            else:
                turtle.goto(IMAGE_SIZE + TRUE_WIDTH/2, game_object['y'])

        screen.update()

    screen.ontimer(lambda: animate(game_object), 100)

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(WIDTH/2, HEIGHT/2)  # backing store needs to be smaller than window
screen.tracer(False)

for game_object in game_objects:
    initialize(game_object)
    animate(game_object)

screen.mainloop()