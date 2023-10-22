# Zie voor uitleg Readme.txt

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Laden van de Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # We gebruiken slechts de eerste twee kenmerken voor visualisatie
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

# Visualisatie van beslissingsgrens
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
Z = perceptron.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=20)
plt.title("Beslissingsgrens van het Perceptron-model")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
