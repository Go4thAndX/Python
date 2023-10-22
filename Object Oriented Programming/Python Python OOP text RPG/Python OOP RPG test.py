import random


class Player:
    level = 1
    # Was xp
    experians_points = 0
    # Was next_level_xp
    next_level_experians_points = 500
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

    def experians_points_gain(self, experians_points_amount):
        self.experians_points += experians_points_amount
        print(
            f"You have gained {experians_points_amount} experians points, your experians points are {self.experians_points}/{self.next_level_experians_points} !"
        )
        # Check if you have reached a next level
        if self.experians_points >= self.next_level_experians_points:
            self.level += 1
            self.experians_points -= self.next_level_experians_points
            self.next_level_experians_points = int(
                self.next_level_experians_points * 1.5
            )
            self.max_life_points = int(self.max_life_points * 1.5)
            self.life_points = self.max_life_points
            print(f"Yeah ! Next level ! You've reached level {self.level} !")
            self.print_stats()

    def equip_item(self):
        pass

    def print_stats(self):
        print()
        print("-----------------------------")
        print("##### Player statistics #####")
        print("-----------------------------")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Life points: {self.life_points}/{self.max_life_points}")
        print(
            f"Experience points: {self.experians_points}/{self.next_level_experians_points}"
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
    pass


# Subclass van Monster
class Skeleton(Monster):
    pass


# Subclass van Monster
class Troll(Monster):
    pass


class Battle:
    pass
