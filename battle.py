import random

from hero import Hero
from goblin import Goblin 

def battleStart():
    print(f"{"=" * 40}\n!Battle Start!\n{"=" * 40}")


def getTurns(enemies, hero):
    global entities
    entities = []
    entities += enemies
    entities.append(hero)
    random.shuffle(entities)
    print("~ TURN ORDER ~")
    for number,entity in enumerate(entities):
        print(f"{number} | {entity.name}")

def turn():
    for entity in entities:
        if type(entity) == Goblin:
            print("hi")
        if type(entity) == Hero:
            print("hero")

