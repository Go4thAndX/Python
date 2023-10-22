import matplotlib.pyplot as plt
import numpy as np
import colorsys

# Number of sides
n = 50

# Set starting colors
start_color = colorsys.rgb_to_hsv(135/255, 206/255, 235/255)  # Light Blue
end_color = colorsys.rgb_to_hsv(0/255, 0/255, 139/255)       # Dark Blue

# Create a new figure and axis
fig, ax = plt.subplots()

# Loop to draw a side
for i in range(n):
    # Calculate color for current step
    curr_color = (
        start_color[0] - (start_color[0] - end_color[0]) * i / n,
        start_color[1] - (start_color[1] - end_color[1]) * i / n,
        start_color[2] - (start_color[2] - end_color[2]) * i / n
    )
    
    # Convert HSV to RGB
    rgb_color = colorsys.hsv_to_rgb(*curr_color)
    
    # Set pen color
    color = [c * 255 for c in rgb_color]
    int_color = [int(num) for num in color]
    rgb_color = "#{:02X}{:02X}{:02X}".format(*int_color)
    
    # Draw line segment
    ax.plot([0, np.cos(2 * np.pi * i / n) * i * 10],
            [0, np.sin(2 * np.pi * i / n) * i * 10],
            color=rgb_color)

# Set aspect ratio to be equal, and remove axes
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')

# Show the plot
plt.show()
