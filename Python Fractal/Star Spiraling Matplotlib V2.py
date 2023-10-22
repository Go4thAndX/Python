import matplotlib.pyplot as plt
import math
import colorsys

# Functie om een nieuw punt te berekenen gegeven startpunt, hoek en lengte
def calculate_new_point(x, y, angle_degrees, length):
    angle_radians = math.radians(angle_degrees)
    new_x = x + length * math.cos(angle_radians)
    new_y = y + length * math.sin(angle_radians)
    return new_x, new_y

# Beginpunt en lijnparameters
start_x = 0
start_y = 0
angle_degrees = 144
length_factor = 10
num_lines = 50

# Lijsten om x- en y-coördinaten van de lijn te volgen
x_coords = [start_x]
y_coords = [start_y]

# Stel de start- en eindkleur in
start_color = colorsys.rgb_to_hsv(255/255, 0/255, 0/255)
end_color = colorsys.rgb_to_hsv(0/255, 0/255, 255/255)

# Genereer de lijnen en de kleuren
for i in range(num_lines):
    # Bereken het eindpunt van de huidige lijn
    end_x, end_y = calculate_new_point(x_coords[-1], y_coords[-1], angle_degrees, length_factor)

    # Voeg de eindpunten toe aan de lijsten
    x_coords.extend([x_coords[-1], end_x])
    y_coords.extend([y_coords[-1], end_y])

    # Bereken de huidige kleur
    curr_color = (
        start_color[0] - (start_color[0] - end_color[0]) * i / num_lines,
        start_color[1] - (start_color[1] - end_color[1]) * i / num_lines,
        start_color[2] - (start_color[2] - end_color[2]) * i / num_lines
    )
    
    # Converteer de kleur van HSV naar RGB
    rgb_color = colorsys.hsv_to_rgb(*curr_color)
    
    # Converteer de kleur van 0-1 naar 0-255 en van float naar int
    color = [c * 255 for c in rgb_color]
    int_color = [int(num) for num in color]
    rgb_color = "#{:02X}{:02X}{:02X}".format(*int_color)
    print(rgb_color)
    # Alleen de laatste lijnsegment toevoegen
    plt.plot(x_coords[-2:], y_coords[-2:], color=rgb_color)

    # Verhoog de lengte voor de volgende lijn
    length_factor += 10

    # Pas de draaihoek aan voor de volgende lijn
    angle_degrees -= 144

plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Figuur met RGB-kleurverloop')
plt.show()
