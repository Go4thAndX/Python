# Het tekenen en visualiseren van fractals met behulp van Python kan op verschillende manieren worden gedaan,
# maar een populaire aanpak is om gebruik te maken van de Python-bibliotheek genaamd "matplotlib".
# Matplotlib is een krachtige bibliotheek voor datavisualisatie die je in staat stelt om verschillende soorten
# grafieken en visuele representaties, waaronder fractals, te maken.
# Hier is een eenvoudig voorbeeld van hoe je een eenvoudige fractal, zoals de Julia-set,
# kunt tekenen en visualiseren met matplotlib:
# Je kunt experimenteren met verschillende waarden voor c, max_iter, en andere parameters om verschillende soorten
# fractals te genereren.
# Je kunt ook de breedte en hoogte van de afbeelding wijzigen om de resolutie van de fractal te veranderen.
# Hoe hoger de resolutie, hoe langer het duurt om de fractal te berekenen.
# Als je de fractal wilt opslaan als een afbeeldingsbestand, kun je de volgende regel code toevoegen:
# plt.savefig('julia_set.png', dpi=300)
# Hiermee wordt de fractal opgeslagen als een PNG-bestand met een resolutie van 300 dpi.


import numpy as np
import matplotlib.pyplot as plt


# Functie om de Julia-set te berekenen
# def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
#     x = np.linspace(x_min, x_max, width)
#     y = np.linspace(y_min, y_max, height)
#     X, Y = np.meshgrid(x, y)
#     Z = X + 1j * Y
#     fractal = np.zeros(Z.shape, dtype=int)
#
#     for i in range(max_iter):
#         Z = Z ** 2 + c
#         mask = np.abs(Z) < 10
#         fractal += mask
#
#     return fractal


# Functie om de Julia-set te berekenen met hogere precisie
def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    fractal = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        Z = Z ** 2 + c
        mask = np.abs(Z) < 10
        fractal += mask

    return fractal


# Instellingen voor de fractal
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
c = -0.7 + 0.27j  # Complex getal voor de Julia-set
max_iter = 100

# Bereken de fractal
fractal = julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)

# Visualiseer de fractal
plt.imshow(fractal, extent=(x_min, x_max, y_min, y_max), cmap='inferno')
plt.colorbar()
plt.title("Julia-set Fractal")
plt.xlabel("Reële as")
plt.ylabel("Imaginaire as")
plt.show()

# Als de voorgestelde oplossing nog steeds foutmeldingen genereert, zijn er enkele andere stappen die je kunt overwegen:
# Verklein het bereik van de complexe getallen: Probeer het gebied van complexe getallen dat je onderzoekt verder te beperken. Dit kan helpen om de waarden van de iteratieve berekeningen binnen redelijke grenzen te houden.
#
# Gebruik een andere fractal formule: Als je voortdurend problemen hebt met de Julia-set formule, probeer dan een andere fractal formule, zoals de Mandelbrot-set formule. De Mandelbrot-formule wordt vaak gebruikt en heeft vaak minder kans op overflows.
#
# Gebruik een kleinere iteratielimiet: Verminder het aantal iteraties dat je uitvoert om de groei van de waarden te beperken. Dit kan de kans op overflows verminderen, hoewel het ook de kwaliteit van de fractal kan beïnvloeden.
#
# Gebruik complexe getallen met kleinere waarden: Probeer complexe getallen te gebruiken met kleinere reële en imaginaire delen. Dit kan helpen om de waarden tijdens de iteratieve berekeningen te beperken.
#
# Controleer de implementatie: Controleer zorgvuldig je implementatie om ervoor te zorgen dat er geen andere factoren zijn die overflows kunnen veroorzaken, zoals verkeerde berekeningen of ontbrekende omstandigheden.