# In dit voorbeeld worden 2 lijnen getekend vanuit het opgegeven startpunt (x_coord_begin, y_coord_begin) met de opgegeven verplaatsing in zowel de x- als de y-richting. Waarbij het eindpunt van de 1e lijn het startpunt is van de 2e lijn. We stellen de limieten van zowel de x-as als de y-as in om ervoor te zorgen dat de grafiek de lijnen volledig weergeeft.

import matplotlib.pyplot as plt

# Gegevens voor de eerste lijn
x_coord_begin = 0
x_coord_start = x_coord_begin
y_coord_begin = 0
y_coord_start = y_coord_begin

move_x_1 = -4
x_coord_end_1 = x_coord_start + move_x_1
move_y_1 = 4
y_coord_end_1 = y_coord_start + move_y_1

# Gegevens voor de tweede lijn
x_coord_start_2 = x_coord_end_1
y_coord_start_2 = y_coord_end_1
move_x_2 = 3
x_coord_end_2 = x_coord_start_2 + move_x_2
move_y_2 = 3
y_coord_end_2 = y_coord_start_2 + move_y_2

# Bepaal de maximale absolute waarden van x en y coördinaten
max_abs_x = max(abs(x_coord_start), abs(x_coord_end_1), abs(x_coord_start_2), abs(x_coord_end_2))
max_abs_y = max(abs(y_coord_start), abs(y_coord_end_1), abs(y_coord_start_2), abs(y_coord_end_2))

# Bereken de marge om de limieten te vergroten, zodat de lijnen niet de randen raken
margin = 1.0

# Pas de limieten aan met de marge en de maximale absolute waarden
plt.xlim(-max_abs_x - margin, max_abs_x + margin)
plt.ylim(-max_abs_y - margin, max_abs_y + margin)

# Teken de eerste lijn
plt.plot([x_coord_start, x_coord_end_1], [y_coord_start, y_coord_end_1], color='blue', linewidth=2)

# Teken de tweede lijn
plt.plot([x_coord_start_2, x_coord_end_2], [y_coord_start_2, y_coord_end_2], color='red', linewidth=2)

plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Twee lijnen met verbonden eindpunt en beginpunt')
plt.grid()
plt.show()
