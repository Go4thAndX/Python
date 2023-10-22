import tkinter as tk
from tkinter import messagebox

# Maak het hoofdvenster
root = tk.Tk()
root.title("Mijn GUI-toepassing")

# Open het bestand en lees de inhoud
try:
    with open("bestand.txt", "r") as file:
        inhoud = file.read()
except FileNotFoundError:
    messagebox.showerror("Fout", "Het bestand kon niet worden gevonden.")
    root.destroy()

# Voeg een Label widget toe om de inhoud weer te geven
inhoud_label = tk.Label(root, text=inhoud)
inhoud_label.pack()

# Voeg een knop widget toe om het venster te sluiten
# sluit_knop = tk.Button(root, text="Sluiten", command=root.destroy)
# sluit_knop.pack()

# Toon het venster
root.mainloop()