from tkinter import *

def display():
    if(x.get()):
        print("You agree to something")
    else:    
        print("You don't agree to something")
        
window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file= "python.png")

widget_checkbutton = Checkbutton(window,
                                 text= "I agree to something",
                                 variable= x,
                                 onvalue= True,
                                 offvalue= False,
                                 command= display,
                                 font= ("Cambria", 20),
                                #  Zo zal tijdens het gebruiken van de checkbutton, de voor- en achtergrond niet van kleur verschillen, geeft een rustiger effect
                                 activeforeground= "black",
                                 activebackground= "white",
                                 image= python_photo,
                                 compound= "right"
                                )
widget_checkbutton.pack()

window.mainloop()