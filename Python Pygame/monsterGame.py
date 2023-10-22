# Om klassen en subklassen in Python te maken en te gebruiken, kun je de principes van objectgeoriënteerd programmeren (OOP) volgen. In OOP worden klassen gebruikt om objecten te maken die eigenschappen en gedragingen delen. Hier is een voorbeeld van hoe je de klasse "Monster" en de subklassen "Predator" en "Alien" kunt maken:


# Definieer de klasse Monster
class Monster:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def make_sound(self):
        return "Grrrr!"


# Definieer de subklasse Predator, die Monster erft
class Predator(Monster):
    def __init__(self, name, strength, prey_type):
        super().__init__(name, strength)
        self.prey_type = prey_type

    def make_sound(self):
        return "Roar!"


# Definieer de subklasse Alien, die Monster erft
class Alien(Monster):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength)
        self.planet = planet

    def make_sound(self):
        return "Zzzzzap!"


# Maak een instantie van Monster
monster1 = Monster("Generic monster", 50)
# Maak een instantie van Predator
predator1 = Predator("Shadowfang", 100, "humans")
# Maak een instantie van Alien
alien1 = Alien("Lumina", 80, "Mars")

# Gebruik de methoden van de objecten
print(f"{monster1.name} says {monster1.make_sound()}")
# Output: Generic Monster says Grrrr!
print(
    f"{predator1.name} is a {predator1.prey_type} predator and says {predator1.make_sound()}"
)
# Output: Shadowfang is a humans predator and says Roar!
print(f"{alien1.name} is from {alien1.planet} and says {alien1.make_sound()}")
# Output: Lumina is from Mars and says Zzzzzap!

#  In dit voorbeeld is de klasse `Monster` de basisklasse die twee attributen (`name` en `strength`) en één methode (`make_sound`) heeft. De subklassen `Predator` en `Alien` erven van de `Monster`-klasse en breiden deze uit met extra attributen (`prey_type` en `planet`) en een eigen implementatie van de methode `make_sound`.
# De subklasse heeft een constructor methode "init" die parameters voor naam, sterkte en prooidier-type ontvangt. Het roept de constructor van de ouderklasse aan met behulp van de "super()" functie en geeft de naam- en sterkte-parameters door. Vervolgens initialiseert het de "prey_type" attribuut met de waarde die als parameter is doorgegeven.
# Daarnaast heeft de subklasse een methode genaamd "make_sound" die de string "Roar!" retourneert.
# Let op dat de methode `make_sound` in de subklassen de methode in de basisklasse overschrijft, wat polymorfisme mogelijk maakt. Bij het aanroepen van `make_sound()` wordt de juiste implementatie op basis van het objecttype uitgevoerd.
