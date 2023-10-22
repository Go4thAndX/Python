import tkinter as tk
import turtle

# Maak het Tkinter-venster
root = tk.Tk()

# Maak een Turtle-canvas in het venster
canvas = turtle.Canvas(root, width=400, height=400)
canvas.pack()

# Maak een Turtle-object
t = turtle.RawTurtle(canvas)

# Voer Turtle-opdrachten uit
t.forward(100)

# Voeg een knop toe aan het venster om de Turtle te laten bewegen
button = tk.Button(root, text="Move Turtle", command=lambda: t.forward(50))
button.pack()

# Start de Tkinter main loop
root.mainloop()
