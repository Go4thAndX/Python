from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_date_string = strftime("%A %d %B %Y")
    day_date_label.config(text=day_date_string)

    # date_string = strftime("%d %B %Y")
    # date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=("Cambria", 50), fg="black", bg="grey")
time_label.pack()

day_date_label = Label(window, font=("Consolas", 30, "bold"))
day_date_label.pack()

# date_label = Label(window, font=("Consolas", 25, "bold"))
# date_label.pack()

update()

window.mainloop()
