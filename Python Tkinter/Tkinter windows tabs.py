from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x300")

# ttk.Notebook() = A widget that manages a collection of windows/displays
widget_notebook = ttk.Notebook(window)

# New frame for tab_1
tab_1 = Frame(widget_notebook)
# New frame for tab_2
tab_2 = Frame(widget_notebook)

widget_notebook.add(tab_1,
                    text= "Tab 1",
                    )
widget_notebook.add(tab_2,
                    text= "Tab 2",
                    )
# expand = this will expand to fill any space not otherwise used
# fill = this will fill space on x- and y axis
widget_notebook.pack(expand= True,
                     fill= "both")

Label(tab_1,
      text= "Hello, this is tab#1",
      width= 50,
      height= 25,
      ).pack()
Label(tab_2,
      text= "Goodbye, this is tab#2",
      width= 50,
      height= 25,
      ).pack()

window.mainloop()