# firstGame.py Versie 2.
# Jan George Koomen
# 2023-07-30
# Creeren scherm
# Creeren klasse Shape met 1 sub-klasse Rectangle en sub-klasse Circle
# Creeren instantie rectangle1 en instantie circle1
# Creeren while loop:
# Creeren functie die vormen laten bewegen in een willekeurige richting naar links, rechts, boven of beneden
# totdat ze het eind van het scherm bereiken

import pygame
import random

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")


# Coordinaten beginnen in de linkerbovenhoek met (0, 0)
class Shape:
    def __init__(self, x_coor, y_coor, mov) -> None:
        # Startpunt x coordinaat vorm
        self.x_coor = x_coor
        # Startpunt y coordinaat vorm
        self.y_coor = y_coor
        # Verplaatsing in pixels
        self.mov = mov


# Sub klasse van klasse Shape
class Rectangle(Shape):
    def __init__(self, x_coor, y_coor, mov, width, height, ) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.width = width
        self.height = height


# Sub klasse van klasse Shape
class Circle(Shape):
    def __init__(self, x_coor, y_coor, mov, radius) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.radius = radius


# Instantie van Rectangle
rectangle1 = Rectangle(250, 200, 10, 40, 60)

# Instantie van Circle
circle1 = Circle(200, 250, 10, 30)

run = True
while run:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # TODO Code aanpassen zodat beide shapes willekeurig naar links, rechts, boven of beneden kunnen bewegen
    def direction():
        move = ["left", "right", "up", "down"]
        rand_move_rectangle = random.choice(move)
        rand_move_circle = random.choice(move)

        return rand_move_rectangle, rand_move_circle


    move_rectangle = direction()[0]
    move_circle = direction()[1]

    for i in range(5):

        if move_rectangle == "left":
            # Verander de bewegingsrichting
            if rectangle1.x_coor + (rectangle1.width / 2) > win_width or rectangle1.x_coor < 0:
                rectangle1.mov *= -1

            rectangle1.x_coor -= rectangle1.mov

        if move_rectangle == "right":
            # Verander de bewegingsrichting
            if rectangle1.x_coor + (rectangle1.width / 2) > win_width or rectangle1.x_coor < 0:
                rectangle1.mov *= -1

            rectangle1.x_coor += rectangle1.mov

        if move_rectangle == "up":
            # Verander de bewegingsrichting
            if rectangle1.y_coor + (rectangle1.height / 2) > win_height or rectangle1.y_coor < 0:
                rectangle1.mov *= -1

            rectangle1.y_coor += rectangle1.mov

        if move_rectangle == "down":
            # Verander de bewegingsrichting
            if rectangle1.y_coor + (rectangle1.height / 2) > win_height or rectangle1.y_coor < 0:
                rectangle1.mov *= -1

            rectangle1.y_coor -= rectangle1.mov

        if move_circle == "left":
            # Verander de bewegingsrichting
            if circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
                circle1.mov *= -1

            circle1.x_coor -= circle1.mov

        if move_circle == "right":
            # Verander de bewegingsrichting
            if circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
                circle1.mov *= -1

            circle1.x_coor += circle1.mov

        if move_circle == "up":
            # Verander de bewegingsrichting
            if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0:
                circle1.mov *= -1

            circle1.y_coor += circle1.mov

        if move_circle == "down":
            # Verander de bewegingsrichting
            if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0:
                circle1.mov *= -1

            circle1.y_coor -= circle1.mov

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
