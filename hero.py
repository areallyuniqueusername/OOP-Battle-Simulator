import random


class Hero:
    def __init__(self, name, health, attack_power, class_type, inventory, equippedArmor):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.class_type = class_type
        self.inventory = inventory
        self.equippedArmor = equippedArmor
    def __str__(self):
        return f"Hero {self.name}: Health={self.health}, Attack Power={self.attack_power}, Class={self.class_type}, Inventory={self.inventory}"

    def attack(self):
        damage = random.randint(1, self.attack_power)

        if damage == 1:
            print(f"{self.name} attacks and deals {damage} damage! (MISS)")

        if random.randint(0,50) == 0:
            damage *= 2
            print(f"{self.name} attacks and deals {damage} damage! (CRIT)")
        
        return damage
    def take_damage(self, damage):
        if self.equippedArmor:
            damage = damage // self.equippedArmor.defense
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. \n ♥ Health: {self.health} ♥")


    def is_alive(self):
        
        return self.health > 0



    