from tkinter import *
from tkinter import Frame
window = Tk()
window.geometry("400x300")

# Frame = a rectangular container to group and hold widgets
widget_frame = Frame(window,
                     bg= "purple",
                     bd= 5,
                     relief= SUNKEN,
                     )
# widget_frame.pack(side= BOTTOM)
widget_frame.place(x= 100, y= 100)

Button(widget_frame,
       text= "W",
       font= ("Consolas", 25),
       width= 3,
       ).pack(side= TOP)
Button(widget_frame,
       text= "A",
       font= ("Consolas", 25),
       width= 3,
       ).pack(side= LEFT)
Button(widget_frame,
       text= "S",
       font= ("Consolas", 25),
       width= 3,
       ).pack(side= LEFT)
Button(widget_frame,
       text= "D",
       font= ("Consolas", 25),
       width= 3,
       ).pack(side= LEFT)

window.mainloop()