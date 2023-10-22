# Om ervoor te zorgen dat een print statement niet op een nieuwe regel begint, kunt u het argument end in de print() functie gebruiken. Het end argument bepaalt wat er aan het einde van het print statement wordt geplaatst in plaats van de standaard nieuwe regel (\n).

# Bijvoorbeeld, als u de volgende code uitvoert:
print("Hello", end=" ")
print("world!")
# Output: Hello world!

# Zoals u kunt zien, wordt het tweede print() statement op dezelfde regel afgedrukt als het eerste statement omdat we de end parameter hebben gebruikt om aan te geven dat het einde van het eerste statement een spatie moet zijn in plaats van een nieuwe regel.

# Dus als u een print statement op dezelfde regel wilt laten beginnen als de vorige, kunt u de end parameter gebruiken en deze instellen op een lege string
# Bijvoorbeeld:
print("Dit is een print statement", end="")
print(" dat op dezelfde regel begint!")
# Output: Dit is een print statement dat op dezelfde regel begint!

# Merk op dat het end argument standaard is ingesteld op "\n", dus als u het end argument niet specificeert, zal elk print() statement standaard op een nieuwe regel beginnen.
