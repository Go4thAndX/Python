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
t.pencolor("white")
t.pensize(3)

# Maak een functie om de stippeltekst te tekenen
def draw_text(text, x, y):
    for i in range(len(text)):
        t.penup()
        t.goto(x+i*20, y)
        t.pendown()
        for j in range(10):
            t.forward(2)
            t.penup()
            t.forward(2)
            t.pendown()
        t.write(text[i], font=("Arial", 24, "bold"))

# Roep de functie aan om de stippeltekst te tekenen
draw_text("Hello World !", -100, 0)

# Houd het scherm open totdat de gebruiker het sluit
turtle.done()

