from random import randint, choice


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


class Weapon(Ability):
    """Defines weapons used for attacks"""

    def attack(self):
        """This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage // 2, self.max_damage)


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
        self.kills = 0
        self.deaths = 0

    def add_kill(self, num_kills):
        """Update kills with num_kills"""
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        """Update deaths with num_deaths"""
        self.deaths += num_deaths

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

    def defend(self):
        """Runs block method on all armors.
        Returns sum of all blocks.
        """
        total = 0
        for armor in self.armors:
            total += armor.block()

        return total

    def take_damage(self, damage):
        """Updates current health to reflect the damage minus the defense"""
        self.current_health -= (damage - self.defend())

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
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f"{opponent.name} wins!")
                self.add_deaths(1)
                opponent.add_kill(1)
        else:
            print("Draw")


class Team():
    """Defines team of heroes"""

    def __init__(self, name):
        """Initialize team with name (string)"""
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """Add a hero to the heroes list"""
        self.heroes.append(hero)

    def remove_hero(self, name):
        """Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return

        return 0

    def view_all_heroes(self):
        """Print a list of all the heroes' names"""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """Battle each team against each other."""
        fighting = True
        team_one = []
        team_two = []

        while fighting:
            team_one.clear()
            team_two.clear()
            for hero in self.heroes:
                if hero.is_alive():
                    team_one.append(hero)
            for hero in other_team.heroes:
                if hero.is_alive():
                    team_two.append(hero)

            if len(team_one) <= 0 or len(team_two) <= 0:
                fighting = False
            else:
                hero_one = choice(team_one)
                hero_two = choice(team_two)
                hero_one.fight(hero_two)

    def revive_heroes(self):
        """Reset all heroes health to starting_health"""
        for hero in self.heroes:
            hero.health = hero.starting_health

    def stats(self):
        """Print team statistics"""
        print(f"Name | Kills / Deaths")
        for hero in self.heroes:
            print(f"{hero.name} | {hero.kills} / {hero.deaths}")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    team1 = Team("One")
    team2 = Team("Two")
    hero1 = Hero("Wonder Woman")
    hero3 = Hero("Manman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero3.add_ability(ability4)
    team1.add_hero(hero1)
    team2.add_hero(hero2)
    team2.add_hero(hero3)
    team1.attack(team2)
