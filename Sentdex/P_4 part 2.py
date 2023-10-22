# Building neural networks from scratch in Python
# https://youtu.be/TEWy9vZcxW4

import numpy as np
# Wanneer je een "seed" instelt met np.random.seed(0), zorg je ervoor dat elke keer dat het programma wordt uitgevoerd,
# dezelfde reeks willekeurige getallen wordt gegenereerd. Dit is handig voor reproduceerbaarheid, omdat het ervoor
# zorgt dat dezelfde willekeurige getallen worden gegenereerd telkens als het programma wordt uitgevoerd met dezelfde
# "seed".
np.random.seed(0)

# X = inputs
X = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]


# y = targets
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases, randn = random normal distribution
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        # Initialize biases as zero, np.zeros = array of zeros, 1 = 1 dimension, n_neurons = number of neurons
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


# 4 = number of inputs, 5 = number of neurons
layer1 = Layer_Dense(4, 5)
# 5 = number of inputs, 2 = number of neurons
layer2 = Layer_Dense(5, 2)

# Forward pass
layer1.forward(X)
# print(layer1.output)
print(layer1.output)
layer2.forward(layer1.output)
# print(layer2.output)
print(layer2.output)
# Output:
# [[ 0.10758131  1.03983522  0.24462411  0.31821498  0.18851053]
#  [-0.08349796  0.70846411  0.00293357  0.44701525  0.36360538]
#  [-0.50763245  0.55688422  0.07987797 -0.34889573  0.04553042]]
# [[ 0.148296   -0.08397602]
#  [ 0.14100315 -0.01340469]
#  [ 0.20124979 -0.07290616]]


list_output = np.random.randn(4, 3)
print(list_output)
# Output:
# [[ 1.76405235  0.40015721  0.97873798]
#  [ 2.2408932   1.86755799 -0.97727788]
#  [ 0.95008842 -0.15135721 -0.10321885]
#  [ 0.4105985   0.14404357  1.45427351]]

print(0.10 * list_output)
# Output:
# [[ 0.17640523  0.04001572  0.0978738 ]
#  [ 0.22408932  0.1867558  -0.09772779]
#  [ 0.09500884 -0.01513572 -0.01032189]
#  [ 0.04105985  0.01440436  0.14542735]]
