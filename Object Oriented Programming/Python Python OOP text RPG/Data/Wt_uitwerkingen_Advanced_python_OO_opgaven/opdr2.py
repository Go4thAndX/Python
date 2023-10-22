import random #nodig om random getallen te genereren

class Enemy:
    life = 3

    def attack(self):
        print("ouch!")

        damage = random.randint(0,3) #kies random schade
        self.life -= damage

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

    def heal(self):
        self.life += 2
        print("2 life restored!")



# maak enemy objects:
e1 = Enemy()
e2 = Enemy()

#kies willekeurige eerste aanvaller
beurt = random.randint(1,2)

#en meppen maar:
while e1.life > 0 and e2.life > 0: #is er nog niemand dood?
    if beurt == 1:
        print("Enemy 1 is under attack!")
        e1.attack()
        e1.checkLife()
        beurt = 2 #beurt doorgeven aan andere enemy
    else:
        print("Enemy 2 is under attack!")
        e2.attack()
        e2.checkLife()
        beurt = 1 #beurt doorgeven aan andere enemy

#wie heeft er gewonnen?
if e1.life > 0:
    print("Enemy 1 has won")
    e1.checkLife()
else:
    print("Enemy 2 has won")
    e2.checkLife()


