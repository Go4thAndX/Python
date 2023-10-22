import random


class Player:
    level = 1
    # Was xp
    experience_points = 0
    # Was next_level_xp
    next_level_experience_points = 500
    # Was hp
    life_points = 50
    # Was max_hp
    max_life_points = 50

    def __init__(self, name):
        self.name = name
        self.weapon = Weapon(1)
        self.armor = Armor(1)

    def attack(self):
        # Was damage
        damage_points = self.level + random.randint(
            self.weapon.min_damage_points, self.weapon.max_damage_points
        )
        print(
            f"{self.name} attacks with {self.weapon.weapon_type} for {damage_points} damage points"
        )
        return damage_points

    # Was take_hit
    def take_life_points(self, damage_points):
        # Was final_damage
        final_damage_points = damage_points - self.armor.defence_points

        if final_damage_points > 0:
            self.life_points -= final_damage_points

            print(f"Ouch ! You took {final_damage_points} damage points")

            if self.life_points <= 0:
                print("You haven't got any life points left ! Aaaaargh !  You died !")
            else:
                print(
                    f"You have {self.life_points}/{self.max_life_points} life points left"
                )
        else:
            print("Your armour protected you well ! You lose no life points !")

    def heal(self, heal_amount):
        self.life_points += heal_amount
        # Check if you reached the maximium life points
        if self.life_points > self.max_life_points:
            self.life_points = self.max_life_points
        print(f"You healed for {heal_amount} life points")
        print(
            f"You currently have {self.life_points}/{self.max_life_points} life points"
        )

    def experience_points_gain(self, experience_points_amount):
        self.experience_points += experience_points_amount
        print(
            f"You have gained {experience_points_amount} experience points, your experience points are {self.experience_points}/{self.next_level_experience_points} !"
        )
        # Check if you have reached a next level
        if self.experience_points >= self.next_level_experience_points:
            self.level += 1
            self.experience_points -= self.next_level_experience_points
            self.next_level_experience_points = int(
                self.next_level_experience_points * 1.5
            )
            self.max_life_points = int(self.max_life_points * 1.5)
            self.life_points = self.max_life_points
            print(f"Yeah ! Next level ! You've reached level {self.level} !")
            self.print_stats()

    def equip_item(self, item):
        if item.item_type == "weapon":
            self.weapon = item
        elif item.item_type == "armor":
            self.armor = item

        # Laat zien hoe de player er nu voor staat
        self.print_stats()

    def print_stats(self):
        print()
        print("-----------------------------")
        print("##### Player statistics #####")
        print("-----------------------------")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Life points: {self.life_points}/{self.max_life_points}")
        print(
            f"Experience points: {self.experience_points}/{self.next_level_experience_points}"
        )
        print("-----------------------------")
        self.weapon.print_stats()
        self.armor.print_stats()
        print("-----------------------------")


# De geselecteerde code definieert een klasse genaamd "Item". Deze klasse heeft een klassevariabele genaamd "item_type", die aanvankelijk is ingesteld op None
# De klasse heeft ook een constructor methode genaamd "init". Deze methode neemt een parameter genaamd "item_level" aan. In de constructor methode wordt de "item_level" parameter toegewezen aan een instantievariabele die ook "item_level" heet. Het doel van deze code is om een blauwdruk te definiëren voor objecten van de klasse "Item", waarbij elke instantie van de klasse een "item_level" attribuut zal hebben. Het "item_type" attribuut kan worden geraadpleegd en gewijzigd door alle instanties van de klasse, terwijl het "item_level" attribuut specifiek zal zijn voor elke individuele instantie
class Item:
    item_type = None

    def __init__(self, item_level):
        self.item_level = item_level

    def print_stats(self):
        print(f"{self.item_type} - level {self.item_level}")


# Subclass van Item
class Weapon(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type_type = "weapon"
        weapon_list = ["Sword", "Axe"]
        self.weapon_type = random.choice(weapon_list)

        if self.weapon_type == "Sword":
            # Was min_damage
            self.min_damage_points = self.item_level * 2
            # Was max_damage
            self.max_damage_points = self.item_level * 3

        elif self.weapon_type == "Axe":
            self.min_damage_points = 1
            self.max_damage_points = self.item_level * 4

    def print_stats(self):
        Item.print_stats(self)
        print(
            f"{self.weapon_type} damage {self.min_damage_points} - {self.max_damage_points}"
        )


# Subclass van Item
class Armor(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type = "armor"
        # Was defence
        self.defence_points = self.item_level * 2

    def print_stats(self):
        Item.print_stats(self)
        print(f"Defence points: {self.defence_points}")


class Monster:
    life_points = 1
    max_life_points = 1
    min_damage_points = 1
    max_damage_points = 1
    monster_type = None

    experience_points_value = 1

    def __init__(self, level):
        self.level = level

    def attack(self):
        damage_points = random.randint(self.min_damage_points, self.max_damage_points)
        print(f"{self.monster_type} attacks for {damage_points} damage points")
        return damage_points

    def take_life_points(self, damage_points):
        self.life_points -= damage_points

        if self.life_points > 0:
            # Monster leeft nog
            print(f"{self.monster_type} has {self.life_points} life points left")
        else:
            # Monster is dood
            print(f"{self.monster_type} beaten and died")

    def print_stats(self):
        print(f"{self.monster_type} - level {self.level}")

        if self.life_points > 0:
            print(f"Life points: {self.life_points} / {self.max_life_points}")
        else:
            print("This particular monster exterminated")


# Subclass van Monster
class Skeleton(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)

        self.monster_type = "Skeleton"
        self.life_points = self.max_life_points = self.level * 15
        self.min_damage_points = self.level + 1
        self.max_damage_points = self.level * 3
        self.experience_points_value = 100 + self.level * 20


# Subclass van Monster
class Troll(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)

        self.monster_type = "Troll"
        self.life_points = self.max_life_points = self.level * 20
        self.min_damage_points = 1
        self.max_damage_points = self.level * 4
        self.experience_points_value = 100 + self.level * 20
        self.critical_chance = max(30, level * 10)

    def attack(self):
        damage_points = random.randint(self.min_damage_points, self.max_damage_points)

        # Bij een critical hit
        if random.randint(1, 100) <= self.critical_chance:
            print(f"{self.monster_type} makes a critical hit !")
            damage_points *= 2

        print(f"{self.monster_type} attacks for {damage_points} damage points")
        return damage_points


class Battle:
    # TODO Hier zit mogelijk een fout in de code !!!
    # def __init__(self):
    #     # Een link naar player
    #     self.player = Player
    def __init__(self, player):
        # Een link naar player
        self.player = player
        self.difficulty = random.randint(1, 3)
        self.monster_list = []
        self.experience_points_value = 0
        monster_types = ["Skeleton", "Troll"]

        for i in range(self.difficulty):
            monster_choice = random.choice(monster_types)

            if monster_choice == "Skeleton":
                self.monster_list.append(Skeleton(self.player.level))
            elif monster_choice == "Troll":
                self.monster_list.append(Troll(self.player.level))

            self.experience_points_value += self.monster_list[i].experience_points_value

    def battle_stats(self):
        print("You are battling")

        for i in range(self.difficulty):
            print(("Enemy", i + 1))
            self.monster_list[i].print_stats()
            print()

        print("-----------------------------")
        print()

    # Genereert mogelijk nieuwe items na een battle
    def generate_loot(self):
        loot = False

        if self.difficulty == 1:
            if random.randint(1, 100) <= 25:
                loot = True
        elif self.difficulty == 2:
            if random.randint(1, 100) <= 40:
                loot = True
        elif self.difficulty == 3:
            if random.randint(1, 100) <= 60:
                loot = True

        # Genereer een item voor de player
        if loot == True:
            # Er wordt een keuze gemaakt tussen een wapen en eens schild
            loot_list = ["Weapon", "Armor"]
            loot_type = random.choice(loot_list)

            if loot_type == "Weapon":
                item = Weapon(random.randint(self.player.level, self.player.level + 1))
                print("You can loot a weapon from the monster !")
            elif loot_type == "Armor":
                item = Armor(random.randint(self.player.level, self.player.level + 1))
                print("You can loot an armor from the monster !")

            # Laat het gegenereerde item zien
            item.print_stats()
            print()
            print("Your current stats are:")
            self.player.print_stats()
            print()

            choice = input("Do you want to equip the new item ? (Y/N): ")
            choice = choice.lower()

            if choice == "n":
                print("You are not equip the new item")
            else:
                self.player.equip_item(item)
                print("You equip the new item")
        #  Geen item voor de player beschikbaar na het verslaan van een monster
        else:
            print("There is no item made available by slaying a monster !")

    def monster_attack(self):
        # De monsters doen een aanval
        for monster in self.monster_list:
            if monster.life_points > 0:
                monster_damage = monster.attack()
                self.player.take_life_points(monster_damage)

    def player_attack(self):
        # De player valt 1 van de monsters aan

        # Zijn er 1 of meerdere monsters
        if len(self.monster_list) > 1:
            max_target = len(self.monster_list)
            # target_answer = True
            target = -1

            while target < 1 or target > max_target:
                target = int(
                    input(
                        f"Which monster would you like to atack, monster (1 - {max_target}): "
                    )
                )
                print(target)
                # if target == 1 or target == 2 or target == 3:
                #     target_answer = False
            target -= 1
        else:
            target = 0
        player_damage = self.player_attack()

        if self.monster_list[target].life_points > 0:
            self.monster_list[target].take_hit(player_damage)
        else:
            print("You attacked a dead monster, it will cost ye...")

    def player_heal(self):
        # De speler probeert zichzelf beter te maken
        if random.randint(1, 100) <= 40:
            heal_amount = random.randint(
                self.player.max_life_points // 4, self.player.max_life_points // 3
            )
            self.player.heal(heal_amount)
        else:
            print("You tried to heal, but the healing wasn't posibble...")

    def player_cloaking(self):
        if random.randint(1, 100) <= 25:
            print("You tried cloaking because the monsters were overwhelming strong")
        else:
            print(
                "You couldn't use cloaking, you had no time to use the cloaking device...!"
            )
            return False

    def player_quit(self):
        print("You know you can't win and give up so the life will drain out of you")
        self.player.life_points = 0

    def fight_battle(self):
        print()
        print("You are under attack")

        while True:
            print()
            print("---- BATTLE ROUND ----")
            self.battle_stats()
            player_action = ""

            while player_action not in ["S", "F", "H", "C", "Q"]:
                player_action = input(
                    "What action will you take ? (S)tats, (F)ight, (H)eal, (C)loak, (Q)uit: "
                ).upper()

            if player_action == "S":
                self.player.print_stats()
                input("Press [Enter] to continue the battle: ")

            elif player_action == "F":
                self.player_attack()
                monsters_alive = 0

                for monster in self.monster_list:
                    if monster.life_points > 0:
                        monsters_alive += 1

                if monsters_alive > 0:
                    self.monster_attack()

                else:
                    print("--------------------------")
                    print("--- YOU WON THE BATTLE ---")
                    print("--------------------------")
                    self.player.experience_points_gain(self.experience_points_value)
                    self.generate_loot()
                    break

            elif player_action == "H":
                self.player_heal()
                print()
                self.monster_attack()

            elif player_action == "C":
                if self.player_cloaking() == True:
                    break
                else:
                    self.monster_attack()

            elif player_action == "Q":
                self.player_quit()
                break

            if self.player.experience_points <= 0:
                print("--------------------------")
                print("--- YOU LOST YOUR LIFE ---")
                print("--------------------------")
                break


player_name = input("What is your player name ?: ")
player = Player(player_name)
print()
print(f"Good battle player {player_name}. Try to defeat the monsters !")
input("Press [Enter] to start the battle !")
battle_count = 0

while player.life_points > 0:
    print()
    print("-----")
    print()
    battle_count += 1
    print(f"Battle {battle_count}")
    battle = Battle(player)
    battle.fight_battle()

print()
print(f"You have battled {battle_count} battles")
print("Your final battle stats are:")
print()
print("Thnx for playing")
