# In dit voorbeeld wordt de plot-functie gebruikt om een rechte lijn te trekken tussen het startpunt en het eindpunt. We passen nog steeds de limieten van de x-as en y-as aan om ervoor te zorgen dat de assen in overeenstemming zijn en de lijn correct wordt weergegeven.

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
plt.plot([start_punt[0], end_punt[0]], [start_punt[1], end_punt[1]], color='b', linewidth=2)
plt.xlim(0, lengte)  # Aanpassen van de x-as limieten
plt.ylim(0, lengte)  # Aanpassen van de y-as limieten
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Lijn vanuit een punt met lengte en hoek')
plt.grid()
plt.show()
