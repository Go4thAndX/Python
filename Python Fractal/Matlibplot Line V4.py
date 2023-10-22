# In dit voorbeeld wordt de quiver-functie gebruikt om een vectorpijl te tekenen die begint bij het startpunt en eindigt bij het berekende eindpunt. We passen de limieten van zowel de x-as als de y-as aan om ervoor te zorgen dat de assen in overeenstemming zijn en de lijn correct wordt weergegeven. De angles='xy' en scale_units='xy' parameters zorgen ervoor dat de hoek en de schaal van de pijl in overeenstemming zijn met het coördinatensysteem.

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

# Teken de lijn als een vectorpijl
plt.figure(figsize=(5, 5))
plt.quiver(start_punt[0], start_punt[1], end_punt[0] - start_punt[0], end_punt[1] - start_punt[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.xlim(0, lengte)  # Aanpassen van de x-as limieten
plt.ylim(0, lengte)  # Aanpassen van de y-as limieten
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Lijn vanuit een punt met lengte en hoek')
plt.grid()
plt.show()
