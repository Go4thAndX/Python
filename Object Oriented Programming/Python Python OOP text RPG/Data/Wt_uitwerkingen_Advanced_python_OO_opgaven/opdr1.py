class Enemy:
    life = 3

    def attack(self):
        print("Ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(f"{self.life} life left")

    def heal(self):
        self.life += 2
        print("2 life restored!")


# Maak een Enemy() object
e = Enemy()

# Begin met aanvallen:
e.attack()
e.checkLife()
e.attack()
e.checkLife()

# Tussendoor even herstellen:
e.heal()
e.checkLife()

# Verder gaan met aanvallen:
e.attack()
e.checkLife()
e.attack()
e.checkLife()
e.attack()
e.checkLife()
