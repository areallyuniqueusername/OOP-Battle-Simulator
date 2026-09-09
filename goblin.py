import random

class Goblin:

    def __init__(self, name):
        self.name = name
        if self.name == "Goblin the Third":
            self.health = 300
            self.attack_power = 25
        else:
            self.health = random.randint(20, 120)
            self.attack_power = random.randint(10, 20)

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
