# firstGame me chatGPT v4.py
# Jan George Koomen
# 2023-08-02

# Om de snelheid van de beweging onafhankelijk te maken van de willekeurige functie, kunnen we een constante snelheid gebruiken voor de cirkel
# en de richtingsvector normaliseren (de lengte ervan op 1 houden) zodat de cirkel altijd met dezelfde snelheid beweegt.
# Nu gebruiken we de math.cos en math.sin functies om de x- en y-componenten van de richting van de cirkel te berekenen op basis van de hoek circle_angle.
# De hoek blijft willekeurig worden gewijzigd wanneer de cirkel de randen van het scherm raakt, maar de snelheid blijft constant door circle_speed te gebruiken.
# Dit zorgt ervoor dat de beweging van de cirkel niet afhankelijk is van de willekeurige snelheid, maar toch een willekeurige en continue verandering van richting heeft.
# Soms kan de cirkel vast komen te zitten aan de rand van het scherm vanwege de willekeurige aard van de beweging. Om dit te voorkomen, kunnen we een kleine
# bufferzone toevoegen rond de randen van het scherm waarin we de cirkel niet laten bewegen. Hierdoor zal de cirkel niet precies aan de rand blijven "plakken".
# Om twee cirkels toe te voegen en ervoor te zorgen dat ze afzonderlijk willekeurig bewegen maar van richting veranderen als ze elkaar raken, moeten we de positie
# en richting van beide cirkels bijhouden en controleren of ze elkaar raken.
# In deze aangepaste code hebben we een functie generate_random_direction() toegevoegd om een nieuwe willekeurige richting te genereren voor elke cirkel wanneer dat nodig is.
# De twee cirkels bewegen onafhankelijk en zodra ze elkaar raken, zullen hun richtingen willekeurig worden gewijzigd door een nieuwe willekeurige richting te genereren
# voor elk van de cirkels. Dit zorgt ervoor dat beide cirkels apart willekeurig bewegen, maar dat ze van richting veranderen wanneer ze elkaar raken.
# Het probleem waarbij de cirkels elkaar lijken te "plakken" ontstaat doordat beide cirkels worden teruggeplaatst wanneer ze elkaar raken, maar vervolgens
# kunnen ze direct weer in dezelfde richting bewegen, waardoor ze elkaar opnieuw raken.
# Om dit te voorkomen, kunnen we ervoor zorgen dat de cirkels bij een botsing niet alleen van richting veranderen, maar ook een minimale afstand tot elkaar behouden.
# We kunnen een bufferzone rond elke cirkel instellen en ervoor zorgen dat de afstand tussen de cirkels minimaal gelijk is aan de som van hun stralen plus de bufferzone.
# In deze aangepaste code voegen we een minimale afstand min_distance tussen de cirkels toe en gebruiken we een while-lus om de cirkels terug te plaatsen en te verplaatsen
# totdat ze een veilige afstand van elkaar hebben. Hierdoor blijven de cirkels elkaar niet raken en zien ze er vloeiender uit als ze botsen en van richting veranderen.


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
pygame.display.set_caption("Bewegende Cirkels")

# Cirkel attributen
circle_radius = 20
circle_color = WHITE

# Functie om een nieuwe willekeurige richting te genereren
def generate_random_direction():
    angle = random.uniform(0, 2 * math.pi)
    return [math.cos(angle), math.sin(angle)]

# Cirkels initialiseren
circle1_x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
circle1_y = random.randint(circle_radius, SCREEN_HEIGHT - circle_radius)
circle1_direction = generate_random_direction()

circle2_x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
circle2_y = random.randint(circle_radius, SCREEN_HEIGHT - circle_radius)
circle2_direction = generate_random_direction()

# Minimale afstand tussen de cirkels (2 * straal + buffer)
min_distance = 2 * circle_radius + 1

# Functie om de cirkels te tekenen
def draw_circles(x1, y1, x2, y2):
    pygame.draw.circle(screen, circle_color, (x1, y1), circle_radius)
    pygame.draw.circle(screen, circle_color, (x2, y2), circle_radius)
    
# Snelheid van de cirkel
circle_speed = 5

# Pygame hoofdloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cirkel 1 positie updaten
    circle1_x += circle_speed * circle1_direction[0]
    circle1_y += circle_speed * circle1_direction[1]

    # Cirkel 2 positie updaten
    circle2_x += circle_speed * circle2_direction[0]
    circle2_y += circle_speed * circle2_direction[1]

    # Controleer of de cirkels elkaar raken
    distance = math.sqrt((circle1_x - circle2_x) ** 2 + (circle1_y - circle2_y) ** 2)
    # if distance <= 2 * circle_radius:
    if distance <= min_distance:
        # Richting aanpassen
        circle1_direction = generate_random_direction()
        circle2_direction = generate_random_direction()
        
        # Terugplaatsen en opnieuw proberen om botsing te voorkomen
        while distance <= min_distance:
            circle1_x += circle_speed * circle1_direction[0]
            circle1_y += circle_speed * circle1_direction[1]
            circle2_x += circle_speed * circle2_direction[0]
            circle2_y += circle_speed * circle2_direction[1]
            distance = math.sqrt((circle1_x - circle2_x) ** 2 + (circle1_y - circle2_y) ** 2)

    # Controleer of de cirkels de randen van het scherm raken
    if circle1_x <= circle_radius or circle1_x >= SCREEN_WIDTH - circle_radius:
        circle1_x = max(circle_radius, min(circle1_x, SCREEN_WIDTH - circle_radius))
        # circle_angle = random.uniform(0, 2 * math.pi)
        circle1_direction = generate_random_direction()
    if circle1_y <= circle_radius or circle1_y >= SCREEN_HEIGHT - circle_radius:
        circle1_y = max(circle_radius, min(circle1_y, SCREEN_WIDTH - circle_radius))
        # circle_angle = random.uniform(0, 2 * math.pi)
        circle1_direction = generate_random_direction()
    if circle2_x <= circle_radius or circle2_x >= SCREEN_WIDTH - circle_radius:
        circle2_x = max(circle_radius, min(circle2_x, SCREEN_WIDTH - circle_radius))
        # circle_angle = random.uniform(0, 2 * math.pi)
        circle2_direction = generate_random_direction()
    if circle2_y <= circle_radius or circle2_y >= SCREEN_HEIGHT - circle_radius:
        circle2_y = max(circle_radius, min(circle2_y, SCREEN_WIDTH - circle_radius))
        # circle_angle = random.uniform(0, 2 * math.pi)
        circle2_direction = generate_random_direction()

    # Scherm leegmaken en cirkels tekenen
    screen.fill((0, 0, 0))
    draw_circles(int(circle1_x), int(circle1_y), int(circle2_x), int(circle2_y))

    # Scherm updaten
    pygame.display.flip()

    # FPS beperken
    pygame.time.Clock().tick(60)

# Pygame afsluiten
pygame.quit()
