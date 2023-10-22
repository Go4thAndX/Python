# In dit voorbeeld wordt een verticale lijn getekend vanuit het opgegeven startpunt (x_coord, y_coord) omhoog met de opgegeven lengte. We stellen de limieten van zowel de x-as als de y-as in om ervoor te zorgen dat de grafiek de lijn volledig weergeeft.

import matplotlib.pyplot as plt

# Gegevens voor de lijn
x_coord = 1  # x-coördinaat van het startpunt
y_coord = 1  # y-coördinaat van het startpunt
lengte = 4  # Lengte van de lijn omhoog

# Bereken eindpunt van de lijn
end_y = y_coord + lengte

# Teken de lijn
plt.plot([x_coord, x_coord], [y_coord, end_y], color='b', linewidth=2)
plt.xlim(0, max(x_coord, end_y + 1))  # Aanpassen van de x-as limieten
plt.ylim(0, max(x_coord, end_y + 1))  # Aanpassen van de y-as limieten
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Verticale lijn vanuit een punt met lengte omhoog')
plt.grid()
plt.show()
