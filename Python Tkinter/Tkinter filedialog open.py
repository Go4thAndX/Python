from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir= "G:\\Mijn Drive\\GoogleMap Python\\Python Tkinter",
                                           title= "Open file",
                                           filetypes= (("text files", "*.txt"), ("All files", "*.*")),
    )
    file = open(file_path, "r")
    print(file.read())
    file.close()
    
window = Tk()

widget_button = Button(text= "Open",
                       command= open_file)
widget_button.pack()

window.mainloop()