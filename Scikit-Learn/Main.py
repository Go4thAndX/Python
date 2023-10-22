# Zie voor uitleg Readme.txt

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Laden van de Iris dataset
iris = load_iris()
X = iris.data
y = (iris.target != 0).astype(int)  # Binary class problem: Setosa vs others

# Data opsplitsen in training en test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiseren van het Perceptron model
perceptron = Perceptron(random_state=42)

# Model trainen
perceptron.fit(X_train, y_train)

# Voorspellingen maken op de test set
predictions = perceptron.predict(X_test)

# Nauwkeurigheid evalueren
accuracy = accuracy_score(y_test, predictions)
print(f"Nauwkeurigheid: {accuracy:.2f}")
