# // Daniel Shiffman
# // The Nature of Code
# // http://natureofcode.com
#
# // Simple Perceptron Example
# // See: http://en.wikipedia.org/wiki/Perceptron
#
# // Code based on text "Artificial Intelligence", George Luger

import random
import pygame
import sys

# Perceptron is created with n weights and learning constant

# Perceptron Class
class Perceptron:
    def __init__(self, n, c):
        # Array van gewichten voor input
        self.weights = [random.uniform(-1, 1) for _ in range(n)]
        self.c = c  # leersnelheid/constante

    def train(self, inputs, desired):
        # Schatting maken
        guess = self.feedforward(inputs)
        # Factor berekenen voor het aanpassen van het gewicht op basis van de fout
        # Fout = gewenste output - geschatte output
        # Let op: dit kan alleen 0, -2 of 2 zijn
        # Vermenigvuldigen met leersnelheid
        error = desired - guess
        # Gewichten aanpassen op basis van weightChange * input
        for i in range(len(self.weights)):
            self.weights[i] += self.c * error * inputs[i]

    def feedforward(self, inputs):
        # Som van alle waarden
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        # Resultaat is het teken van de som, -1 of 1
        return self.activate(sum)

    def activate(self, sum):
        if sum > 0:
            return 1
        else:
            return -1

    def get_weights(self):
        return self.weights

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

    # Define the interpolate function
    def interpolate(value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Your existing code
    screen.fill((0, 0, 0))
    line_ymin = interpolate(f(xmin), ymin, ymax, 0, height)
    line_ymax = interpolate(f(xmax), ymin, ymax, 0, height)
    pygame.draw.line(screen, (255, 255, 255), (0, height - line_ymin), (width, height - line_ymax))

    weights = ptron.get_weights()
    x1 = xmin
    y1 = (-weights[2] - weights[0] * x1) / weights[1]
    x2 = xmax
    y2 = (-weights[2] - weights[0] * x2) / weights[1]
    x1_mapped = interpolate(x1, xmin, xmax, 0, width)
    y1_mapped = interpolate(y1, ymin, ymax, height, 0)
    x2_mapped = interpolate(x2, xmin, xmax, 0, width)
    y2_mapped = interpolate(y2, ymin, ymax, height, 0)
    pygame.draw.line(screen, (255, 255, 255), (x1_mapped, y1_mapped), (x2_mapped, y2_mapped))

    ptron.train(training[count]['input'], training[count]['output'])
    count = (count + 1) % len(training)

    for i in range(count):
        guess = ptron.feedforward(training[i]['input'])
        color = (255, 255, 255) if guess > 0 else (0, 0, 0)
        x = interpolate(training[i]['input'][0], xmin, xmax, 0, width)
        y = interpolate(training[i]['input'][1], ymin, ymax, height, 0)
        pygame.draw.circle(screen, color, (x, y), 8)

    pygame.display.flip()
    clock.tick(30)
