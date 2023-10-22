from tkinter import *

def open_file():
    print("This will open a file")
    
def save_file():
    print("This will save a file")
    
def cut_text():
    print("This will cut some text")
    
def copy_text():
    print("This will copy some text")
    
def paste_text():
    print("This will paste some text")
      
window = Tk()

copy_image = PhotoImage(file= "Icon copy.png")
cut_image = PhotoImage(file= "Icon cut.png")
paste_image = PhotoImage(file= "Icon paste.png")

widget_menu = Menu(window)
window.config(menu= widget_menu)

file_menu_item = Menu(widget_menu,
                 tearoff= 0,
                 font= ("MV Boli", 15)
                 )
widget_menu.add_cascade(label= "File",
                        menu= file_menu_item,
                        )
file_menu_item.add_command(label= "Open",
                      command= open_file,
                      )
file_menu_item.add_command(label= "Save",
                      command= save_file,
                      )
file_menu_item.add_separator()
file_menu_item.add_command(label= "Exit",
                      command= quit,
                      )

edit_menu_item = Menu(widget_menu,
                 tearoff= 0,
                 font= ("MV Boli", 15),
                 )
widget_menu.add_cascade(label= "Edit"
                        ,menu= edit_menu_item,
                        )
edit_menu_item.add_command(label= "Cut",
                      command= cut_text,
                      image= cut_image,
                      compound= "left",
                      )
edit_menu_item.add_command(label= "Copy",
                      command= copy_text,
                      image= copy_image,
                      compound= "left",
                      )
edit_menu_item.add_command(label= "Paste",
                      command= paste_text,
                      image= paste_image,
                      compound= "left",
                      )


# file_ = Menu(widget_menu)
# widget_menu.add_cascade(label= "File", menu= file_)

window.mainloop()