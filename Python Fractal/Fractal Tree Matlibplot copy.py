import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', 'box')

# ax.axis('off')

# Draw a tree
start_x = 0
start_y = 0
angle = 0
length = 100

ax.plot([start_x, start_y], [start_x + length, start_y + length], linewidth=2)

# Show the plot
plt.show()
