import random

player_level = 1
# xp = player_xp(experience points)
player_xp = 0
player_next_level_xp = 500
# hp = player_hp(hit points)
player_hp = 50
# max_hp = player_hp
player_max_hp = 50
player_name = ""
# damage = damage_points
damage_points = 0
# min_damage = min_damage_points
min_damage_points = 0
# max_damage = max_damage_points
max_damage_points = 0
weapon_type = ""
weapon = []
defence_points = 0
item = []


def give_name(name):
    global player_name, weapon
    player_name = name
    weapon = create_weapon(1)
    print(weapon)
    armor = create_armor(1)
    print(armor)
    return weapon


def attack() -> object:
    global damage_points, min_damage_points
    damage_points = player_level + random.randint(min_damage_points, max_damage_points)
    print(f"{player_name} attacks with the weapon {weapon[2]} for {damage_points} damage points")
    return damage_points


def take_hit(damage_points: object, defence_points: int):
    global player_hp
    player_hp -= damage_points - defence_points
    final_damage_points = damage_points - defence_points

    if final_damage_points > 0:
        player_hp -= final_damage_points

        if player_hp <= 0:
            # De player heeft geen hit points meer
            print("Aaaargh ! You died !")
        else:
            print(f"Ouch ! You take {damage_points} damage points")
            print(f"You currently have {player_hp}/{player_max_hp} hit points")

    else:
        print("Your armor protected you. You take 'no' damage points !")


def heal(heal_amount):
    global player_hp
    player_hp += heal_amount

    # Check of de player over het maximum hit points gaat
    if player_hp > player_max_hp:
        player_hp = player_max_hp
        print(f"Yeah ! You healed until the maximum hit points !")
    else:
        print(f"Yeah ! You healed for {heal_amount} hit points !")

    print(f"You currently have {player_hp}/{player_max_hp} hit points")


def xp_gain(xp_amount):
    global player_xp, player_level, player_next_level_xp, player_hp, player_max_hp
    player_xp += xp_amount

    # Check of we naar een volgend level gaan
    if player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = int(player_next_level_xp * 1.25)
        player_max_hp = int(player_max_hp * 1.25)
        player_hp = player_max_hp
        print(f"Yeah ! You've reached the next level, level {player_level} !")
        print(
            f"Your new level {player_level} experience points are: {player_xp}/{player_next_level_xp}"
        )
        print(
            f"Your new level {player_level} hit points are: {player_hp}/{player_max_hp}"
        )
    else:
        print(f"Yeah ! You have gained {xp_amount} experience points !")
        print(
            f"You currently have {player_xp}/{player_next_level_xp} experience points"
        )


def equip_item():
    pass


def create_weapon(item_level_weapon):
    global min_damage_points, max_damage_points, weapon_type
    weapon_list = ["sword", "axe"]
    weapon_type = random.choice(weapon_list)

    if weapon_type == "sword":
        min_damage_points = item_level * 2
        max_damage_points = item_level * 3
    elif weapon_type == "axe":
        min_damage_points = 1
        max_damage_points = item_level * 4

    return item_level_weapon, weapon_type, min_damage_points, max_damage_points


def create_armor(item_level):
    global defence_points, item
    # defence = defence_points
    defence_points = item_level * 2

    return item_level, defence_points


def print_stats():
    print()
    print("-----------------------------")
    print("##### Player statistics #####")
    print("-----------------------------")
    print(f"Name: {player_name}")
    print(f"Level: {player_level}")
    print(f"Hit points: {player_hp}/{player_max_hp}")
    print(f"Experience points: {player_xp}/{player_next_level_xp}")
    print("-----------------------------")
    # print_stats_item(item)
    # print(f"Weapon: {player['weapon']['weapon_type']}")
    # print(f"Armor: {player['armor']['defence_points']}")
    # print("-----------------------------")


def print_stats_weapon(item_level, weapon_type, min_damage_points, max_damage_points):
    # global min_damage_points, max_damage_points, weapon_type, defence_points
    # item_type, item_level = item[0], item[1]
    print(f"{item_type} - level: {item_level}")
    # weapon_type, min_damage_points, max_damage_points = item[2], item[3], item[4]
    print(f"{weapon_type} damage points: {min_damage_points} - {max_damage_points}")

def print_stats_armor():
    defence_points = item[2]
    print(f"Defence points: {defence_points}")
    print("-----------------------------")


player = input("Give the player a name: ")
give_name(name=player)
# Test code voor debuggen
test_continue = True

while test_continue:
    input_answer = input("Testing Y or N: ")

    if input_answer == "Y" or input_answer == "y":
        attack()
        # take_hit_points = int(input("Give take hit points amount: "))
        # defence_points_amount = int(input("Give defence points amount: "))
        # damage_points_amount = int(input("Give damage points amount: "))
        # take_hit(damage_points, defence_points)
        # heal_points = int(input("Give heal points amount: "))
        # heal(heal_points)
        # xp_gain_amount = int(input("Give experience points gain amount: "))
        # xp_gain(xp_gain_amount)
        print_stats()
        # input_item_type = input("Give item type 'weapon' or 'armor': ")
        # input_item_level = int(input("Give item level: "))
        # if input_item_type == "weapon":
        #     input_weapon_type = input("Give weapon type 'sword' or 'axe': ")
        #     input_min_damage_points = int(input("Give min damage points: "))
        #     input_max_damage_points = int(input("Give max damage points: "))
        #     item = [input_item_type, input_item_level, input_weapon_type, input_min_damage_points, input_max_damage_points]
        # elif input_item_type == "armor":
        #     input_defence_points = int(input("Give defence points: "))
        #     item = [input_item_type, input_item_level, input_defence_points]
        # print_stats_item(item)
    else:
        test_continue = False

print("Testing ended")
