# firstGame me chatGPT v1.py
# Jan George Koomen
# 2023-08-02

# Creëer Pygame code die het volgende bewerkstelligt:  In een gecreëerd venster met bepaalde afmetingen, beweegt een vorm (cirkel) zich
# vanuit bepaald punt op het venster, met een bepaalde snelheid in een willekeurige richting en bij het bereiken van de rand (einde) van
# het venster veranderd de richting van de beweging willekeurig maar wel zodanig dat hij van de rand van het (eind) van het venster af beweegt
# en dit wordt eindeloos herhaald totdat het venster gesloten wordt.

import pygame
import random

# Pygame initialisatie
pygame.init()

# Scherm afmetingen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Kleuren
WHITE = (255, 255, 255)

# Scherm creëren
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bewegende Cirkel")

# Cirkel attributen
circle_radius = 20
circle_color = WHITE

# Startpositie van de cirkel (willekeurig punt op het scherm)
circle_x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
circle_y = random.randint(circle_radius, SCREEN_HEIGHT - circle_radius)

# Snelheid en richting van de cirkel
circle_speed = 5
circle_direction = [random.uniform(-1, 1), random.uniform(-1, 1)]
# circle_direction = [(random.choice([-100, 100])) / 100, (random.choice([-1, 1])) / 100]
print(circle_direction)

# Functie om de cirkel te tekenen
def draw_circle(x, y):
    pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

# Pygame hoofdloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cirkelpositie updaten
    circle_x += circle_speed * circle_direction[0]
    circle_y += circle_speed * circle_direction[1]

    # Controleer of de cirkel de randen van het scherm raakt
    if circle_x <= circle_radius or circle_x >= SCREEN_WIDTH - circle_radius:
        circle_direction[0] = random.uniform(-1, 1)
    if circle_y <= circle_radius or circle_y >= SCREEN_HEIGHT - circle_radius:
        circle_direction[1] = random.uniform(-1, 1)

    # Scherm leegmaken en cirkel tekenen
    screen.fill((0, 0, 0))
    draw_circle(int(circle_x), int(circle_y))

    # Scherm updaten
    pygame.display.flip()

    # FPS beperken
    pygame.time.Clock().tick(60)

# Pygame afsluiten
pygame.quit()
