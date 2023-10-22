from tkinter import *

# The given code initializes a Tkinter object by creating an instance of the Tk class and storing it in the variable named "root". Tkinter is a standard Python library that provides a graphical user interface (GUI) toolkit for creating windows, frames, buttons, labels, etc.
# The Tk() function creates a top-level window object that serves as the main window of the GUI application.
# The second line of the code sets the title of the main window to "Tkinter" using the title() method provided by the Tk class. This method takes a string argument that represents the text to be displayed in the title bar of the window. By calling this method, we can customize the appearance and behavior of the main window according to our needs.
root =Tk()
root.title("Tkinter")

# The code creates a text input field or a widget called an Entry in a graphical user interface (GUI) using the Tkinter library. 
# Specifically, this code creates an Entry widget with a width of 35 pixels and a border width of 5 pixels. Then, it is placed in the GUI using the grid geometry manager. The widget is placed in row 0 and column 0 of the grid and it spans for three columns using the parameter columnspan. Finally, it is given padding of 10 pixels on the x and y axis using padx and pady respectively. 
my_entry = Entry(root, width= 35, borderwidth= 5)
my_entry.grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)

# This code defines the function button_click, which takes a parameter number. When called, this function gets the current contents of an entry widget named my_entry, deletes the contents of my_entry, and inserts new contents into my_entry.
# The new contents inserted into my_entry are a string that combines the previous contents of my_entry with the number passed in as a parameter. In detail, a string is created using Python's formatted string literal syntax (f"{...}"). This string contains two placeholders ({}), which are replaced by converting the current contents of my_entry and number to strings with str(). The resulting concatenated string is then inserted into my_entry.
def button_click(number):
    current = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, (f"{str(current)}{str(number)}"))
    
def button_clear():
    my_entry.delete(0, END)

# The code creates a button widget named "button_1" with the text "Button 1" in the root window. When the button is clicked, it will execute a function named "button_click" with an argument of 1, that is defined using the lambda function to pass the argument without using a separate function definition.
button_1 = Button(root, text= "Button 1", borderwidth= 5, command= lambda: button_click(1))

button_2 = Button(root, text= "Button Clear", borderwidth= 5, command= button_clear)

# The selected code refers to the placement of a Tkinter button in a grid layout. 
# button_1 is the name of the button widget created in the code.
# .grid() is the method used to place the button in a grid layout.
# row=2 defines the row for placement of the button in the grid.
# column=2 defines the column for placement of the button in the grid.
# Therefore, the code will place "button_1" in the cell of the grid layout that is in the third row and third column (since the indexing starts with zero).
# You can add padding to the buttons using the padx and pady parameters when calling the grid() method. padx adds horizontal padding and pady adds vertical padding, in this case adding 10 pixels of padding between the two buttons:
button_1.grid(row=1, column=1, padx=10, pady=10)

button_2.grid(row=2, column=1)

# The root.mainloop() is a method used in Tkinter module for Python that starts the event loop. The event loop listens for events such as mouse clicks and keypresses, and then triggers actions based on the event. The root parameter refers to the main window or frame of the GUI application, which is created using the Tk() method. 
# root.mainloop() starts the main event loop of a GUI application created using Tkinter. It is an essential line of code to ensure that the application is running and is responsive to events generated by the user interacting with the GUI.
root.mainloop()