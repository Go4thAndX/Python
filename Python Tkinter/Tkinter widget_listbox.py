from tkinter import *

def submit():
    food = []
    for i in widget_listbox.curselection():
        food.insert(i, widget_listbox.get(i))  
    print("You have ordered: ")
    for i in food:
        print(i)
    
def add():
    widget_listbox.insert(widget_listbox.size(), entry_box.get())
    widget_listbox.config(height= widget_listbox.size())
    
def delete():
    for i in reversed(widget_listbox.curselection()):
        widget_listbox.delete(i)
    widget_listbox.config(height= widget_listbox.size())

window = Tk()

# Listbox = a listing of selectable text items within it's own container
widget_listbox = Listbox(window,
                         bg= "#9be7eb",
                         font=("Constantia, 35"),
                         width= 12,
                         selectmode= MULTIPLE, 
                         )
widget_listbox.pack()

widget_listbox.insert(1, "pizza")
widget_listbox.insert(2, "pasta")
widget_listbox.insert(3, "garlic bread")
widget_listbox.insert(4, "soup")
widget_listbox.insert(5, "salad")

widget_listbox.config(height= widget_listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text= "Submit",
                       command= submit)
submit_button.pack()

add_button = Button(window,
                       text= "Add",
                       command= add)
add_button.pack()

delete_button = Button(window,
                       text= "Delete",
                       command= delete)
delete_button.pack()

window.mainloop()