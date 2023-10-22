# Dit voorbeeld maakt gebruik van Matplotlib om de stam, tak en het blaadje van de boom te tekenen. We gebruiken NumPy om de coördinaten te manipuleren. De draw_tree()-functie creëert een plot en voegt lijnen en een cirkel toe om de boom te tekenen. Vervolgens wordt de plot weergegeven met plt.show().

# Het is handig om een set assen te gebruiken bij het tekenen met Matplotlib.
# In Matplotlib is een "set van assen" (axes) een object dat een enkel plotvlak vertegenwoordigt waarop je visuele elementen kunt tekenen, zoals lijnen, cirkels, tekst en meer. Hier zijn enkele redenen waarom het gebruik van een set assen handig is:
# 1. **Flexibiliteit**: Met een set assen kun je meerdere tekeningen en visuele elementen op hetzelfde plotvlak plaatsen. Dit stelt je in staat om complexe tekeningen te maken door verschillende elementen samen te voegen.
# 2. **Coördinatensysteem**: Een set assen creëert een gestandaardiseerd coördinatensysteem waarin je kunt tekenen. Je kunt de x- en y-coördinaten van je visuele elementen aangeven op basis van dit coördinatensysteem.
# 3. **Opmaak en aanpassing**: Met een set assen kun je de eigenschappen van het plotvlak aanpassen, zoals de limieten van de assen, de titels, de assenlabels, de achtergrondkleur en meer. Dit geeft je controle over het uiterlijk van je tekening.
# 4. **Overlappende elementen**: Wanneer je verschillende elementen op een plotvlak wilt plaatsen, zoals lijnen en vormen, kun je met een set assen bepalen welke elementen bovenop andere elementen worden getekend. Dit is handig wanneer je bijvoorbeeld een lijn wilt tekenen die bovenop een cirkel wordt getekend.
# 5. **Herbruikbaarheid**: Je kunt dezelfde set assen gebruiken om meerdere tekeningen te maken zonder steeds opnieuw de eigenschappen van het plotvlak te hoeven instellen.
# In het voorbeeld dat ik eerder gaf, gebruikten we een set assen om de boom te tekenen. We kunnen de coördinaten van de stam, tak en het blaadje eenvoudig aangeven in het coördinatensysteem van de assen, en we kunnen de opmaak en eigenschappen van het plotvlak aanpassen om de tekening te verbeteren.

import matplotlib.pyplot as plt

# Creëer een nieuw figuur en een set van assen
fig, ax = plt.subplots()
plt.pause(1)
# Teken de stam van de boom
ax.plot([0, 0], [0, 0.5], color='chocolate', linewidth=20)
plt.pause(1)
# Teken de tak van de boom
ax.plot([0, 0.2], [0.5, 0.7], color='brown', linewidth=10)
plt.pause(1)
# Teken het blaadje
leaf = plt.Circle((0.2, 0.7), 0.1, color='green')
ax.add_artist(leaf)
plt.pause(1)
# Stel de limieten van de plot in
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
# Verberg de assen
ax.axis('off')
# Toon de plot
plt.show()
