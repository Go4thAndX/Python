from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("600x600")

image1 = Image.open("Pinup.jpg")
photoimage = ImageTk.PhotoImage(image1)

# label = an area widget that holds text and/or an image within a window
widget_label = Label(window,
                     bd= 10,
                     compound= "bottom",
                     bg= "#8ab0ed",
                     font=("Cambria", 40, "bold"),
                     image= photoimage,
                     padx= 20,
                     pady= 20,
                     relief = RAISED,
                     text="Hello World!",
                     )
widget_label.pack()
# widget_label.place(x= 0, y= 0)

window.mainloop()