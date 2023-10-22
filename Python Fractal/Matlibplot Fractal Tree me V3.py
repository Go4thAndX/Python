import matplotlib.pyplot as plt

# Gegevens voor de eerste lijn
x_coord_begin = 0
move_x = 0
x_coord_end = x_coord_begin + move_x
x_coord_start = x_coord_begin

y_coord_begin = 0
move_y= 10
y_coord_end = y_coord_begin + move_y
y_coord_start = y_coord_begin

# Teken de eerste lijn
plt.plot([0, 0], [-20, 10], marker = "o")
# plt.plot([x_coord_begin, x_coord_end], [y_coord_begin, y_coord_end], marker = "o")

# Coordinaten voor de volgende lijnen
for i in range(5):
    move_x = 5 + i
    x_coord_start = x_coord_end
    x_coord_end = x_coord_end + move_x
    move_y = move_y * 0.75
    y_coord_start = y_coord_end
    y_coord_end = y_coord_end + move_y
    
    plt.plot([x_coord_start, x_coord_end], [y_coord_start, y_coord_end], marker = "o", color = "red")
    
    # Bepaal de maximale absolute waarden van x en y coördinaten
    max_abs_x_1 = max(abs(x_coord_begin), abs(x_coord_end))
    max_abs_y_1= max(abs(y_coord_begin), abs(y_coord_end))
    
x_coord_end = 0
y_coord_end = 10

for i in range(5):
    move_x = 5 + i
    x_coord_start = x_coord_end
    x_coord_end = x_coord_end + move_x
    move_y = move_y * 0.75
    y_coord_start = y_coord_end
    y_coord_end = y_coord_end + move_y
    
    plt.plot([x_coord_start, x_coord_end], [y_coord_start, y_coord_end], marker = "o", color = "green")    
    
    # Bepaal de maximale absolute waarden van x en y coördinaten
    max_abs_x_2 = max(abs(x_coord_begin), abs(x_coord_end))
    max_abs_y_2= max(abs(y_coord_begin), abs(y_coord_end))

if max_abs_x_1 > max_abs_x_2:
    max_abs_x = max_abs_x_1
else:
    max_abs_x = max_abs_x_2
    
if max_abs_y_1 > max_abs_y_2:
    max_abs_y = max_abs_y_1
else:
    max_abs_y = max_abs_y_2     
    
# Bereken de marge om de limieten te vergroten, zodat de lijnen niet de randen raken
margin = max(max_abs_x, max_abs_y) * 0.1
print("margin: ", margin)

# Pas de limieten aan met de marge en de maximale absolute waarden
plt.xlim(-max_abs_x - margin, max_abs_x + margin)
plt.ylim(-max_abs_y - margin, max_abs_y + margin)

plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Lijnen met verbonden eindpunt en beginpunt')
plt.grid()    
plt.show()
