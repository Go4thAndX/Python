from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Set the size of the window
root.geometry("400x400")

# Position text in frame
label1 = Label(root,
               text="Position image on button",
               font=('Arial', 16),
               relief = RAISED)

label1.pack(side=TOP, padx=10, pady=10)

# Create a PIL Image object of the image in the path
image1 = Image.open("Pinup.jpg")

# Create a PhotoImage object from the PIL Image
photoimage = ImageTk.PhotoImage(image1)

# Resize image to fit on button
# photoimage = photoimage.subsample(1, 2)

# Position image on button
button_image = Button(root, image=photoimage)
button_image.pack(side=TOP, pady=10)

mainloop()