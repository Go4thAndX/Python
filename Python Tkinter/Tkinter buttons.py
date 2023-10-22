from tkinter import *
from PIL import Image, ImageTk

count = 0
def click():
    global count
    count += 1
    if count == 1:
        print(f"You clicked the button {count} time in a row")
    else:
        print(f"You clicked the button {count} times in a row")
        
window = Tk()
window.geometry("600x600")

image1 = Image.open("Pinup.jpg")
photoimage = ImageTk.PhotoImage(image1)

# button = a button is a graphical control widget that allows the user to interact with a program or application. It usually consists of a text label, an icon, or both. When the user clicks the button, a command is sent to the program or application, which carries out a specified task.that holds text and/or an image within a window

widget_button = Button(window,
                    activebackground= "black",
                    activeforeground= "#8ab0ed",
                    bd= 10,
                    command= click,
                    compound= "bottom",
                    bg= "#8ab0ed",
                    font=("Cambria", 40, "bold"),
                    image= photoimage,
                    padx= 20,
                    pady= 20,
                    relief = RAISED,
                    state= ACTIVE,
                    # state= DISABLED,
                    text="Click Me!",
                    )
widget_button.pack()

window.mainloop()