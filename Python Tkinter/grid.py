from tkinter import *

root =Tk()

# Creating a label widget
my_label_1 = Label(root, text = "Hello World!")
my_label_2 = Label(root, text = "My name is Jan George Koomen")
my_label_3 = Label(root, text = "I live in a town called Goes")

# Using the grid on the screen
my_label_1.grid(row= 0, column= 0)
my_label_2.grid(row= 1, column= 1)
my_label_3.grid(row= 2, column= 2)

# tkinter is object oriented so we can als use this:
my_label_4 = Label(root, text = "Hello World!").grid(row= 3, column= 3)
my_label_5 = Label(root, text = "My name is Jan George Koomen").grid(row= 4, column= 4)
my_label_6 = Label(root, text = "I live in a town called Goes").grid(row= 5, column= 5)

root.mainloop()