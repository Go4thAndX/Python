from tkinter import *

def submit():
    username = widget_entry.get()
    if username != "":
        print(f"Hello {username}")
    widget_entry.config(state=DISABLED)
    
def delete():
    widget_entry.delete(0, END)

window = Tk()
window.geometry("500x100")

# entry widget = a textbox that accepts a single line of user input
widget_entry = Entry(window,                     
                    font= ("Arial", 25),
                     fg= "#00FF00",
                     bg= "black",
                     show= "*",
                     )
widget_entry.insert(0, "Username")
widget_entry.pack()

submit_button = Button(window,
                       text= "submit",
                       command= submit,
                       )
submit_button.pack()
# submit_button.grid(column= 1, row= 0, padx= 10, pady= 10)
# submit_button.pack(side= RIGHT)

delete_button = Button(window,
                       text= "delete",
                       command= delete)
delete_button.pack()
# delete_button.grid(column= 1, row= 1, padx= 10, pady= 10)
# delete_button.pack(side= RIGHT)

window.mainloop()