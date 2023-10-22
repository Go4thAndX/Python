# Ja, het is mogelijk dat het uitvoeringsvenster in PyCharm verdwijnt
# tijdens het gebruik van Turtle-graphics. Dit gebeurt omdat Turtle-graphics
# een afbeelding weergeeft in een afzonderlijk venster, en het kan zijn dat
# het uitvoeringsvenster van PyCharm hierdoor naar de achtergrond wordt geduwd.
#
# Een eenvoudige oplossing is om het Turtle-venster te minimaliseren of te
# verplaatsen, zodat het uitvoeringsvenster van PyCharm weer zichtbaar
# wordt. Je kunt ook overwegen om de Turtle-graphics in een apart bestand te
# schrijven en dit bestand buiten PyCharm uit te voeren. Dit kan worden
# gedaan door het bestand op te slaan met de extensie "Triangle Filled.py" en het
# vervolgens uit te voeren vanuit de opdrachtregel of een ander
# Python-uitvoeringsprogramma.
#
# Een andere oplossing is om de functie "mainloop()" aan het einde van je
# Turtle-code toe te voegen. Deze functie zorgt ervoor dat het venster open
# blijft en wacht tot de gebruiker het sluit. Hierdoor blijft het
# uitvoeringsvenster van PyCharm zichtbaar totdat het Turtle-venster is
# gesloten.

import turtle

# Voeg hier je Turtle-code toe

turtle.mainloop() # Voeg deze functie toe aan het einde van je code

# Ja, je kunt het Turtle-scherm een specifieke grootte geven door de setup()
# functie van de Turtle-module te gebruiken. De setup() functie accepteert
# twee argumenten, de breedte en hoogte van het scherm, in pixels.
#
# Hier is een voorbeeld van het instellen van het Turtle-scherm op een
# grootte van 600x400 pixels:

import turtle

turtle.setup(width=600, height=400)

# Voeg hier je Turtle-code toe

turtle.mainloop()

# Je kunt de waarden van de breedte en hoogte aanpassen aan wat jij nodig
# hebt. Let op dat het opgeven van te grote waarden kan leiden tot een
# vertraging van de prestaties van de grafische rendering.
# Als je ook de positie van het venster wilt instellen, kun je de setpos()
# functie van het turtle object gebruiken:

import turtle

# Met deze code wordt het venster ingesteld op een grootte van 600x400
# pixels en verplaatst naar positie (100, 100) op het scherm.
turtle.setup(width=600, height=400)
turtle.setpos(x=100, y=100)

# Voeg hier je Turtle-code toe

turtle.mainloop()

