# We doorlopen stap voor stap de code en geven uitleg voor de redenen achter elke stap.

# Stap 1: Importeer de vereiste bibliotheken (Matplotlib) en modules (pyplot, patches).
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Stap 2: Definieer de functie `draw_tree()` die de boom zal tekenen.
def draw_tree():

# Stap 3: Creëer een set van assen.
    ax = plt.gca()
    plt.pause(1)
# We verkrijgen hier direct een set van assen verkregen met plt.gca() (get current axes). Deze set assen (`ax`) zal dienen als ons canvas om de visuele elementen op te tekenen.

# Stap 4: Teken de stam van de boom.
    ax.plot([0, 0], [0, 0.5], color='brown', linewidth=20)
    plt.pause(1)

# Hier gebruiken we de `ax.plot()` functie om een verticale lijn (de stam) te tekenen van (0,0) tot (0,0.5). We stellen de kleur in op bruin en de lijnbreedte op 20 om een dikke stam te maken.

# Stap 5: Teken de tak van de boom.
    ax.plot([0, 0.2], [0.5, 0.7], color='brown', linewidth=10)
    plt.pause(1)
    
# Met een vergelijkbare aanroep van `ax.plot()` tekenen we een schuine lijn (de tak) van (0, 0.5) tot (0.2, 0.7). De kleur is opnieuw bruin, maar ditmaal stellen we de lijnbreedte in op 10.

# Stap 6: Teken het blaadje.
    leaf_path = patches.PathPatch(
        patches.Path([
            (0.2, 0.7),
            (0.28, 0.9),
            (0.33, 0.9),
            (0.4, 0.7),
            (0.33, 0.5),
            (0.28, 0.5),
            (0.2, 0.7)
        ]),
        facecolor='green'
    )
    ax.add_patch(leaf_path)
    plt.pause(1)
    
# We maken gebruik van de Path-klasse van Matplotlib om een aangepaste vorm van een blad te definiëren. Vervolgens creëren we een PathPatch-object met deze vorm en voegen het toe aan de assen met ax.add_patch(). Hierdoor krijgt het blaadje de vorm van een echt blad met de kleur groen.

# Stap 7: Stel de opmaak en eigenschappen van het plotvlak in.
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 1)
    # ax.axis('off')

# We stellen de x- en y-limieten in om ervoor te zorgen dat de hele boom binnen het zichtbare gebied past. We schakelen de assen uit met `ax.axis('off')` om alleen de tekening weer te geven zonder de assenlijnen.

# Stap 8: Toon de plot.
    plt.show()
    
# Met deze laatste regel roepen we `plt.show()` aan om de tekening te tonen in een nieuw venster.

# Roep de functie aan om de boom te tekenen
draw_tree()

# Voeg dit aan het einde van je code toe
# input("Druk op Enter om af te sluiten...")