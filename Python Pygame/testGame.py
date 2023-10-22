# Hero Classes
class Warrior(object):
    health = 50
    strength = 10
    defence = 10
    magic = 1


class Wizard(object):
    health = 125
    strength = 7
    defence = 7
    magic = 10


class Elf(object):
    health = 100
    strength = 5
    defence = 10
    magic = 7


def hero_select():
    print("Select your hero!")
    selection = input("1. Warrior \n2. Wizard \n3. Elf \n")

    if selection == "1":
        character = Warrior
        print("You have selected the warrior...These are his stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character
    elif selection == "2":
        character = Wizard
        print("You have selected the wizard...These are his stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character
    elif selection == "3":
        character = Elf
        print("You have selected the elf...These are his stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character
    else:
        print("Only press 1, 2 or 3")
        hero_select()


hero_select()
