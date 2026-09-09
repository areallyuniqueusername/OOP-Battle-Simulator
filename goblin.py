import random
class Goblin:

    def __init__(self, name, minHP, maxHP, attack):
        self.name = name
        self.health = random.randint(minHP, maxHP)
        self.attack_power = attack

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
