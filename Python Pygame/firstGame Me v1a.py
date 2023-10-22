import pygame

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")


class Shapes:
    def __init__(self, x_coor, y_coor, mov) -> None:
        # Starpunt x coordinaat vorm
        self.x_coor = x_coor
        # Starpunt y coordinaat vorm
        self.y_coor = y_coor
        # Verplaatsing in pixels
        self.mov = mov


# Sub klasse van klasse Shapes
class Rectangle(Shapes):
    def __init__(self, x_coor, y_coor, mov, width, height, ) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.width = width
        self.height = height


# Sub klasse van klasse Shapes
class Circle(Shapes):
    def __init__(self, x_coor, y_coor, mov, radius) -> None:
        super().__init__(x_coor, y_coor, mov)
        self.radius = radius


# Instantie van Rectangle
rectangle1 = Rectangle(250, 200, 1, 40, 60)

# Instantie van Circle
circle1 = Circle(200, 250, 10, 30)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Coordinaten beginnen in de linkerbovenhoek met (0, 0)
    keys = pygame.key.get_pressed()
    
    if rectangle1.x_coor + rectangle1.width > win_width or rectangle1.x_coor < 0:
        rectangle1.mov *= -1  # Verander de bewegingsrichting

    rectangle1.x_coor += rectangle1.mov
    rectangle1.y_coor -= rectangle1.mov
    
    if circle1.x_coor + circle1.radius > win_width or circle1.x_coor - circle1.radius < 0:
        circle1.mov *= -1  # Verander de bewegingsrichting
        
    circle1.x_coor += circle1.mov
    circle1.y_coor += (circle1.mov * -0.5)
    
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
