import matplotlib.pyplot as plt
import numpy as np
import random

# Instellen van het figuur en de assen
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')
ax.axis('off')

# Definieer de bomen als lijnsegmenten
trees = []
x = -200

for _ in range(5):
    tree_color = random.choice(['saddlebrown', 'sienna', 'chocolate', 'maroon'])
    x += random.randint(80, 160)
    y = random.randint(-100, 100)
    tree = [(x, y)]
    trees.append((tree_color, tree))

# Functie om een tak te tekenen
def branch(ax, branch_data, branch_len):
    angle = np.radians(random.uniform(22, 30))
    shrink_factor = random.uniform(0.6, 0.9)
    size = int(branch_len / 10)

    if branch_len < 20:
        leaf_color = random.choice(['green', 'darkgreen', 'forestgreen', 'greenyellow', 'limegreen', 'lime', 'olivedrab'])
        branch_data.append(('leaf', plt.Circle((0, 0), size, color=leaf_color)))
        branch_color = random.choice(['chocolate', 'brown', 'saddlebrown', 'sienna', 'peru', 'burlywood', 'tan'])
        branch_data.append(('branch', plt.Line2D([0, 0], [0, 0], linewidth=size, color=branch_color)))

    if branch_len > 10:
        new_x = branch_len * np.sin(angle)
        new_y = branch_len * np.cos(angle)
        branch_data[-1][1].set_data([0, new_x], [0, new_y])
        ax.add_artist(branch_data[-1][1])
        branch(ax, branch_data, branch_len * shrink_factor)
        
        new_x = branch_len * np.sin(angle)
        new_y = branch_len * np.cos(angle)
        branch_data[-1][1].set_data([0, new_x], [0, -new_y])
        ax.add_artist(branch_data[-1][1])
        branch(ax, branch_data, branch_len * shrink_factor)
        
        branch_data[-1][1].set_data([0, 0], [0, -branch_len])
        ax.add_artist(branch_data[-1][1])

# Tekenen van de bomen
for color, tree_data in trees:
    branch_data = [(None, None)]
    if ax is None:
        fig, ax = plt.subplots()  # Create a new axes object
        ax.add_artist(branch_data[0][1])  # Add the artist object to the axes object
    branch(ax, branch_data, 100)

plt.show()
