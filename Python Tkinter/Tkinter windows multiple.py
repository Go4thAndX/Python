from tkinter import *

# Toplevel() = New window "on top" of other windows, linked to a "bottom" window
def create_window():
    # new_window = Toplevel()
# Tk() = New independent window
    new_window = Tk()
# .destroy() = Close out the main_window
    main_window.destroy()
    
main_window = Tk()
main_window.geometry("400x300")

Button(main_window, text= "Create new window", command= create_window).pack()

main_window.mainloop()