from tkinter import *

# Om de text van het label altijd van een gelijke lengte te laten zijn, heb ik 9 regels if - elif - else toegevoegd voor het toevoegen van "geen" tot "twee" voorvoeg "nullen" [0]
def use_mouse(event):
    if event.x < 10 and event.y < 10:
        label.config(text= f"The mouse coordinates are: x = 00{str(event.x)} y = 00{str(event.y)}")
    elif event.x < 10 and event.y > 9 and event.y < 100:
        label.config(text= f"The mouse coordinates are: x = 00{str(event.x)} y = 0{str(event.y)}")
    elif event.x < 10 and event.y > 99:
        label.config(text= f"The mouse coordinates are: x = 00{str(event.x)} y = {str(event.y)}")
    elif event.x > 9 and event.x < 100 and event.y < 10:
        label.config(text= f"The mouse coordinates are: x = 0{str(event.x)} y = 00{str(event.y)}")            
    elif event.x > 9 and event.x < 100 and event.y > 9 and event.y < 100:
        label.config(text= f"The mouse coordinates are: x = 0{str(event.x)} y = 0{str(event.y)}")    
    elif event.x > 9 and event.x < 100 and event.y > 99:
        label.config(text= f"The mouse coordinates are: x = 0{str(event.x)} y = {str(event.y)}")           
    elif event.x > 99 and event.y < 10:
        label.config(text= f"The mouse coordinates are: x = {str(event.x)} y = 00{str(event.y)}")
    elif event.x > 99 and event.y > 9 and event.y < 100:
        label.config(text= f"The mouse coordinates are: x = {str(event.x)} y = 0{str(event.y)}")       
    else:    
        label.config(text= f"The mouse coordinates are: x = {str(event.x)} y = {str(event.y)}")
            
window = Tk()
window.geometry("800x600")

# left mouse click
# window.bind("<Button-1>", use_mouse)
# # scroll wheel click
# window.bind("<Button-2>", use_mouse)
# # right mouse click
# window.bind("<Button-3>", use_mouse)
# # move the mouse to enter the window 
# window.bind("<Enter>", use_mouse)
# # release one of the three buttons
# window.bind("<ButtonRelease>", use_mouse)
# # move the mouse to leave the window
# window.bind("<Leave>", use_mouse)
# # move the mouse
window.bind("<Motion>", use_mouse)

label = Label(window, font= ("Cambria", 30))
# The place method takes three arguments: relx and rely (relative x and y coordinates of a point to place the widget) and an anchor argument to specify the anchor point. Here, relx=0.5 and rely=0.5 puts the label in the middle of the window, and anchor=CENTER specifies that the center of the label should be placed at the middle point.
label.place(relx= 0.5, rely= 0.5, anchor= CENTER)

window.mainloop()