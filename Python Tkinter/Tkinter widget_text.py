from tkinter import *

def submit():
    input_text = widget_text.get("1.0", END)
    print(input_text)

window = Tk()

# text widget = a widget for a text area, you can enter multiple lines of text
widget_text = Text(window,
                   bg= "light yellow",
                   font= ("Ink Free", 25),
                   height= 8,
                   width= 20,
                   padx= 20,
                   pady= 20,
                   fg= "purple")
widget_text.pack()

widget_button = Button(window,
                       text= "Submit",
                       command= submit,
                       )
widget_button.pack()

window.mainloop()