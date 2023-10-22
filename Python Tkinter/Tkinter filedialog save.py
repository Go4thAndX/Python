from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir= "G:\\Mijn Drive\\GoogleMap Python\\Python Tkinter",
                                    defaultextension= ".txt",
                                    filetypes= [("Text file", ".txt"),
                                                ("HTML file", ".html"),
                                                ("All files", ".*"),
                                                ]
                                    )
    if file is None:
        return
    file_text = str(widget_text.get(1.0, END))
    file.write(file_text)
    file.close()
    # (initialdir= "G:\\Mijn Drive\\GoogleMap Python\\Python Tkinter",
    #                                        title= "Open file",
    #                                        filetypes= (("text files", "*.txt"), ("All files", "*.*")),
    # )
    # file = open(file_path, "r")
    # print(file.read())
    # file.close()
    
window = Tk()

widget_button = Button(text= "Save file",
                       command= save_file)
widget_button.pack()
widget_text = Text(window)
widget_text.pack()

window.mainloop()