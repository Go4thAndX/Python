from tkinter import *
from class_Ball import *
import time

# import random

WIDTH = 500
HEIGHT = 500

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT + 50}")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# adding a global variable to keep track of the program's state
running = True


def stop_program():
    global running
    running = False
    window.destroy()


stop_button = Button(window, text="Stop", command=stop_program)
# adding the stop button
# stop_button.pack(pady=10)
stop_button.pack(side=BOTTOM, pady=10)

volley_ball = Ball(canvas, 0, 0, 100, 1, 3, "purple")
tennis_ball = Ball(canvas, 0, 0, 50, 3, 2, "yellow")
basket_ball = Ball(canvas, 0, 0, 125, 2, 5, "brown")
pingpong_ball = Ball(canvas, 0, 0, 20, 5, 4, "white")

running = True
while running:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    pingpong_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()
