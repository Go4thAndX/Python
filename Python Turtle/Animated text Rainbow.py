import turtle

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

# Maak een lijst met kleuren
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Maak een functie om de regenboogtekst te tekenen
def draw_text(text, x, y):
    for i in range(len(text)):
        t.penup()
        t.goto(x+i*20, y)
        t.pendown()
        t.pencolor(colors[i%len(colors)])
        t.write(text[i], font=("Arial", 24, "bold"))

# Roep de functie aan om de regenboogtekst te tekenen
draw_text("Hello World !", -100, 0)

# Houd het scherm open totdat de gebruiker het sluit
turtle.done()
