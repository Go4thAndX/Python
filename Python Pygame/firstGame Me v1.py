# firstGame.py Versie 1.
# Jan George Koomen
# 2023-07-29
# Creeren scherm
# Creeren klasse Shape met 1 sub-klasse Rectangle en sub-klasse Circle
# Creeren instantie rectangle1 en instantie circle1
# Creeren while loop:
# De rectangle1 beweegt van een bepaald punt naar rechts met een bepaalde snelheid en bij het bereiken van het einde van het scherm veranderd de richting van de beweging 180 graden.
# De circle1 beweegt van een bepaald punt naar rechts met een bepaalde snelheid en bij het bereiken van het einde van het scherm veranderd de richting van de beweging 180 graden.

import pygame

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")


# Coordinaten beginnen in de linkerbovenhoek met (0, 0)
class Shape:
    def __init__(self, x_coor, y_coor, mov) -> None:
        # Starpunt x coordinaat vorm
        self.x_coor = x_coor
        # Starpunt y coordinaat vorm
        self.y_coor = y_coor
        # Verplaatsing in pixels
        self.mov = mov


# Sub klasse van klasse Shapes
class Rectangle(Shape):
    def __init__(self, x_coor, y_coor, mov, width, height, ) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.width = width
        self.height = height


# Sub klasse van klasse Shapes
class Circle(Shape):
    def __init__(self, x_coor, y_coor, mov, radius) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.radius = radius


# Instantie van Rectangle
rectangle1 = Rectangle(250, 200, 1, 40, 60)

# Instantie van Circle
circle1 = Circle(200, 250, 2, 30)

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Verander de bewegingsrichting
    if rectangle1.x_coor + rectangle1.width > win_width or rectangle1.x_coor < 0:
        rectangle1.mov *= -1

    rectangle1.x_coor += rectangle1.mov
    # Verander de bewegingsrichting
    if circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
        circle1.mov *= -1  
        
    circle1.x_coor -= circle1.mov

# Opvullen van het scherm met de kleur zwart als we een vorm getekend hebben
    win.fill((0, 0, 0))

    pygame.draw.rect(
        win,
        (255, 0, 0),
        (rectangle1.x_coor, rectangle1.y_coor, rectangle1.width, rectangle1.height),
    )
    pygame.draw.circle(win, (0, 255, 0), (circle1.x_coor, circle1.y_coor), circle1.radius)
    pygame.display.update()

pygame.quit()
