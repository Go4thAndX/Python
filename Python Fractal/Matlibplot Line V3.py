# In dit script wordt eerst het eindpunt van de lijn berekend met behulp van de trigonometrische functies np.cos() en np.sin() voor de x- en y-coördinaten van het eindpunt, respectievelijk. Vervolgens wordt een rechte lijn getekend tussen het beginpunt en het eindpunt met behulp van de plot-functie. De grid()-functie wordt gebruikt om een raster in de grafiek weer te geven.

import matplotlib.pyplot as plt
import numpy as np

# Gegevens voor de lijn
start_punt = [0, 0]  # Beginpunt van de lijn
lengte = 5  # Lengte van de lijn
hoek_graden = 30  # Hoek in graden

# Converteer de hoek naar radialen
hoek_rad = np.radians(hoek_graden)

# Bereken eindpunt van de lijn
end_punt = [start_punt[0] + lengte * np.cos(hoek_rad), start_punt[1] + lengte * np.sin(hoek_rad)]

# Teken de lijn
plt.figure(figsize=(5, 5))
plt.plot([start_punt[0], end_punt[0]], [start_punt[1], end_punt[1]], marker='o')
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Lijn vanuit een punt met lengte en hoek')
plt.grid()

plt.show()
