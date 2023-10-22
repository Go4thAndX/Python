from tkinter import *
import time
import random

WIDTH = 500
HEIGHT = 500
x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image_1 = PhotoImage(file="EarthfromSpace.png")
my_image_1 = canvas.create_image(0, 0, image=photo_image_1, anchor=NW)

photo_image_2 = PhotoImage(file="Ufo.png")
my_image_2 = canvas.create_image(0, 0, image=photo_image_2, anchor=NW)

image_width = photo_image_2.width()
image_height = photo_image_2.height()

# adding a global variable to keep track of the program's state
running = True


def stop_program():
    global running
    running = False
    window.destroy()


stop_button = Button(window, text="Stop", command=stop_program)
# adding the stop button
stop_button.pack(side=BOTTOM)


def update_ufo_position():
    # adding the running variable to update_ufo_position()
    global x_velocity, y_velocity, running
    if running:
        coordinates = canvas.coords(my_image_2)
        # prints the coordinates with 1 decimal digit
        print("%.1f %.1f" % (coordinates[0], coordinates[1]))
        if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
            x_velocity = -x_velocity
            y_velocity = random.uniform(-2, 2)
        # use random module to set new y velocity
        if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
            y_velocity = -y_velocity
            x_velocity = random.uniform(-3, 3)
        # use random module to set new x velocity
        canvas.move(my_image_2, x_velocity, y_velocity)
        canvas.after(10, update_ufo_position)


canvas.after(10, update_ufo_position)
window.mainloop()
