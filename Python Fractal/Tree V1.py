# Dit voorbeeld gebruikt recursie om een boom te tekenen.
# De draw_tree functie tekent een tak van de boom en roept zichzelf vervolgens tweemaal aan om kleinere takken
# te tekenen, waardoor de boom zich vertakt. Je kunt de waarden van de variabelen aanpassen om verschillende vormen
# en maten van de boom te verkrijgen.
# Dit is slechts een basisvoorbeeld van het tekenen van een recursieve boom. Je kunt dit verder aanpassen en verbeteren
# door kleuren toe te voegen, bladeren te tekenen, enzovoort.
#  In deze aangepaste versie wordt de plt.pause(pause_time) functie gebruikt om een korte pauze in te lassen tussen
#  elke stap van de recursie. Hierdoor kun je het geleidelijke opbouwproces van de boom zien.
#  Pas de waarde van pause_time aan om de snelheid van de animatie aan te passen.
#  Let op dat het uitvoeren van deze code even kan duren vanwege de pauzes tussen de stappen.

import matplotlib.pyplot as plt
import numpy as np

# Functie om een boom te tekenen
# x en y zijn de coördinaten van het beginpunt van de tak
# length is de lengte van de tak
# angle is de hoek van de tak
# depth is de diepte van de boom
# branch_width is de breedte van de tak


def draw_tree(x, y, length, angle, depth, branch_width, pause_time):
    if depth > 0:
        # Bereken de eindpunten van de tak
        # De tak begint op (x, y) en eindigt op (x_end, y_end)
        # De hoek van de tak is angle

        x_end = x + length * np.cos(np.radians(angle))
        y_end = y + length * np.sin(np.radians(angle))
        plt.plot([x, x_end], [y, y_end], color='brown', linewidth=branch_width)
        plt.pause(pause_time)

        draw_tree(x_end, y_end, length * 0.7, angle - 20, depth - 1, branch_width * 0.7, pause_time)
        draw_tree(x_end, y_end, length * 0.7, angle + 20, depth - 1, branch_width * 0.7, pause_time)


def main():
    # figsize is de grootte van de figuur van 20x20 centimeter bij 100 dpi
    plt.figure(figsize=(20 / 2.54, 20 / 2.54), dpi=100)
    plt.axis('off')

    start_x = 0.0
    start_y = 0.0
    # trunk_length is de lengte van de stam
    trunk_length = 100
    # trunk_angle is de hoek van de stam
    trunk_angle = 90
    # tree_depth is het aantal iteraties van de recursie
    tree_depth = 8
    # initial_branch_width is de breedte van de stam
    initial_branch_width = 10
    # pause_time is de pauze tussen elke stap in seconden
    pause_time = 0.1

    draw_tree(start_x, start_y, trunk_length, trunk_angle, tree_depth, initial_branch_width, pause_time)

    plt.show()

# Voer de main functie uit als dit script wordt uitgevoerd
# if __name__ == "__main__":
main()
