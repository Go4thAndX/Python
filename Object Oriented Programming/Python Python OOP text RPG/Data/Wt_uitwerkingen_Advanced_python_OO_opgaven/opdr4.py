import random #nodig om random getallen te genereren

class Enemy:

    #de init heeft nu standaardwaarden voor start_life en max_damage
    def __init__(self, name, start_life=20, max_damage=3):
        #sla de twee opgegeven startwaarden op als instance variabelen:
        self.name = name
        self.life = start_life
        self.max_damage = max_damage    

    def attack(self):
        print("ouch!")
        damage = random.randint(0,self.max_damage) #kies random schade tussen 0 en maximum
        self.life -= damage

        #druk duidelijke info af:
        print(self.name +  " took " + str(damage) + " damage and has " + str(self.life) + " life left.")

    def checkLife(self):
        #gebruik nu ook de naam in de checklife voor extra duidelijkheid
        if self.life <= 0:
            print(self.name, "is dead")
        else:
            print(self.name, "has", self.life, "life left")

    def heal(self):
        self.life += 2
        print("2 life restored!")



# maak enemy objects:
e1 = Enemy("Henk", 10, 3) #Enemy met eigen waarden
e2 = Enemy("Piet") #Enemy met standaardwaaren

#kies willekeurige eerste aanvaller
beurt = random.randint(1,2)

#en meppen maar:
while e1.life > 0 and e2.life > 0: #is er nog niemand dood?
    if beurt == 1:
        print("Enemy 1 is under attack!")
        e1.attack()
        beurt = 2 #beurt doorgeven aan andere enemy
    else:
        print("Enemy 2 is under attack!")
        e2.attack()
        beurt = 1 #beurt doorgeven aan andere enemy

#wie heeft er gewonnen?
print("------------")
if e1.life > 0:
    print("Enemy 1 has won:", e1.name)
    e1.checkLife()
else:
    print("Enemy 2 has won:", e2.name)
    e2.checkLife()



