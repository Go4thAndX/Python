import matplotlib.pyplot as plt
import matplotlib.patches as patches
# Hier zijn de redenen waarom het gebruik van een set assen handig is, uitgelegd aan de hand van stapsgewijze codevoorbeelden:

# **Reden 1: Flexibiliteit**
# In dit voorbeeld gebruiken we een enkele set assen om meerdere elementen te tekenen - de stam, tak en het blaadje van de boom. Hierdoor kunnen we de visuele elementen op hetzelfde canvas plaatsen en combineren.
ax = plt.gca()
# We tekenen eerst de stam in de vorm van een rechthoek
# 1. plt.Rectangle is een functie die een rechthoek maakt. De eerste twee cijfers zijn de x en y coordinaten van de linker onderhoek van de rechthoek. De derde en vierde cijfers zijn de lengte en breedte van de rechthoek.
# 2. color is de kleur van de rechthoek. De kleur is chocolade bruin.
rectangle = patches.Rectangle((0.2, 0.3), 0.4, 0.5, color='chocolate')
ax.add_patch(rectangle)
plt.show()


# ax.plot([0, 0], [0, 0.5], color='chocolate', linewidth=20)
branche = plt.Rectangle((2, 10), 1, 5, color='brown')
ax.add_artist(branche)
# ax.plot([0, 0.2], [0.5, 0.7], color='brown', linewidth=10)
leaf = plt.Circle((0.2, 0.7), 0.1, color='green')
ax.add_artist(leaf)
plt.pause(1)

# # **Reden 2: Coördinatensysteem**
# # Door het instellen van de x- en y-limieten van de set assen, definiëren we een gestandaardiseerd coördinatensysteem waarin we de elementen kunnen positioneren. Hier gebruiken we de coördinaten van de stam, tak en het blaadje om de elementen te tekenen.
# ax = plt.gca()
# ax.plot([0, 0], [0, 0.5], color='chocolate', linewidth=20)
# ax.plot([0, 0.2], [0.5, 0.7], color='brown', linewidth=10)
# leaf = plt.Circle((0.2, 0.7), 0.1, color='green')
# ax.add_artist(leaf)
# ax.set_xlim(-0.5, 0.5)
# ax.set_ylim(0, 1)
# plt.pause(1)

# # **Reden 3: Overlappende elementen**
# # De volgorde van de tekenopdrachten bepaalt welke elementen bovenop andere worden getekend. Hier tekenen we eerst de tak daarna de stam, en als laatste het blaadje, zodat de stam bovenop de tak en het blaadje boven op de tak ligt.

# ax = plt.gca()

# ax.plot([0, 0.2], [0.5, 0.7], color='brown', linewidth=10)
# ax.plot([0, 0], [0, 0.5], color='chocolate', linewidth=20)
# # En nu een blad in de vorm van een cirkel
# leaf = plt.Circle((0.2, 0.7), 0.1, color='green')
# ax.add_artist(leaf)
# ax.set_xlim(-0.5, 0.5)
# ax.set_ylim(0, 1)
# plt.pause(1)

plt.show()
