from tkinter import *

def submit():
    first_name_text = first_name_entry.get()
    print(first_name_text)
    last_name_text = last_name_entry.get()
    print(last_name_text)
    email_text = email_entry.get()
    print(email_text)
    
window = Tk()

title_label = Label(window,
                    text= "Enter your info: ",
                    font= ("Cambria", 25),
                    )
title_label.grid(row= 0,
                column= 0,
                columnspan= 2)

first_name_label = Label(window,
                        text= "First name: ",
                        width= 10,
                        anchor= "w",
                        bg= "#76b085",
                        )
first_name_label.grid(row= 1,
                    column= 0,
                    padx= 5)
first_name_entry = Entry(window)
first_name_entry.grid(row= 1,
                    column= 1)

last_name_label = Label(window,
                        text= "Last name: ",
                        width= 10,
                        anchor= "w",
                        bg= "#76b085",
                        )
last_name_label.grid(row= 2,
                    column= 0,
                    padx= 5)
last_name_entry = Entry(window)
last_name_entry.grid(row= 2,
                    column= 1)

email_label = Label(window,
                    text= "Email adres: ",
                    width= 10,
                    anchor= "w",
                    bg= "#76b085",
                    )
email_label.grid(row= 3,
                column= 0,
                padx= 5)
email_entry = Entry(window)
email_entry.grid(row= 3,
                column= 1)

submit_button = Button(window,
                    text= "Submit",
                    command= submit)
submit_button.grid(row= 4,
                column= 1, 
                columnspan= 2,
                pady= 10)

window.mainloop()