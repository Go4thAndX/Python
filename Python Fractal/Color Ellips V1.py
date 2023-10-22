import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import colorsys as cs

'''Deze code creëert een lege figuur en assen door de subplots() functie van de matplotlib.pyplot module te gebruiken. Het wijst het figuur-object toe aan de variabele 'fig', en het assen-object aan de variabele 'ax'.

Vervolgens stelt het de beeldverhouding van de assen in op 'gelijk' met behulp van de set_aspect() methode. Het eerste argument 'equal' zorgt ervoor dat de beeldverhouding gelijk is in zowel de x- als y-richting. Het tweede argument 'box' geeft aan dat de verhouding wordt bepaald door de gegevenslimieten.

Daarna schakelt het de aslijnen en labels uit met behulp van de set_axis_off() methode, zodat de assen niet worden weergegeven in de uiteindelijke plot.

Ten slotte stelt het de achtergrondkleur van de assen in op zwart met behulp van de set_facecolor() methode. Dit zal de achtergrondkleur van de plot op zwart zetten.'''

fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_axis_off()
ax.set_facecolor('black')

num_frames = 1
num_segments = 1

'''De geselecteerde code wordt gebruikt om een ellips te tekenen op een matplotlib-figuur. Hier is een uitleg van elke regel:

`ax.clear()`: Met deze code wordt alle vorige inhoud van het huidige assenobject 'ax' gewist.

`color = cs.hsv_to_rgb(0, 0, 1)`: Deze regel zet de opgegeven HSV (Tint, Verzadiging, Waarde) waarden om naar het RGB-kleurformaat. De resulterende kleur is een volledig verzadigd en helder blauw.

`angle = np.linspace(0, 2 * np.pi, 100)`: Deze regel creëert een reeks van 100 gelijkmatig verdeelde hoeken, variërend van 0 tot 2π radialen. Deze hoeken worden gebruikt om de x- en y-coördinaten van de ellips te genereren.

`a = 200`: Met deze regel wordt de waarde 200 toegewezen aan de variabele 'a', die de grote as van de ellips vertegenwoordigt.

`b = 100`: Deze regel kent de waarde 100 toe aan de variabele 'b', die de kleine as van de ellips voorstelt.

`x = a * np.cos(angle)`: Hiermee worden de x-coördinaten van de punten op de ellips berekend met behulp van de cosinusfunctie en de gegeven hoekwaarden. De grote as 'a' schaalt de x-coördinaten.

`y = b * np.sin(angle)`: Deze regel berekent de y-coördinaten van de punten op de ellips met behulp van de sinusfunctie en de gegeven hoekwaarden. De kleine as 'b' schaalt de y-coördinaten.

`ax.plot(x, y, color=color)`: Hiermee wordt de ellips getekend op het assenobject 'ax'. De plot-functie neemt de x- en y-coördinaten van de punten en de gespecificeerde kleur aan. Het resulterende plot zal een gesloten kromme zijn die een ellips voorstelt.'''

def draw_frame(frame):
    ax.clear()
    color = cs.hsv_to_rgb(0, 0, 1)  # Kleur van de ellips
    angle = np.linspace(0, 2 * np.pi, 100)
    a = 200  # Grote as
    b = 100  # Kleine as
    x = a * np.cos(angle)
    y = b * np.sin(angle)
    ax.plot(x, y, color=color)
    
'''De geselecteerde code creëert een animatie met behulp van de functie animation.FuncAnimation. Hierbij worden drie argumenten gebruikt: fig, draw_frame en frames.

- fig is een verwijzing naar het figuur-object waarop de animatie zal worden weergegeven.
- draw_frame is de functie die wordt aangeroepen om elk frame van de animatie te tekenen.
- frames is het aantal frames dat in de animatie zal worden getekend.

De functie animation.FuncAnimation maakt een animatie door herhaaldelijk de draw_frame-functie aan te roepen voor elk frame in de animatie. Hierbij wordt het frames-argument gebruikt om het totale aantal frames te bepalen.

Het resultaat van deze code is de variabele ani, die de gecreëerde animatie vertegenwoordigt.'''

ani = animation.FuncAnimation(fig, draw_frame, frames=num_frames)
plt.show()
