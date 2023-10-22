# Dit script tekent een lijn vanuit het oorsprongspunt in een polaire grafiek. Het eindpunt van de lijn wordt berekend op basis van de opgegeven lengte en hoek. Let op dat de hoek wordt omgezet van graden naar radialen met behulp van np.radians() omdat trigonometrische functies in numpy radialen verwachten.

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
plt.polar([0, hoek_rad], [0, lengte], marker='o')  # Teken een lijn van oorsprong naar eindpunt
plt.title('Lijn vanuit een punt met lengte en hoek')
plt.show()

