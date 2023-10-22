# Wanneer je dit script uitvoert, zal Matplotlib een grafiek weergeven met een lijn die de punten (1, 2), (2, 4), (3, 6), (4, 8) en (5, 10) met elkaar verbindt.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Een eenvoudige lijngrafiek')
plt.show()
