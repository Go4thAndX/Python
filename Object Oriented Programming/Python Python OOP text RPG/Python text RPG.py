import random


def create_player(name):
    player = {}
    player["name"] = name
    player["level"] = 1
    player["experience_points"] = 0
    player["next_level_experience_points"] = 500
    player["life_points"] = 50
    player["max_life_points"] = 50
    player["weapon"] = create_weapon(1)
    player["armor"] = create_armor(1)
    return player


def create_weapon(level):
    weapon = {}
    weapon["min_damage_points"] = 10 * level
    weapon["max_damage_points"] = 20 * level
    weapon["weapon_type"] = "Sword"
    return weapon


def create_armor(level):
    armor = {}
    armor["defence_points"] = 5 * level
    return armor


def attack(player, enemy):
    damage_points = player["level"] + random.randint(
        player["weapon"]["min_damage_points"], player["weapon"]["max_damage_points"]
    )
    enemy["life_points"] -= damage_points


def take_life_points(player, damage_points):
    final_damage_points = damage_points - player["armor"]["defence_points"]

    if final_damage_points > 0:
        player["life_points"] -= final_damage_points

        if player["life_points"] <= 0:
            print("You died !")
        else:
            print(
                f"You have {player['life_points']}/{player['max_life_points']} life points left"
            )
    else:
        print("Your armour protected you well !")


def heal(player, heal_amount):
    player["life_points"] += heal_amount

    if player["life_points"] > player["max_life_points"]:
        player["life_points"] = player["max_life_points"]

    print(f"You healed for {heal_amount} life points")


def experience_points_gain(player, experience_points_amount):
    player["experience_points"] += experience_points_amount

    if player["experience_points"] >= player["next_level_experience_points"]:
        player["level"] += 1
        player["experience_points"] -= player["next_level_experience_points"]
        player["next_level_experience_points"] = int(
            player["next_level_experience_points"] * 1.5
        )
        player["max_life_points"] = int(player["max_life_points"] * 1.5)
        player["life_points"] = player["max_life_points"]
        print(f"You've reached level {player['level']} !")


def equip_item(player, item):
    if item["item_type"] == "weapon":
        player["weapon"] = item
    elif item["item_type"] == "armor":
        player["armor"] = item


def print_stats(player):
    print()
    print("-----------------------------")
    print("##### Player statistics #####")
    print("-----------------------------")
    print(f"Name: {player['name']}")
    print(f"Level: {player['level']}")
    print(f"Life points: {player['life_points']}/{player['max_life_points']}")
    print(
        f"Experience points: {player['experience_points']}/{player['next_level_experience_points']}"
    )
    print("-----------------------------")
    print(f"Weapon: {player['weapon']['weapon_type']}")
    print(f"Armor: {player['armor']['defence_points']}")
    print("-----------------------------")

def create_item(item_type, item_level):
    item = {}
    item["item_type"] = item_type
    item["item_level"] = item_level

    if item_type == "weapon":
        weapon_list = ["Sword", "Axe"]
        item["weapon_type"] = random.choice(weapon_list)
        item["min_damage_points"] = item_level * 2
        item["max_damage_points"] = item_level * 3

    elif item_type == "armor":
        item["defence_points"] = item_level * 2

    return item


def print_stats(item):
    print(f"{item['item_type']} - level {item['item_level']}")

    if item["item_type"] == "weapon":
        print(f"{item['weapon_type']} damage {item['min_damage_points']} - {item['max_damage_points']}")
    elif item["item_type"] == "armor":
        print(f"Defence points: {item['defence_points']}")

def create_monster(monster_type, level):
    monster = {}
    monster["monster_type"] = monster_type
    monster["level"] = level
    monster["life_points"] = level * 15
    monster["max_life_points"] = level * 15
    monster["min_damage_points"] = level + 1
    monster["max_damage_points"] = level * 3
    monster["experience_points_value"] = 100 + level * 20

    if monster_type == "Troll":
        monster["critical_chance"] = max(30, level * 10)

    return monster


def attack(monster):
    damage_points = random.randint(monster["min_damage_points"], monster["max_damage_points"])
    print(f"{monster['monster_type']} attacks for {damage_points} damage points")
    return damage_points


def take_life_points(monster, damage_points):
    monster["life_points"] -= damage_points

    if monster["life_points"] > 0:
        # Monster leeft nog
        print(f"{monster['monster_type']} has {monster['life_points']} life points left")
    else:
        # Monster is dood
        print(f"{monster['monster_type']} beaten and died")


def print_stats(monster):
    print(f"{monster['monster_type']} - level {monster['level']}")

    if monster["life_points"] > 0:
        print(f"Life points: {monster['life_points']} / {monster['max_life_points']}")
    else:
        print("This particular monster exterminated")


def Battle(player, monster_list, experience_points_value):
    pass


def create_battle(player):
    difficulty = random.randint(1, 3)
    monster_list = []
    experience_points_value = 0

    for i in range(difficulty):
        monster_choice = random.choice(["Skeleton", "Troll"])

        if monster_choice == "Skeleton":
            monster = create_monster(monster_choice, player["level"])
        elif monster_choice == "Troll":
            monster = create_monster(monster_choice, player["level"])

        monster_list.append(monster)
        experience_points_value += monster["experience_points_value"]

    return Battle(player, monster_list, experience_points_value)


def fight_battle(battle):
    while True:
        print()
        print("---- BATTLE ROUND ----")
        battle_stats()
        player_action = input(
            "What action will you take ? (S)tats, (F)ight, (H)eal, (C)loak, (Q)uit: "
        ).upper()

        if player_action == "S":
            battle.player.print_stats()
            input("Press [Enter] to continue the battle: ")

        elif player_action == "F":
            battle.player_attack()
            monsters_alive = 0

            for monster in battle.monster_list:
                if monster.life_points > 0:
                    monsters_alive += 1

            if monsters_alive > 0:
                battle.monster_attack()

            else:
                break

        elif player_action == "H":
            battle.player_heal()
            print()
            battle.monster_attack()

        elif player_action == "C":
            battle.player_cloaking()
            battle.monster_attack()

        elif player_action == "Q":
            battle.player_quit()
            break

        if battle.player.experience_points <= 0:
            break


def main():
    player_name = input("What is your player name ?: ")
    player = create_player(player_name)
    print()
    print(f"Good battle player {player_name}. Try to defeat the monsters !")
    input("Press [Enter] to start the battle !")
    battle_count = 0

    while player["life_points"] > 0:
        print()
        print("-----")
        print()
        battle_count += 1
        print(f"Battle {battle_count}")
        battle = create_battle(player)
        fight_battle(battle)

    print()
    print(f"You have battled {battle_count} battles")
    print("Your final battle stats are:")
    print()
    print("Thnx for playing")


if __name__ == "__main__":
    main()
    player = create_player("John Doe")
    print_stats(player)
    attack(player)
    print_stats(player)
    weapon = create_item("weapon", 1)
    print_stats(weapon)
    armor = create_item("armor", 1)
    print_stats(armor)
    skeleton = create_monster("Skeleton", 1)
    print_stats(skeleton)
    attack(skeleton)
    print_stats(skeleton)
    troll = create_monster("Troll", 1)
    print_stats(troll)
    attack(troll)
    print_stats(troll)
