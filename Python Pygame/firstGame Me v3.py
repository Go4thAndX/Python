# firstGame.py Versie 1.
# Jan George Koomen
# 2023-07-29
# Creeren scherm
# Creeren klasse Shape met 1 sub-klasse Circle
# Creeren instantie circle1
# Creeren while loop:
# De circle1 beweegt van een bepaald punt met een bepaalde snelheid in een willekeurige richting en bij het bereiken van het einde van het scherm
# veranderd de richting van de beweging willekeurig maar wel zodanig dat hij van het eind van het scherm af beweegt

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
        # Starpunt x coordinaat vorm
        self.x_coor = x_coor
        # Starpunt y coordinaat vorm
        self.y_coor = y_coor
        # Verplaatsing in pixels
        self.mov = mov


# Sub klasse van klasse Shapes
class Circle(Shape):
    def __init__(self, x_coor, y_coor, mov, radius) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.radius = radius


# Instantie van Circle
circle1 = Circle(250, 250, 1, 30)

list_direction = ["up", "right", "down", "left"]
rand_direction = random.choice(list_direction)
change_direction = (random.randint(-100, 100)) / 100
# print(change_direction)
# rand_direction = "up"

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if rand_direction == "up":
        # Verander de bewegingsrichting
        if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0 or circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
            circle1.mov *= -1
            change_direction = (random.randint(-100, 100)) / 100
                
        circle1.y_coor += circle1.mov
        circle1.x_coor += circle1.mov * change_direction
        
    if rand_direction == "right":
        # Verander de bewegingsrichting
        if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0 or circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
            circle1.mov *= -1
            change_direction = (random.randint(-100, 100)) / 100
                
        circle1.x_coor += circle1.mov
        circle1.y_coor += circle1.mov * change_direction
        
    if rand_direction == "down":
        # Verander de bewegingsrichting
        if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0 or circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
            circle1.mov *= -1
            change_direction = (random.randint(-100, 100)) / 100
                
        circle1.y_coor -= circle1.mov
        circle1.x_coor += circle1.mov * change_direction
        
    if rand_direction == "left":
        # Verander de bewegingsrichting
        if circle1.y_coor + circle1.radius > win_height or circle1.y_coor - circle1.radius < 0 or circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
            circle1.mov *= -1
            change_direction = (random.randint(-100, 100)) / 100
                
        circle1.x_coor -= circle1.mov
        circle1.y_coor += circle1.mov * change_direction

# Opvullen van het scherm met de kleur zwart als we een vorm getekend hebben
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (0, 255, 0), (circle1.x_coor, circle1.y_coor), circle1.radius)
    pygame.display.update()

pygame.quit()
