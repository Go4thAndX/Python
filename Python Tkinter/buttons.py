from tkinter import *

root =Tk()

def my_click_1():
    my_label = Label(root, text= "Look I clicked a Button!!")
    my_label.pack()
    
def my_click_2():
    my_label = Label(root, text= "Look I clicked a second Button!!")
    my_label.pack()   

my_button_1 = Button(root, text="Click Me!", command= my_click_1)
my_button_1.pack()

my_button_2 = Button(root, text="You can't click Me!", state= DISABLED)
my_button_2.pack()

my_button_3 = Button(root, text="Click Me Twice!", padx= 50)
my_button_3.pack()

my_button_4 = Button(root, text="Don't Click Me", padx= 50, pady= 50, command= my_click_2, fg="red", bg= "#000")
my_button_4.pack()

root.mainloop()