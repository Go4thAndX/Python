import numpy as np
import matplotlib.pyplot as plt


# Functie om de Mandelbrot-set te berekenen
def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    fractal = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        Z = Z ** 2 + C
        mask = np.abs(Z) < 10
        fractal += mask

    return fractal


# Instellingen voor de fractal
width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iter = 100

# Bereken en visualiseer de fractal
fractal = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
plt.imshow(fractal, extent=(x_min, x_max, y_min, y_max), cmap='inferno', origin='lower')
plt.colorbar()
plt.title("Mandelbrot-set Fractal")
plt.xlabel("Reële as")
plt.ylabel("Imaginaire as")
plt.show()
