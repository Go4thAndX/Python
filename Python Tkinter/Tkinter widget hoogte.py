# Je kunt de hoogte in pixels van een tkinter-element bepalen door gebruik te maken van de .winfo_height() methode. Deze methode geeft een integer terug die de hoogte in pixels van het element aanduidt. Voorbeeldcode:

from tkinter import *

root = Tk()

widget = Label(root)
widget.pack()

# Bepaal de hoogte in pixels van de widget, waarbij zeker is gesteld dat de widget is gerenderd op het scherm
root.update()
widget_height = widget.winfo_height()
print(widget_height)

root.mainloop()