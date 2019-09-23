from random import randint


class Ability:
    """Defines ability names and damage"""

    def __init__(self, name, max_damage):
        """Create instance variables:
        name: String
        max_damage: Integer
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """Return a value between 0 and the value set by max_damage"""
        return randint(0, self.max_damage)


class Armor:
    """Defines armor"""

    def __init__(self, name, max_block):
        """Instantiate instance properties.
        name: String
        max_block: Integer
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return a random value between 0 and the value set by max_block"""
        return randint(0, self.max_block)


class Hero:
    """Defines properties of heroes to do battle"""

    def __init__(self, name, starting_health=100):
        """Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        """Add ability to abilities list"""
        self.abilities.append(ability)

    def add_armor(self, armor):
        """Add armor to armor list"""
        self.armors.append(armor)

    def attack(self):
        """Calculate total attack from all abilities
        return: total:int
        """
        total = 0
        for ability in self.abilities:
            total += ability.attack()

        return total

    def defend(self, damage_amt):
        """Runs block method on all armors.
        Returns sum of all blocks.
        """
        total = 0
        for armor in self.armors:
            total += armor.block()

        return total

    def take_damage(self, damage):
        """Updates current health to reflect the damage minus the defense"""
        self.current_health -= (damage - self.defend(damage))

    def is_alive(self):
        """Returns true or false depending on if the hero has health or not"""
        return self.current_health > 0

    def fight(self, opponent):
        """Current hero will take turns fighting the opponent hero that is
        passed in
        """
        if self.abilities != [] and opponent.abilities != []:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                print(f"{opponent.name} has {opponent.current_health} health!")
                self.take_damage(opponent.attack())
                print(f"{self.name} has {self.current_health} health!")

            if self.is_alive():
                print(f"{self.name} wins!")
            else:
                print(f"{opponent.name} wins!")
        else:
            print("Draw")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
