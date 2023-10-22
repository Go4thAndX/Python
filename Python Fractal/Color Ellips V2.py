import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs

fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_axis_off()
ax.set_facecolor('black')

def draw_ellips(center_x, center_y, color, shift_x, shift_y):
    angle = np.linspace(0, 2 * np.pi, 100)
    a = 200  # Grote as
    b = 100  # Kleine as
    x = a * np.cos(angle) + center_x + shift_x
    y = b * np.sin(angle) + center_y + shift_y
    ax.plot(x, y, color=color)

num_frames = 1

def draw_frame(frame):
    ax.clear()
    
    # Kleur van de ellipsen
    color1 = cs.hsv_to_rgb(0.2, 1, 1)  # Eerste ellips kleur
    color2 = cs.hsv_to_rgb(0.6, 1, 1)  # Tweede ellips kleur
    
    # Eerste ellips op originele positie
    draw_ellips(0, 0, color1, 0, 0)
    
    # Tweede ellips met een kleine verschuiving
    draw_ellips(0, 0, color2, 10, -10)

draw_frame(0)  # Teken het frame
plt.show()
