import random
import matplotlib.pyplot as plt
import numpy as np

# TODO: Alle waarden van de variabelen in het programma kunnen kiezen door input statements

# Function to draw the fractal tree
def draw_fractal_tree(ax, x, y, angle, length, depth):
    if depth == 0:
        return
    else:
        color_list_tree = ['chocolate', 'brown', 'saddlebrown', 'sienna', 'peru', 'burlywood', 'tan']
        color_tree = random.choice(color_list_tree)
        
        new_x = x + length * np.cos(np.radians(angle))
        new_y = y + length * np.sin(np.radians(angle))
        
        ax.plot([x, new_x], [y, new_y], color=color_tree, linewidth=2)
        
        draw_fractal_tree(ax, new_x, new_y, angle - 30, length * 0.75, depth - 1)
        draw_fractal_tree(ax, new_x, new_y, angle + 30, length * 0.75, depth - 1)
        
        # if depth <= 2:
        draw_leaf(ax, new_x, new_y)
        
        # plt.pause(0.01)

# Function to draw a leaf at the specified coordinates
def draw_leaf(ax, x, y):
    color_list_leaf = ['green', 'darkgreen', 'forestgreen', 'greenyellow', 'limegreen', 'lime', 'olivedrab']
    color_leaf = random.choice(color_list_leaf)
    leaf_size = random.uniform(2, 10)
    ax.plot(x, y, marker='o', markersize=leaf_size, color=color_leaf, linestyle='None')

# Create a blank canvas
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', 'box')
ax.axis('off')

while True:
    try:
        input_depth = int(input("Hoeveel iteraties wil je 2 - 10? "))
        if 2 <= input_depth <= 10:
            break  # Beëindig de lus als een geldige waarde is ingevoerd
        else:
            print("Het antwoord moet tussen 1 en 10 liggen. Probeer opnieuw.")
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in tussen 1 en 10.")

while True:
    try:
        input_length = int(input("Hoe lang moet de stam zijn 100 - 400 ? "))
        if 100 <= input_length <= 400:
            break  # Beëindig de lus als een geldige waarde is ingevoerd
        else:
            print("Het antwoord moet tussen 100 en 400 liggen. Probeer opnieuw.")
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in tussen 100 en 400.")
        
while True:
    try:
        input_angle = int(input("Onder welke hoek moet de boom staan 0 - 180 ? "))
        if 0 <= input_angle <= 180:
            break  # Beëindig de lus als een geldige waarde is ingevoerd
        else:
            print("Het antwoord moet tussen 0 en 180 liggen. Probeer opnieuw.")
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in tussen 0 en 180.")        

# input_leaf = input("Wil je bladeren? (y/n) ")

# input_pause = input("Wil je de boom in stappen zien? (y/n) ")
# input_pause_time = input("Hoeveel seconden wil je tussen de stappen? ")

# Draw the fractal tree
# draw_fractal_tree(ax, 0, 0, angle=input_angle + 90, length=input_length, depth=input_depth)
draw_fractal_tree(ax, 0, 0, 180, length=input_length, depth=input_depth)

# Show the plot
plt.show()
