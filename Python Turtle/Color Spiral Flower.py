import turtle as t
import colorsys as cs
import time

t.setup(800, 800)
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor("black")

# Functie om een vertraging in seconden in te voegen
def delay(seconds):
    time.sleep(seconds)

for j in range(25):
    for i in range(15):
        t.color(cs.hsv_to_rgb(i/15, j/25, 1))
        t.right(90)
        t.circle(200-j*4, 90)
        t.left(90)
        t.circle(200-j*4, 90)
        t.right(180)
        t.circle(50, 24)
        # Handmatig het venster bijwerken om tekeningen te laten zien
        t.update()
        # Voeg een vertraging van 0.1 seconden toe  
        delay(0.1)

t.hideturtle()
t.done()

