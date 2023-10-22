from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain thes widgets
# Instantiate an instance of a window, most coders use "root"
window = Tk()
window.geometry("400x300")
window.title("My first GUI program")

window_icon = PhotoImage(file= "windows.png")
window.iconphoto(True, window_icon)
window.config(bg= "#6fe2e8")

# Place window on computer screen, listen for events
window.mainloop()

