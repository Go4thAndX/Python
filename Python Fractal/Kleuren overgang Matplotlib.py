# Dit script laat zien hoe je een kleurovergang van drie kleuren kunt maken met Matplotlib, zonder gebruik te maken van een colormap.
# Voor een mooie soepele kleurovergang moet het aantal tussenligende stappen minimaal 10 zijn.

import matplotlib.pyplot as plt

# Aantal tussenliggende stappen
num_steps = 10

# Lijst om kleuren op te slaan
colors = []

# De RGB-waarde van rood is (255, 0, 0)
# De RGB-waarde van groen is (0, 255, 0)
# De RGB-waarde van blauw is (0, 0, 255)

# Stel de start- en eindkleur in
start_color = (255, 0, 0)
between_color = (0, 255, 0)  
end_color = (0, 0, 255)

# Creëer kleurovergang
for i in range(num_steps):
    # Kleurverloop van rood naar groen
    if i <= num_steps / 2:
        curr_color = (
            start_color[0] - (start_color[0] * i * 2 / num_steps),
            between_color[1] * i * 2 / num_steps, 0
        )
    # Kleurverloop van groen naar blauw
    else:
        curr_color = (
            0,
            between_color[1] * (2 - (i * 2 / num_steps)),
            (end_color[2] * i * 2 / num_steps) - end_color[2]    
        ) 
    
    # Converteer de kleur tuple van float naar int
    int_color = tuple(int(num) for num in curr_color) 
    colors.append(int_color)

# Plot kleurverloop
plt.figure(figsize=(10, 1))
for i, color in enumerate(colors):
    plt.fill_between([i, i+1], 0, 1, color=[c/255 for c in color])

plt.axis('off')
plt.show()
