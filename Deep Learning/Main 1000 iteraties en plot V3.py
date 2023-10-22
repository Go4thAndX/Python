# Main 1000 iteraties en plot V3.py
# Jan George Koomen
# Nederland, Goes, 07-08-2023
# Zie voor commentaar het file: [Deep Learning.txt]

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


verkleinings_factor = 0.99
verkleinings_factor = float(input("Welke stapgrootte wilt u gebruiken 0.01 - 0.99 : "))
afstand_doel = 1
afstand_doel = int(input("Welke afstand tot het doel wilt u gebruiken om het itereren te stoppen 1 - 10 : "))

# Kies random een punt in het grid en noem dit punt het doel.
x_coord_doel = random.randint(1, GRID_SIZE - 1)
y_coord_doel = random.randint(1, GRID_SIZE - 1)

# Kies random nog een punt in het grid en noem dit punt de start.
x_coord_start = random.randint(1, GRID_SIZE - 1)
y_coord_start = random.randint(1, GRID_SIZE - 1)

# Puntenlijsten voor de plot
x_coords = [x_coord_doel, x_coord_start]
y_coords = [y_coord_doel, y_coord_start]

# Stel de initiële stapgrootte in (maximale afstand dat het startpunt kan bewegen)
stapgrootte = max(GRID_SIZE - 1, GRID_SIZE - 1)

# Voer de iteraties uit om het punt dichter bij het doel te krijgen
for iteraties in range(MAX_ITERATIONS):
    # Kies nu random een hoek en bereken het nieuwe punt binnen de stapgrootte vanaf het startpunt
    while True:
        hoek = 2 * math.pi * random.random()
        stap_x = int(stapgrootte * math.cos(hoek))
        stap_y = int(stapgrootte * math.sin(hoek))
        x_coord_rand = max(1, min(GRID_SIZE - 1, x_coord_start + stap_x))
        y_coord_rand = max(1, min(GRID_SIZE - 1, y_coord_start + stap_y))
        # Controleer of het nieuwe punt binnen het grid ligt
        if 0 <= x_coord_rand < GRID_SIZE - 1 and 1 <= y_coord_rand < GRID_SIZE - 1:
            break

    # Bepaal de afstanden tussen de punten
    abs_afst_start = afstand(x_coord_doel, y_coord_doel, x_coord_start, y_coord_start)
    abs_afst_rand = afstand(x_coord_doel, y_coord_doel, x_coord_rand, y_coord_rand)

    # Als het random punt dichter bij het doel ligt dan het start punt,
    # dan wordt het random punt het dichtstbijzijnde punt.
    if abs_afst_start >= abs_afst_rand:
        x_coord_start = x_coord_rand
        y_coord_start = y_coord_rand

    # Voeg de nieuwe punten toe aan de lijsten voor de plot.
    x_coords.append(x_coord_start)
    y_coords.append(y_coord_start)

    # Als de afstand minder dan (initieel 1) is, stop met itereren.
    if abs_afst_start < afstand_doel:
        break
    # Pas de verkleiningsfactor (initieel 0.99) aan om het gedrag aan te passen.
    # Verklein de stapgrootte voor de volgende iteratie.
    stapgrootte *= verkleinings_factor

# Print de beschrijving en coördinaten van het huidige punt
    print(f"Iteratie {iteraties+1}:")
    print(f"Doel coördinaten: x = {x_coord_doel}, y = {y_coord_doel}")
    print(f"Start coördinaten: x = {x_coord_start}, y = {y_coord_start}")
    print(f"Random coördinaten: x = {x_coord_rand}, y = {y_coord_rand}")
    print(f"Afstand tot doel (startpunt): {abs_afst_start}")
    print(f"Afstand tot doel (random punt): {abs_afst_rand}\n")

# Print het aantal uitgevoerde iteraties.
print(f"Aantal iteraties: {iteraties+1}")

# Plot de grafiek.
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, color='yellow', marker='o', markersize=5, label='Dichter bij doel')
plt.scatter(x_coord_doel, y_coord_doel, color='red', marker='o', s=100, label='Doel')
plt.scatter(x_coords[1], y_coords[1], color='green', marker='o', s=100, label='Start')
plt.scatter(x_coords[-1], y_coords[-1], color='blue', marker='o', s=100, label='Eind')
plt.xlim(0, GRID_SIZE)
plt.ylim(0, GRID_SIZE)
plt.xlabel('X-coördinaat')
plt.ylabel('Y-coördinaat')
plt.legend()
plt.title('Puntenbeweging naar doel')
plt.grid(True)

# Voeg de tekst met de variabele waarden toe aan de grafiek
plt.text(2, 105, f"Verkleinings_factor: {verkleinings_factor}", fontsize=10, color='black')
plt.text(2, 103, f"Minimale afstand tot doel: {afstand_doel}", fontsize=10, color='black')
plt.text(2, 101, f"Iteraties: {iteraties+1}", fontsize=10, color='black')

plt.tight_layout
plt.show()
