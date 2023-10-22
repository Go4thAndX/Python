from tkinter import *

root =Tk()

my_entry = Entry(root, width= 50, bg= "yellow", fg= "black", borderwidth= 5)
my_entry.pack()
my_entry.insert(0, "Enter your name: ")

def my_click():
    intro_text = (f"Hello {my_entry.get()}")
    my_label = Label(root, text= intro_text)
    my_label.pack()
    
my_button = Button(root, text= "Push the button", command= my_click)
my_button.pack()

root.mainloop()