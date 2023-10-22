import random


def create_item(item_type, item_level):
    return item_type, item_level


def create_weapon(item_level):
    weapon_list = ["Sword", "Axe"]
    weapon_type = random.choice(weapon_list)

    if weapon_type == "Sword":
        min_damage = item_level * 2
        max_damage = item_level * 3
    elif weapon_type == "Axe":
        min_damage = 1
        max_damage = item_level * 4

    return "weapon", item_level, weapon_type, min_damage, max_damage


def create_armor(item_level):
    defence = item_level * 2
    return "armor", item_level, defence


def print_stats(item):
    item_type, item_level = item[0], item[1]
    print(f"{item_type} - level: {item_level}")

    if item_type == "weapon":
        weapon_type, min_damage, max_damage = item[2], item[3], item[4]
        print(f"{weapon_type} damage: {min_damage} - {max_damage}")
    elif item_type == "armor":
        defence = item[2]
        print(f"Defence: {defence}")


# Voorbeeld van het maken van een wapen en afdrukken van de statistieken
weapon = create_weapon(5)
print_stats(weapon)

# Voorbeeld van het maken van een harnas en afdrukken van de statistieken
armor = create_armor(3)
print_stats(armor)
