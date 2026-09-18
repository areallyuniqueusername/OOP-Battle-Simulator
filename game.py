from goblin import Goblin
import random
from hero import Hero
from choosingCharacter import chooseName, chooseClass

goblins = {
    "Gorgle":{"minhealth":10, "maxhealth":20,"attack":10,"slots": 1,"specialMoves":True,"agility": 0},
    "Snaggletooth":{"minhealth":15, "maxhealth":25,"attack":15,"slots": 1,"specialMoves":False,"agility": 7},
    "Grizzle":{"minhealth":20, "maxhealth":30,"attack":20,"slots": 1,"specialMoves":False,"agility": 3},
    "Fang":{"minhealth":25, "maxhealth":35,"attack":25,"slots": 1,"specialMoves":False,"agility": 9},
    "Goblin the Third":{"minhealth":200, "maxhealth":200,"attack":40,"slots": 2,"specialMoves":True,"agility": 10},
    "Gobblin":{"minhealth":30, "maxhealth":40,"attack":1,"slots": 1,"specialMoves":False,"agility": 4},
    "Snoblin":{"minhealth":35, "maxhealth":45,"attack":20,"slots": 1,"specialMoves":False,"agility": 6},
    "Boblin":{"minhealth":40, "maxhealth":50,"attack":15,"slots": 1,"specialMoves":False,"agility": 4},
    "Fly": {"minhealth":1, "maxhealth":1,"attack":1,"slots": 0,"specialMoves":False,"agility": 1},
    "Duke of Flies": {"minhealth":100, "maxhealth":100,"attack":50,"slots": 2,"specialMoves":True,"agility": 1},
}
ARENA_NAME = "The Arena"
spawnedEnemies = []

def main():
    slots = 2

    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    while not slots == 0:
        chosenGoblin = random.choice(list(goblins.keys()))
        if goblins[chosenGoblin]["slots"] > slots:
            continue
        slots -= goblins[chosenGoblin]["slots"]
        goblin = Goblin(chosenGoblin, 
                        goblins[chosenGoblin]["minhealth"], 
                        goblins[chosenGoblin]["maxhealth"], 
                        goblins[chosenGoblin]["attack"],
                        goblins[chosenGoblin]["specialMoves"],
                        goblins[chosenGoblin]["agility"])
    
        print(f"{goblin.name} enters the arena with {goblin.health} health.\n")
        print(f"{goblin.name} costed {goblins[chosenGoblin]['slots']} slots. {slots} slots remaining.")
        spawnedEnemies.append(goblin)


    print("\n~~ Hero's Name Input ~~")
    heroName = chooseName()

    print("\n~~ Hero's Class Selection ~~")
    chosenClass = chooseClass()

    while True:
        if chosenClass is None:
            print("Going back to name selection.")
            heroName = chooseName()
            print("\n~~ Hero's Class Selection ~~")
            chosenClass = chooseClass()
        else:
            break
    
    hero = Hero(heroName, 100, 10, chosenClass, [], None)
    hero.take_damage(20)
    hero.attack()
    print(hero)
    hero.take_damage(80)
    print(hero.is_alive())
    while True:
        try:
            index = int(input("Enter a Goblin num: (1-2) |  ")) - 1
            if 0 <= index < len(spawnedEnemies):
                print(spawnedEnemies[index])
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
