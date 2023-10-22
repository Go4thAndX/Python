import random

player_level = 1
# xp = player_xp(experience points)
player_xp = 0
player_next_level_xp = 500
# hp = player_hp(hit points)
# global player_hp
player_hp = 50
# max_hp = player_hp
player_max_hp = 50
player_name = ""


def give_name(name):
    global player_name
    player_name = name


def attack() -> object:
    # damage = damage_points
    damage_points = random.randint(2, 5)
    print(f"{player_name} attacks for {damage_points} damage points")
    return damage_points


def take_hit(damage_points):
    global player_hp
    player_hp -= damage_points

    if player_hp <= 0:
        # De player heeft geen hit points meer
        print("Aaaargh ! You died !")
    else:
        print(f"Ouch ! You take {damage_points} damage points")
        print(f"You currently have {player_hp}/{player_max_hp} hit points")


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
        print(f"Your new level {player_level} experience points are: {player_xp}/{player_next_level_xp}")
        print(f"Your new level {player_level} hit points are: {player_hp}/{player_max_hp}")
    else:
        print(f"Yeah ! You have gained {xp_amount} experience points !")
        print(f"You currently have {player_xp}/{player_next_level_xp} experience points")


def equip_item():
    pass


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
    # print(f"Weapon: {player['weapon']['weapon_type']}")
    # print(f"Armor: {player['armor']['defence_points']}")
    # print("-----------------------------")


def item():


    player_item_level = item_level

    def item_weapon(item):
        pass

    def item_armor(item):
        pass

player = input("Give the player a name: ")
give_name(name=player)
# Test code voor debuggen
test_continue = True

while test_continue:
    input_answer = input("Testing Y or N: ")

    if input_answer == "Y" or input_answer == "y":
        attack()
        take_hit_points = int(input("Give take hit points amount: "))
        take_hit(take_hit_points)
        heal_points = int(input("Give heal points amount: "))
        heal(heal_points)
        xp_gain_amount = int(input("Give experience points gain amount: "))
        xp_gain(xp_gain_amount)
        print_stats()
    else:
        test_continue = False

print("Testing ended")
