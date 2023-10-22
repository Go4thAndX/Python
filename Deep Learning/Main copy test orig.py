# Ik probeer hier het concept van Deep Learning onder de knie te krijgen.

# Om de random functie te kunnen gebruiken heb ik de random class nodig
import random
# Om mathematische berekeningen te kunnen doen heb ik de math class nodig
import math
# Om een grafische voorstelling te maken heb ik de matplotlib class nodig
import matplotlib.pyplot as plt

# Stel ik heb een grid van 100 bij 100, en ik kies random een punt in deze grid die een x coordinaat en y coordinaat heeft en noem dit punt het doel
x_coord_doel = random.randint(0, 100)
y_coord_doel = random.randint(0, 100)
print(f"x_coord_d = {x_coord_doel}, y_coord_d = {y_coord_doel}")

# Kies random nog een punt in de grid en noem dit punt de start
x_coord_start = random.randint(0, 100)
y_coord_start = random.randint(0, 100)
print(f"x_coord_s = {x_coord_start}, y_coord_s = {y_coord_start}")

# Nu wil ik dat een volgend gekozen punt dichter bij het doel komt, hoe doe ik dat ?

# Kies nu random weer een punt in de grid en noem dit het random punt
x_coord_rand = random.randint(0, 100)
y_coord_rand = random.randint(0, 100)
print(f"x_coord_r = {x_coord_rand}, y_coord_r = {y_coord_rand}")

# Bepaal de absolute afstand in een rechte lijn tussen het start punt en het doel en tussen het random punt en het doel 
# De absolute afstand in een rechte lijn tussen twee punten is de horizontale afstand te kwadrateren de verticale afstand te kwadrateren
# en van de som van deze twee afstanden de wortel te nemen
# Als de absolute afstand in een rechte lijn tussen het start punt en het doel langer is dan de absolute afstand tussen het random punt en het doel
# dan ligt het random punt dichter bij het doel, dan het start punt
abs_afst_start = math.sqrt(pow((x_coord_doel - x_coord_start), 2) + pow((y_coord_doel - y_coord_start), 2))
print(f"De afstand van het start punt tot het doel is {abs_afst_start}")
abs_afst_rand = math.sqrt(pow((x_coord_doel - x_coord_rand), 2) + pow((y_coord_doel - y_coord_rand), 2))
print(f"De afstand van het random punt tot het doel is {abs_afst_rand}")

# Als het random punt dichter bij het doel ligt dan het start punt, dan wordt het random punt het dichtsbijzijnde punt
# Als het random punt verder van het doel ligt dan het start punt, dan blijft het start punt, het dichtsbijzinde punt
# Kies nu random weer een punt en herhaal dit net zolang totdat het random punt het dichtsbijzijnde punt is
# Herhaal dit totdat het nieuwe dichtsbijzijnde punt zo dicht bij is dat de afstand minder dan 1 is
nieuw_start = True

while nieuw_start:
        
    if abs_afst_start >= abs_afst_rand:
        x_coord_start = x_coord_rand
        y_coord_start = y_coord_rand
        nieuw_start = False
        print(f"Het nieuwe dichtsbijzijnde punt is nu x_coord_s = {x_coord_start}, y_coord_s = {y_coord_start}")
    else:
        print(f"We kiezen een nieuw random punt en bepalen of dit het dichtsbijzijnde punt wordt")
        x_coord_rand = random.randint(0, 100)
        y_coord_rand = random.randint(0, 100)
        print(f"Het nieuwe random punt wordt x_coord_r = {x_coord_rand}, y_coord_r = {y_coord_rand}")
        abs_afst_rand = math.sqrt(pow((x_coord_doel - x_coord_rand), 2) + pow((y_coord_doel - y_coord_rand), 2))
        print(f"De afstand van het random punt tot het doel is {abs_afst_rand}")



    # Oorspronkelijke startpunt en eerste random punt
    # x_coord_start = random.randint(0, 100)
    # y_coord_start = random.randint(0, 100)
    # x_coord_rand = random.randint(0, 100)
    # y_coord_rand = random.randint(0, 100)
    #
    # # Het doelpunt
    # x_coord_doel = random.randint(0, 100)
    # y_coord_doel = random.randint(0, 100)

    # Maak een lijst om de x-coördinaten van het random punt bij te houden tijdens de iteraties
    x_coords = [x_coord_start]

    # Maak een lijst om de y-coördinaten van het random punt bij te houden tijdens de iteraties
    y_coords = [y_coord_start]

    while nieuw_start:
        if abs_afst_start >= abs_afst_rand:
            x_coord_start = x_coord_rand
            y_coord_start = y_coord_rand
            nieuw_start = False
        else:
            x_coord_rand = random.randint(0, 100)
            y_coord_rand = random.randint(0, 100)
            abs_afst_rand = math.sqrt(pow((x_coord_doel - x_coord_rand), 2) + pow((y_coord_doel - y_coord_rand), 2))
            x_coords.append(x_coord_rand)
            y_coords.append(y_coord_rand)

    # Plot de grafische voorstelling
    plt.figure(figsize=(8, 8))

    # Plot het doelpunt
    plt.scatter(x_coord_doel, y_coord_doel, color='red', label='Doelpunt')

    # Plot het startpunt
    plt.scatter(x_coord_start, y_coord_start, color='green', label='Startpunt')

    # plot het random punt inclusief het eerste random punt
    plt.scatter(x_coords, y_coords, color='blue', label='Random punt')

    plt.legend()
    plt.xlabel('X-coördinaat')
    plt.ylabel('Y-coördinaat')
    plt.title('Grafische voorstelling van random punt naar doelpunt')
    plt.grid(True)

    # Zorg ervoor dat de grafiek altijd het gehele coördinatenstelsel van 100 bij 100 laat zien
    plt.axis([0, 100, 0, 100])

    plt.show()


