from tkinter import *

# radiobutton = a button simular to a checkbox, but you can only select one checkbox from a group

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered a pizza !")
    elif(x.get() == 1):
        print("You ordered a hamburger !")
    elif(x.get() == 2):
        print("You ordered a hotdog !")
    else:
        print("You didn't order huh ?")
        
window = Tk()

pizzaImage = PhotoImage(file= "emoji pizza.png")
hamburgerImage = PhotoImage(file= "emoji hamburger.png")
hotdogImage = PhotoImage(file= "emoji hotdog.png")
foodImages =[pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for i in range(len(food)):
    widget_radiobutton = Radiobutton(window,
                                    #  adds text to each radiobutton
                                     text= food[i],
                                    #  groups each radiobutton together for the same variable
                                     variable= x,
                                    #  assigns a different value to each radiobutton
                                     value= i,
                                    #  adds padding on x-axis
                                     padx= 25,
                                     font= ("Impact", 50),
                                    #  adds image to each radiobutton
                                    image= foodImages[i],
                                    # adds image & text to the left-side
                                    compound= "left",
                                    # # eliminate each circle indicator
                                    # indicatoron= 0,
                                    # width= 375,
                                    # height= 150,
                                    # relief= RAISED,
                                    # set command of each radiobutton to the function
                                    command= order,
                                     )
    
    widget_radiobutton.pack(anchor= W)
window.mainloop()