# In dit voorbeeld wordt een lijn getekend vanuit het opgegeven startpunt (x_coord_begin, y_coord_begin) met de opgegeven verplaatsing in zowel de x- als de y-richting. We stellen de limieten van zowel de x-as als de y-as in om ervoor te zorgen dat de grafiek de lijn volledig weergeeft.

import matplotlib.pyplot as plt

# Gegevens voor de lijn

# x-coördinaat van het begintpunt
x_coord_begin = 0
x_coord_start = x_coord_begin
# y-coördinaat van het beginpunt
y_coord_begin = 0
y_coord_start = y_coord_begin

# Verplaatsing van de lijn in de x richting
move_x = -4
# Bereken eindpunt van de lijn in de x-richting
x_coord_end = x_coord_start + move_x
# Bereken eindpunt van de lijn in de y-richting
move_y = 4    
# Bereken eindpunt van de lijn in de y-richting
y_coord_end = y_coord_start + move_y


# Teken de lijn
"""
1. importeer de matplotlib.pyplot module als plt
2. maak een plot object aan
3. zet de x-coördinaat van het begin van de lijn op (0) en de x-coördinaat van het eind van de lijn op (1)
4. zet de y-coördinaa van het begin van de lijn (0) en de y-coördinaat van het eind van de lijn op (4)
5. zet de kleur van de lijn op (blauw)
6. zet de dikte van de lijn op (2)
"""
plt.plot([x_coord_start, x_coord_end], [y_coord_start, y_coord_end], color='blue', linewidth=2)

# Aanpassen van de x-as limieten
plt.xlim(-5, 5)

# Aanpassen van de y-as limieten
plt.ylim(-5, 5)

plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Lijn vanuit startpunt naar eindpunt')
plt.grid()
plt.show()
