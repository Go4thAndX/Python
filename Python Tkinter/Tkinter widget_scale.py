from tkinter import *
from PIL import Image, ImageTk

def submit():
    print(f"The temperature is: {widget_scale.get()} {chr(8451)}")

window = Tk()

window_width = 300
window_height = 1000
window.geometry(f"{window_width}x{window_height}")

# Give all element the same horizontal padding
hor_padding = 20

hot_image = Image.open("Hot.jpg")
hot_label = ImageTk.PhotoImage(hot_image)
widget_label_hot = Label(image=hot_label)
widget_label_hot.pack(pady= hor_padding)


widget_scale = Scale(window,
                     from_= 100,
                     to= 0,
                     length= 600,
                     orient= VERTICAL,
                     font= ("Consolas", 20),
                     tickinterval= 10,
                     showvalue= 0,
                     resolution= 5,
                     troughcolor= "#547aa8"
                     )
widget_scale.set(((widget_scale["from"] - widget_scale["to"])/2) + widget_scale["to"])
# widget_scale.pack(pady= hor_padding)
widget_scale.pack()

cold_image = Image.open("Cold.jpg")
cold_label = ImageTk.PhotoImage(cold_image)
widget_label_cold = Label(image=cold_label)
widget_label_cold.pack(pady= hor_padding)

widget_button = Button(text="submit",
                       command= submit,
                       )
widget_button.pack(pady= hor_padding)

window.mainloop()
