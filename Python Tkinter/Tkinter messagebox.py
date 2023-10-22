from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title= "Info message box",
    #                     message= "You are informed",
    #                     )
    
    # messagebox.showwarning(title= "WARNING message box !!!",
    #                     message= "You have a virus",
    #                     )
    
    # messagebox.showerror(title= "ERROR message box !!!",
    #                     message= "There is something wrong",
    #                     )
    
    # if messagebox.askokcancel(title= "Ok, Annuleren message box",
    #                        message= "Do you want to do something ? "):
    #     print("You did something !")
    # else:
    #     print("You canceled something !")
        
    # if messagebox.askretrycancel (title= "Opnieuw, Annuleren message box",
    #                        message= "Do you want to retry something ? "):
    #     print("You retried something !")
    # else:
    #     print("You canceled something !")
        
    # if messagebox.askyesno (title= "Ja, Nee message box",
    #                        message= "Do you want to do something ? "):
    #     print("You do want to do something !")
    # else:
    #     print("You don't want to do something !")
        
    # answer = (messagebox.askquestion(title= "Question message box", message= "Do you want to do something ? "))
    # if(answer == "yes"):
    #     print("You do want to do something !")
    # else:
    #     print("You don't want to do something !")
        
    answer = (messagebox.askyesnocancel (title= "Ja, Nee, Annuleren message box", message= "Do you want to do something ? "))
    if(answer == True):
        print("You do want to do something !")
    elif(answer == False):
        print("You don't want to do something !")
    else:
        print("You don't know if you want to do something !")
        
window = Tk()

widget_button = Button(text= "Click me!",
                       command= click,
                       )
widget_button.pack()

window.mainloop()