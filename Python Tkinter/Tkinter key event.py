from tkinter import *

def key_stroke(event):
    print(f"You pressed the {event.keysym} key")
    label.config(text= event.keysym)
    
window = Tk()
window.geometry("400x100")

window.bind("<Key>", key_stroke)

label = Label(window, font= ("Cambria", 60))
label.pack()

window.mainloop()