# // The Nature of Code
# // Daniel Shiffman
# // http://natureofcode.com
#
# // Simple Perceptron Example
# // See: http://en.wikipedia.org/wiki/Perceptron
#
# // Code based on text "Artificial Intelligence", George Luger


import random
import pygame
import sys

# A Perceptron class (definitie zoals eerder verstrekt)

# Coordinate space
xmin, ymin = -1, -1
xmax, ymax = 1, 1


# The function to describe a line
def f(x):
    y = 0.3 * x + 0.4
    return y

# Pygame setup
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perceptron Example")
clock = pygame.time.Clock()

# Initialize Perceptron and training data
ptron = Perceptron(3, 0.001)
training = []

for i in range(2000):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    answer = 1 if y < f(x) else -1
    training.append({
        'input': [x, y, 1],
        'output': answer
    })

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the line
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, height - map(f(xmin), ymin, ymax, 0, height)),
                     (width, height - map(f(xmax), ymin, ymax, 0, height)))

    # Draw the line based on the current weights
    weights = ptron.get_weights()
    x1 = xmin
    y1 = (-weights[2] - weights[0] * x1) / weights[1]
    x2 = xmax
    y2 = (-weights[2] - weights[0] * x2) / weights[1]
    pygame.draw.line(screen, (255, 255, 255), (map(x1, xmin, xmax, 0, width), map(y1, ymin, ymax, height, 0)),
                     (map(x2, xmin, xmax, 0, width), map(y2, ymin, ymax, height, 0)))

    # Train the Perceptron with one "training" point at a time
    ptron.train(training[count]['input'], training[count]['output'])
    count = (count + 1) % len(training)

    # Draw all the points based on what the Perceptron would "guess"
    for i in range(count):
        guess = ptron.feedforward(training[i]['input'])
        color = (255, 255, 255) if guess > 0 else (0, 0, 0)
        x = map(training[i]['input'][0], xmin, xmax, 0, width)
        y = map(training[i]['input'][1], ymin, ymax, height, 0)
        pygame.draw.circle(screen, color, (x, y), 8)

    pygame.display.flip()
    clock.tick(30)
