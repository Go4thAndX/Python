import turtle
import math

# Maak een Turtle-scherm
screen = turtle.Screen()

# Stel de achtergrondkleur in
screen.bgcolor("black")

# Maak een Turtle-object
t = turtle.Turtle()

# Stel de beginpositie en oriëntatie in
t.penup()
t.goto(-100, 0)
t.pendown()
t.pencolor("white")
t.pensize(3)

# Maak een functie om de golvende tekst te tekenen
def draw_text(text, x, y):
    amplitude = 20
    period = 40
    y_scale = 15
    for i in range(len(text)):
        t.penup()
        t.goto(x+i*20, y+amplitude*math.sin(i*math.pi/period)*y_scale)
        t.pendown()
        t.write(text[i], font=("Arial", 24, "bold"))

# Roep de functie aan om de golvende tekst te tekenen
draw_text("Hello World !", -100, 0)

# Houd het scherm open totdat de gebruiker het sluit
turtle.done()
