from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

my_image = PhotoImage(file="sportscar.png")
label = Label(window, image=my_image)
label.place(x=0, y=0)

window.mainloop()
