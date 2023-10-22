import time
import random


def animate_text(par_text):
    for i in range(0, len(par_text)):
        print(par_text[i], end="")
        time_seconds = random.uniform(0.05, 0.1)
        time.sleep(time_seconds)


# Open het tekstbestand in leesmodus
text_file = open("Typewriter.txt", "r")
# Lees de inhoud van het bestand
text_content = text_file.read()
# Sluit het bestand
text_file.close()
animate_text(par_text=text_content)
