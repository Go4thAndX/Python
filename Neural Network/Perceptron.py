# // Daniel Shiffman
# // The Nature of Code
# // http://natureofcode.com
#
# // Simple Perceptron Example
# // See: http://en.wikipedia.org/wiki/Perceptron
#
# // Perceptron Class
#
# // Perceptron is created with n weights and learning constant

import random


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
