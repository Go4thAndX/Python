# Om de output van print statements te laten verdwijnen na een bepaalde code stap in PyCharm, kun je de `os` module gebruiken om het terminalscherm te wissen voordat je nieuwe output afdrukt. Hier is een voorbeeld van hoe je dit kunt doen:


import os

# Code hierboven

# Wis het terminalscherm
os.system("cls" if os.name == "nt" else "clear")

# Code hieronder

# In dit voorbeeld wordt de `os.system`-functie gebruikt om het terminalscherm te wissen. De exacte opdracht die wordt gebruikt om het scherm te wissen, is afhankelijk van het besturingssysteem. In dit voorbeeld wordt 'cls' gebruikt voor Windows (NT) en 'clear' voor Unix-gebaseerde systemen.

# Je kunt deze code op elk gewenst punt in je script plaatsen om het scherm te wissen en de oude output te verwijderen voordat je nieuwe output afdrukt. Hierdoor lijkt het alsof de oude output is verdwenen en alleen de nieuwe output wordt weergegeven.
