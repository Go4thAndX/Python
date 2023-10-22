from tkinter import *

window = Tk()
# root.geometry("100x100")
# root.geometry("0x0")

canvas_1 = Canvas(window, width = 100, height = 100)
canvas_1.pack()

# Teken een vierkant
canvas_1.create_rectangle(10, 10, 50, 50)

canvas_2 = Canvas(window, width = 100, height = 100)
canvas_2.pack()

canvas_2.create_rectangle(10, 10, 50, 50)

# Je kunt de hoogte in pixels van een tkinter-element bepalen door gebruik te maken van de .winfo_height() methode. Deze methode geeft een integer terug die de hoogte in pixels van het element aanduidt, bepaal de hoogte in pixels van de widget, waarbij zeker is gesteld dat de widget is gerenderd op het scherm door gebruik te maken van .update() methode
window.update()
print(window.winfo_height())
window.mainloop()