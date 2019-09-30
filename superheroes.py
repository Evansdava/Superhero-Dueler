from random import randint, choice
from statistics import mean


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
        """Add armor to self.armors"""
        self.armors.append(armor)

    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)

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
        damage -= self.defend()
        if damage < 0:
            damage = 0
        self.current_health -= damage

    def is_alive(self):
        """Returns true or false depending on if the hero has health or not"""
        return self.current_health > 0

    def fight(self, opponent):
        """Current hero will take turns fighting the opponent hero that is
        passed in
        """
        if self.abilities != [] or opponent.abilities != []:
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

    def get_living_heroes(self, team):
        """Returns a list of living heroes"""
        hero_list = []
        for hero in team.heroes:
            if hero.is_alive():
                hero_list.append(hero)

        return hero_list

    def attack(self, other_team):
        """Battle each team against each other."""
        fighting = True
        team_one = []
        team_two = []

        while fighting:
            team_one.clear()
            team_two.clear()
            team_one = self.get_living_heroes(self)
            team_two = self.get_living_heroes(other_team)

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


class Arena:
    """Defines the arena in which battles take place"""

    def __init__(self):
        """Instantiate properties
        team_one: None
        team_two: None
        """
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        """Prompt for Ability information.
        return Ability with values from user Input
        """
        name = ""
        damage = ""
        while not name.isalpha():
            name = input("Please input an ability name: ")

        while not damage.isnumeric():
            damage = input(f"What is the maximum damage of {name}? ")

        ability = Ability(name, int(damage))
        return ability

    def create_weapon(self):
        """Prompt for Weapon information.
        return Weapon with values from user Input
        """
        name = ""
        damage = ""
        while not name.isalpha():
            name = input("Please input a weapon name: ")

        while not damage.isnumeric():
            damage = input(f"What is the maximum damage of {name}? ")

        weapon = Weapon(name, int(damage))
        return weapon

    def create_armor(self):
        """Prompt for Armor information.
        return Armor with values from user Input
        """
        name = ""
        defense = ""
        while not name.isalpha():
            name = input("Please input an armor name: ")

        while not defense.isnumeric():
            defense = input(f"What is the maximum damage {name} can block? ")

        armor = Armor(name, int(defense))
        return armor

    def create_hero(self):
        """Prompt for Hero information.
        return Hero with values from user Input
        """
        name = ""
        health = ""
        while not name.isalpha():
            name = input("Please input a hero name: ")

        while not health.isnumeric():
            health = input(f"What is the starting health of {name}? ")

        hero = Hero(name, int(health))

        choice = ""
        while not choice.isalpha():
            choice = input(f"Does {hero.name} have abilities? (y/n) ")

        if choice.lower()[0] == "y":
            while not choice.isnumeric():
                choice = input("How many? ")

            for _ in range(int(choice)):
                hero.add_ability(self.create_ability())

        choice = ""
        while not choice.isalpha():
            choice = input(f"Does {hero.name} have weapons? (y/n) ")
        if choice.lower()[0] == "y":
            while not choice.isnumeric():
                choice = input("How many? ")

            for _ in range(int(choice)):
                hero.add_weapon(self.create_weapon())

        choice = ""
        while not choice.isalpha():
            choice = input(f"Does {hero.name} have armors? (y/n) ")
        if choice.lower()[0] == "y":
            while not choice.isnumeric():
                choice = input("How many? ")

            for _ in range(int(choice)):
                hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        """Prompt the user to build team_one"""
        choice = ""

        choice = input("What's the name of team one? ")
        name = choice
        self.team_one = Team(name)

        choice = ""
        while not choice.isnumeric():
            choice = input(f"How many heroes are on {name}? ")

        for _ in range(int(choice)):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        """Prompt the user to build team_two"""
        choice = ""

        choice = input("What's the name of team two? ")
        name = choice
        self.team_two = Team(name)

        choice = ""
        while not choice.isnumeric():
            choice = input(f"How many heroes are on {name}? ")

        for _ in range(int(choice)):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        """Battle team_one and team_two together."""
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        first = randint(1, 2)
        if first == 1:
            self.team_one.attack(self.team_two)
        else:
            self.team_two.attack(self.team_one)

    def show_stats(self):
        """Prints team statistics to terminal."""
        # Show both teams average kill/death ratio.
        team_one_heroes = self.team_one.get_living_heroes(self.team_one)
        team_two_heroes = self.team_two.get_living_heroes(self.team_two)
        if team_one_heroes != []:
            print(f"\n{self.team_one.name} wins the match!")
            print("Survivors:")
            for hero in team_one_heroes:
                print(hero.name)
        elif team_two_heroes != []:
            print(f"\n{self.team_two.name} wins the match!")
            print("Survivors:")
            for hero in team_two_heroes:
                print(hero.name)
        else:
            print("It's a draw")

        def average_kd(team):
            k_num_list = []
            d_num_list = []
            for hero in team.heroes:
                k_num_list.append(hero.kills)
                d_num_list.append(hero.deaths)
            return mean(k_num_list), mean(d_num_list)

        print(f"\n{self.team_one.name}:")
        self.team_one.stats()
        k, d = average_kd(self.team_one)
        print(f"Average | {k} / {d}")

        print(f"\n{self.team_two.name}:")
        self.team_two.stats()
        k, d = average_kd(self.team_two)
        print(f"Average | {k} / {d}")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
