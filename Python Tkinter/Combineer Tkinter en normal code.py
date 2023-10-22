import tkinter as tk

# Maak het hoofdvenster aan
root = tk.Tk()

# Stel de titel van het venster in
root.title("Hello World en Logo")

# Maak een canvas aan om het logo weer te geven
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Teken het logo op het canvas
logo = tk.PhotoImage(file="Python.png")
canvas.create_image(150, 150, image=logo)

# Maak een label aan met de "Hello World!" tekst
label = tk.Label(root, text="Hello World!")
label.pack()

# Start de mainloop om het venster te laten zien
root.mainloop()
