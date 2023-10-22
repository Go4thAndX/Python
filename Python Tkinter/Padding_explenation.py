from tkinter import *

root = Tk()

# set the window size
root.geometry("400x300")

# create the buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")
button_3 = Button(root, text="Button 3")
button_4 = Button(root, text="Button 4")

# # Geometry 1
# button_1.grid()
# button_2.grid()
# button_3.grid()
# button_4.grid()

# # Geometry 2, apply rows and columns
# button_1.grid(row= 1, column= 1)
# button_2.grid(row= 2, column= 1)
# button_3.grid(row= 1, column= 2)
# button_4.grid(row= 2, column= 2)

# # Geometry 3, apply padding, button_1, padx= 10
# button_1.grid(row=1, column=1, padx=10)
# button_2.grid(row=2, column=1)
# button_3.grid(row=1, column=2)
# button_4.grid(row=2, column=2)

# # Geometry 4, apply padding, button_1, padx= 10, pady= 10
# button_1.grid(row=1, column=1, padx= 10, pady= 10)
# button_2.grid(row=2, column=1)
# button_3.grid(row=1, column=2)
# button_4.grid(row=2, column=2)

# # Geometry 5, apply padding, button_2, padx= 10, pady= 10
# button_1.grid(row=1, column=1, padx= 10, pady= 10)
# button_2.grid(row=2, column=1, padx= 10, pady= 10)
# button_3.grid(row=1, column=2)
# button_4.grid(row=2, column=2)

# # Geometry 6, apply padding, button_3, padx= 10, pady= 10
# button_1.grid(row=1, column=1, padx= 10, pady= 10)
# button_2.grid(row=2, column=1, padx= 10, pady= 10)
# button_3.grid(row=1, column=2, padx= 10, pady= 10)
# button_4.grid(row=2, column=2)

# # Geometry 7, apply padding, button_4, padx= 10, pady= 10
# button_1.grid(row=1, column=1, padx= 10, pady= 10)
# button_2.grid(row=2, column=1, padx= 10, pady= 10)
# button_3.grid(row=1, column=2, padx= 10, pady= 10)
# button_4.grid(row=2, column=2, padx= 10, pady= 10)

# # Geometry 8, apply padding, button_1, padx= 20, pady= 20
# button_1.grid(row=1, column=1, padx= 20, pady= 20)
# button_2.grid(row=2, column=1, padx= 10, pady= 10)
# button_3.grid(row=1, column=2, padx= 10, pady= 10)
# button_4.grid(row=2, column=2, padx= 10, pady= 10)

# Geometry 9, apply padding
button_1.grid(padx= 0, pady= 5)
button_2.grid(row= 2, column= 2, padx= 10, pady= 15)
button_3.grid(padx= 20, pady= 25)
button_4.grid(row= 4, column= 4, padx= 30, pady= 35)

root.mainloop()