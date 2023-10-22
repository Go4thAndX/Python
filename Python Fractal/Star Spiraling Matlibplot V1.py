import matplotlib.pyplot as plt
import math

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

# Genereer de lijnen
for _ in range(num_lines):
    # Bereken het eindpunt van de huidige lijn
    end_x, end_y = calculate_new_point(x_coords[-1], y_coords[-1], angle_degrees, length_factor)

    # Voeg de eindpunten toe aan de lijsten
    x_coords.extend([x_coords[-1], end_x])
    y_coords.extend([y_coords[-1], end_y])

    # Verhoog de lengte voor de volgende lijn
    length_factor += 10

    # Pas de draaihoek aan voor de volgende lijn
    angle_degrees -= 144

# Plot de lijnfiguur
plt.plot(x_coords, y_coords, color='blue')
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Figuur volgens specificaties')
plt.show()
