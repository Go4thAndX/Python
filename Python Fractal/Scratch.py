import matplotlib.pyplot as plt
import colorsys

# Aantal tussenliggende stappen
num_steps = 50

# Lijst om kleuren op te slaan
colors = []

# Creëer kleurovergang van rood naar groen naar blauw
for i in range(num_steps):
    # Bereken de overgangspositie tussen rood en groen
    red_to_green = i / (num_steps - 1)
    # Bereken de overgangspositie tussen groen en blauw
    green_to_blue = i / (num_steps - 1)
    
    # Converteer overgangsposities naar RGB met behulp van colorsys
    r, _, _ = colorsys.hsv_to_rgb(0, 1, 1 - red_to_green)
    _, g, _ = colorsys.hsv_to_rgb(1/3, 1, 1 - green_to_blue)
    _, _, b = colorsys.hsv_to_rgb(2/3, 1, green_to_blue)
    
    # Voeg de kleur toe aan de lijst
    colors.append((r, g, b))

# Plot kleurverloop
plt.imshow([colors], aspect='auto')
plt.xticks([])  # Verberg x-as labels
plt.yticks([])  # Verberg y-as labels
plt.title("Geleidelijke kleurovergang")
plt.show()
