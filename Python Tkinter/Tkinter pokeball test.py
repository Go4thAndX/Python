from tkinter import *

window = Tk()

canvas = Canvas(window,
                height= 550,
                width= 500,
                )
canvas.create_arc(10, 10, 490, 490, fill= "red", extent= 180, width= 10)
canvas.create_arc(10, 40, 490, 530, fill= "white", extent= 180, start= 180, width= 10)

# The first argument, 40, specifies the x-coordinate of the top-left corner of the rectangle.
# The second argument, 245, specifies the y-coordinate of the top-left corner of the rectangle.
# The third argument, 460, specifies the x-coordinate of the bottom-right corner of the rectangle.
# The fourth argument, 285, specifies the y-coordinate of the bottom-right corner of the rectangle.
canvas.create_rectangle(40, 245, 460, 285, fill= "black")
# The coordinates (190, 190) represents the top left corner of a rectangular box that is inscribed within the oval
# The coordinates (310, 310) represents the bottom right corner of that rectangular box. 
canvas.create_oval(190, 210, 310, 330, fill= "white", width= 10)
canvas.create_oval(220, 240, 280, 300, fill= "black")
canvas.pack()

window.mainloop()