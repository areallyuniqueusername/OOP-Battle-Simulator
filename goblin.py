import random
class Goblin:

    def __init__(self, name, minHP, maxHP, attack, specialMoves, agility):
        self.name = name
        self.health = random.randint(minHP, maxHP)
        self.attack_power = attack
        self.specialMoves = specialMoves
        self.agility = random.randint(agility-5, agility+5) if agility > 5 else random.randint(1, agility+5)

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        self.is_alive()

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"\n|{self.name} ~~~\n|♥ Health - {self.health} ♥\n|Attack Power - {self.attack_power}\n|Agility - {self.agility}\n"