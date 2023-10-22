# firstGame me chatGPT v2.py
# Jan George Koomen
# 2023-08-02

# Om de snelheid van de beweging onafhankelijk te maken van de willekeurige functie, kunnen we een constante snelheid gebruiken voor de cirkel
# en de richtingsvector normaliseren (de lengte ervan op 1 houden) zodat de cirkel altijd met dezelfde snelheid beweegt.
# Nu gebruiken we de math.cos en math.sin functies om de x- en y-componenten van de richting van de cirkel te berekenen op basis van de hoek circle_angle.
# De hoek blijft willekeurig worden gewijzigd wanneer de cirkel de randen van het scherm raakt, maar de snelheid blijft constant door circle_speed te gebruiken.
# Dit zorgt ervoor dat de beweging van de cirkel niet afhankelijk is van de willekeurige snelheid, maar toch een willekeurige en continue verandering van richting heeft.

import pygame
import random
import math

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

# Snelheid van de cirkel
circle_speed = 5

# Richting van de cirkel (willekeurige hoek)
circle_angle = random.uniform(0, 2 * math.pi)
circle_direction = [math.cos(circle_angle), math.sin(circle_angle)]

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
        circle_angle = random.uniform(0, 2 * math.pi)
        circle_direction = [math.cos(circle_angle), math.sin(circle_angle)]
    if circle_y <= circle_radius or circle_y >= SCREEN_HEIGHT - circle_radius:
        circle_angle = random.uniform(0, 2 * math.pi)
        circle_direction = [math.cos(circle_angle), math.sin(circle_angle)]

    # Scherm leegmaken en cirkel tekenen
    screen.fill((0, 0, 0))
    draw_circle(int(circle_x), int(circle_y))

    # Scherm updaten
    pygame.display.flip()

    # FPS beperken
    pygame.time.Clock().tick(60)

# Pygame afsluiten
pygame.quit()
