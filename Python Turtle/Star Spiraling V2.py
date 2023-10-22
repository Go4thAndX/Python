'''In dit script gebruiken we de colorsys module om kleurovergangen te berekenen tussen het startkleur (lichtblauw) en het eindkleur (donkerblauw) in het HSV (Hue, Saturation, Value) kleurmodel. We passen geleidelijk de kleur aan terwijl we door de lus itereren en tekenen elke zijde met de bijbehorende kleur. Dit creëert een vloeiende overgang van lichtblauw naar donkerblauw tijdens het tekenen van de lijnen.
'''

import turtle
import colorsys

# Number of sides
n = 50

# Creating instance of turtle
pen = turtle.Turtle()

# Set starting colors
start_color = colorsys.rgb_to_hsv(135/255, 206/255, 235/255)  # Light Blue
end_color = colorsys.rgb_to_hsv(0/255, 0/255, 139/255)       # Dark Blue

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
    pen.color(rgb_color)
    
    # Drawing side of length i*10
    pen.forward(i * 10)
    
    # Changing direction of pen by 144 degrees clockwise
    pen.right(144)

# Closing the instance
turtle.done()
