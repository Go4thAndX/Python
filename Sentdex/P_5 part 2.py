# Building neural networks from scratch in Python
# https://youtu.be/gmjzbpSVY1A
# TODO Hier nog kijken naar de grafiek met de 3 spiralen en de 3 kleuren die daarbij horen (zie video) en Matplotlib

import numpy as np
import nnfs
import nnfs.datasets

nnfs.init()

X, y = spiral_data(100, 3)


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()

layer1.forward(X)

# print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)
