from tkinter import *

window = Tk()

# canvas = a widget that is used to draw graphs, plots, images in a window
canvas_1 = Canvas(window,
                height= 500,
                width= 500,
                )
blue_line = canvas_1.create_line(1, 1, 499, 499, fill= "blue", width= 5)
red_line = canvas_1.create_line(100, 400, 400, 100, fill= "red", width= 5)
canvas_1.grid(row= 0, column= 0)

canvas_2 = Canvas(window,
                height= 500,
                width= 500,
                )
canvas_2.create_rectangle(50, 50, 250, 250, fill= "purple")
canvas_2.grid(row= 0, column= 1)

canvas_3 = Canvas(window,
                height= 500,
                width= 500,
                )
coordinates = [250, 1, 499, 499, 1, 499]
canvas_3.create_polygon(coordinates, fill= "yellow", outline= "black", width= 5)
canvas_3.grid(row= 1, column= 0)

canvas_4 = Canvas(window,
                height= 500,
                width= 500,
                )
canvas_4.create_arc(0, 0, 500, 500, fill= "green")
canvas_4.create_arc(0, 0, 500, 500, fill= "brown", style= CHORD, start= 90)
canvas_4.create_arc(0, 0, 500, 500, fill= "grey", style= PIESLICE, start= 180, extent= 180)
canvas_4.grid(row= 1, column= 1)

window.mainloop()