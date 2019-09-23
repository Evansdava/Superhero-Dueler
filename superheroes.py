from random import randint


class Ability:
    def __init__(self, name, attack_strength):
        """Create instance variables:
            name: String
            attack_strength: Integer
        """
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        """ Return a value between 0 and the value set by attack_strength """
        return randint(0, self.attack_strength)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
