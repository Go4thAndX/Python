# TODO Mogelijk verbeteren van de afstand tussen de letters afhankelijk van
#  de letter breedte in pixels
# TODO De breedte van het turtle screen afhankelijk maken de breedte van de
#  text string
import turtle
import random

# Maak een functie om de tekst te tekenen en te animeren
# def draw_text(text, x, y, replace_x, text_font, color_text,
#               color_dots, pen_size_dots, colors_list):
def draw_text(text, x, y, replace_x, text_font,
              pen_size_dots, colors_list):
    var = True

    for i in range(len(text)):

        if i % 5 == 0:
            var = not var
        t.penup()
        x_position = x + (i * replace_x)
        t.goto(x_position, y)
        # print(x_position, end=" ")
        t.pendown()
        t.pencolor(random.choice(colors_list))
        t.write(text[i], font=text_font)
        t.pensize(pen_size_dots)

        if not var:
            for j in range(5):
                t.pencolor(random.choice(colors_list))
                # draait de turtle 5 graden naar rechts(met de klok mee)
                t.right(5)
                # verplaats de turtle 5 pixels naar voren in de huidige richting
                t.forward(5)
        else:
            for j in range(5):
                t.pencolor(random.choice(colors_list))
                # draait de turtle 5 graden naar links(tegen de klok in)
                t.left(5)
                # verplaats de turtle 5 pixels naar voren in de huidige richting
                t.forward(5)
    t.hideturtle()


# Maak een Turtle-scherm
screen = turtle.Screen()

# Stel de achtergrondkleur in
screen.bgcolor("grey")

# Maak een Turtle-object
t = turtle.Turtle()

# Stel de grootte van het scherm in
turtle.setup(1600, 200)

text = "Hello World ! It's nice to code"
text_font = ("Tempus Sans ITC", 48, "bold")

colors_list = [
    "aliceblue",
    "antiquewhite",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "blanchedalmond",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkgrey",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "grey",
    "greenyellow",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgray",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "whitesmoke",
    "yellowgreen",
]

# color_text = "color"
# color_dots = "color"
pen_size_dots = 10
# Verplaatsing van het volgende karakter in de x-richting in pixels
replace_x = 50
# Bepalen van de lengte van de string om zo het startpunt te kunnen bepalen
# van de animatie
starting_x = -(len(text) * replace_x / 2)
# input_text = input("Type a text: ")
# Roep de functie aan om de tekst te tekenen en te animeren
draw_text(text, starting_x, 0, replace_x, text_font,
          pen_size_dots, colors_list)
# draw_text(text, starting_x, 0, replace_x, text_font, color_text,
#            color_dots, pen_size_dots)
# Houd het scherm open totdat de gebruiker het sluit
turtle.done()
