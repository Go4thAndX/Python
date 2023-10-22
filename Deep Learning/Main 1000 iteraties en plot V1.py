# Ik probeer hier het concept van Deep Learning onder de knie te krijgen.

# Code aan passen zodat er via Matplotlib een grafische voorstelling komt die het doelpunt (rood), het start punt
# (groen) en het eerste random punt (zwart) laat zien en daarna als de code deze genereert de volgende
# random punten (blauw) die steeds dichter bij het doel komen. Om de grafische voorstelling te maken met Matplotlib,
# moeten we de punten tijdens de iteraties opslaan en ze uiteindelijk plotten.
# De lijn in blauw toont de volgorde van de punten na elke iteratie, waarbij elk nieuw punt steeds dichter bij het doel
# komt. Het doelpunt is rood, het startpunt is groen en het eerste willekeurige punt is zwart.
# Let op dat als het willekeurige punt dichter bij het doel ligt dan het startpunt, het startpunt wordt vervangen door
# het willekeurige punt.
# Het proces herhaalt zich totdat het dichtstbijzijnde punt dichter bij het doel ligt dan 1 eenheid.

# Om de random functie te kunnen gebruiken heb ik de random class nodig
import random
# Om mathematische berekeningen te kunnen doen heb ik de math class nodig
import math
# Om een grafische voorstelling te maken heb ik de matplotlib class nodig
import matplotlib.pyplot as plt

# Stel de grootte van het grid in
GRID_SIZE = 100

# Stel het aantal iteraties in
MAX_ITERATIONS = 1000

# Functie om de afstand tussen twee punten te berekenen

def afstand(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


# Kies random een punt in het grid en noem dit punt het doel
x_coord_doel = random.randint(0, GRID_SIZE)
y_coord_doel = random.randint(0, GRID_SIZE)

# Kies random nog een punt in het grid en noem dit punt de start
x_coord_start = random.randint(0, GRID_SIZE)
y_coord_start = random.randint(0, GRID_SIZE)

# Puntenlijsten voor de plot
x_coords = [x_coord_doel, x_coord_start]
y_coords = [y_coord_doel, y_coord_start]

# Voer de iteraties uit om het punt dichter bij het doel te krijgen
for i in range(MAX_ITERATIONS):
    # Kies nu random weer een punt in het grid en noem dit het random punt
    x_coord_rand = random.randint(0, GRID_SIZE)
    y_coord_rand = random.randint(0, GRID_SIZE)

    # Bepaal de afstanden tussen de punten
    abs_afst_start = afstand(x_coord_doel, y_coord_doel, x_coord_start, y_coord_start)
    abs_afst_rand = afstand(x_coord_doel, y_coord_doel, x_coord_rand, y_coord_rand)

    # Als het random punt dichter bij het doel ligt dan het start punt, dan wordt het random punt
    # het dichtstbijzijnde punt
    if abs_afst_start >= abs_afst_rand:
        x_coord_start = x_coord_rand
        y_coord_start = y_coord_rand

    # Voeg de nieuwe punten toe aan de lijsten voor de plot
    x_coords.append(x_coord_start)
    y_coords.append(y_coord_start)

    # Als de afstand minder dan 1 is, stop met itereren
    if abs_afst_start < 1:
        break

    # Print de beschrijving en coördinaten van het huidige punt
    print(f"Iteratie {i + 1}:")
    print(f"Doel Coördinaten: x = {x_coord_doel}, y = {y_coord_doel}")
    print(f"Start Coördinaten: x = {x_coord_start}, y = {y_coord_start}")
    print(f"Random Coördinaten: x = {x_coord_rand}, y = {y_coord_rand}")
    print(f"Afstand tot doel (startpunt): {abs_afst_start}")
    print(f"Afstand tot doel (random punt): {abs_afst_rand}\n")

    # Print de beschrijving en coördinaten van het huidige punt
    print(f"Iteratie {i + 1}:")
    print(f"Start Coördinaten: x = {x_coord_start}, y = {y_coord_start}")
    print(f"Afstand tot doel: {abs_afst_start}\n")

# Plot de grafiek
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, color='blue', marker='o', markersize=5, label='Dichter bij doel')
plt.scatter(x_coord_doel, y_coord_doel, color='red', marker='o', s=100, label='Doel')
plt.scatter(x_coords[1], y_coords[1], color='green', marker='o', s=100, label='Start')
plt.scatter(x_coords[-1], y_coords[-1], color='black', marker='o', s=100, label='Eind')
plt.xlim(0, GRID_SIZE)
plt.ylim(0, GRID_SIZE)
plt.xlabel('X-coördinaat')
plt.ylabel('Y-coördinaat')
plt.legend()
plt.title('Puntenbeweging naar doel')
plt.grid(True)
plt.show()
