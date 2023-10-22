import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

"""
1. Eerst wordt een set assen gemaakt. 
2. Vervolgens worden de vertices gedefinieerd. Dit zijn de hoekpunten van de figuur, waarbij (0,0) linksonder is en (1,1) rechtsboven.
3. Daarna worden de codes gedefinieerd, die aangeven welke lijn tussen welke punten getrokken moet worden.
4. Vervolgens wordt de figuur gemaakt met de gedefinieerde hoekpunten en codes.
5. Als laatste wordt de figuur geplot.
"""

ax = plt.gca()

vertices = [(0.2, 0.2), (0.5, 0.8), (0.8, 0.2), (0.2, 0.2)]
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
path = Path(vertices, codes)
patch = patches.PathPatch(path, edgecolor='black', linewidth=2, facecolor='orange')
ax.add_patch(patch)

# Definieer de hoekpunten van de vorm
hoekpunten = [(0.7, 0.7), (0.9, 0.9), (0.6, 0.9), (0.7, 0.7)]
# Definieer het type verplaatsingen tussen de punten
verplaatsingstypes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
# Creëer het pad van de vorm met behulp van de hoekpunten en verplaatsingstypes
vorm_pad = Path(hoekpunten, verplaatsingstypes)
# Maak een 'patch' object van de vorm met bepaalde eigenschappen
vorm_patch = patches.PathPatch(vorm_pad, edgecolor='blue', linewidth=4, facecolor='red')
# Voeg de 'patch' toe aan de assen om de vorm te tonen
ax.add_patch(vorm_patch)

plt.show()