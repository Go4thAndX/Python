import random


class Battle:
    life_enemy = 10
    life_hero = 10

    def attack(self):
        print("Attack has started, wait for the outcome of this attack !")
        points_enemy = random.randint(1, 6)
        points_hero = random.randint(1, 6)
        outcome = points_enemy - points_hero

        if outcome < 0:
            print(
                f"Yeaa ! Hero wins this attack with {outcome * -1} life gained and enemy lost {outcome * -1} life !"
            )
            self.life_enemy += outcome
            self.life_hero -= outcome
        elif outcome > 0:
            print(
                f"Ouch ? Enemy wins this attack with {outcome} life gained and hero lost {outcome} life !"
            )
            self.life_enemy += outcome
            self.life_hero -= outcome
        else:
            print(f"It's a draw, both contenders loose {points_hero} lives !")
            self.life_enemy -= points_enemy
            self.life_hero -= points_hero

    def check_life(self):
        stop_game = True
        if self.life_enemy <= 0:
            print("Enemy is dead, hero wins the battle !")
            stop_game = False
        elif self.life_hero <= 0:
            print("Hero is dead, enemy wins the battle !")
            stop_game = False
        else:
            print(f"Enemy has {self.life_enemy} life left", end=" ")
            print(f"Hero has {self.life_hero} life left")

        if self.life_enemy >= 20:
            print("Enemy has reached super power !")
            self.life_hero -= 10

            if self.life_hero <= 0:
                print("Hero is dead, enemy wins the battle !")
                stop_game = False
        if self.life_hero >= 20:
            print("Hero has reached super power !")
            self.life_enemy -= 10

            if self.life_enemy <= 0:
                print("Enemy is dead, hero wins the battle !")
                stop_game = False

        return stop_game

    def heal(self):
        # TODO Herstel funtie afhankelijk maken van hoeveel levens er tijdens de attack verloren zijn.
        heal_enemy = random.choice([True, False])

        if heal_enemy == True:
            points_enemy = random.randint(1, 3)
            self.life_enemy += points_enemy
            print(f"Enemy has {points_enemy} life restored !", end=" ")
        else:
            print("Enemy has no life restored !", end=" ")
        heal_hero = random.choice([True, False])

        if heal_hero == True:
            points_hero = random.randint(1, 3)
            self.life_hero += points_hero
            print(f"Hero has {points_hero} life restored !")
        else:
            print("Hero has no life restored !")

    def start_battle(self):
        print("Battle started")
        attack_number = 1
        stop_game = True

        while stop_game:
            print()
            print(f"Attack Number: {attack_number}")
            self.attack()
            self.heal()
            stop_game = self.check_life()
            attack_number += 1

        print("Battle has ended")


battle = Battle()
battle.start_battle()
