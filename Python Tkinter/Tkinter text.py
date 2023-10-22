import tkinter as tk

# Maak een Tkinter-venster
root = tk.Tk()

# Stel de grootte van het venster in
root.geometry("300x150")

# Stel de titel van het venster in
root.title("Hello World Logo")

# Maak een canvas om op te tekenen
canvas = tk.Canvas(root, width=300, height=150, bg="black")
canvas.pack()

# Teken de tekst als een logo
canvas.create_text(150, 75, text="Hello World !", font=("Arial", 36, "bold"), fill="white")

# Start de Tkinter main loop
root.mainloop()
