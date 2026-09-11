from goblin import Goblin
import random
goblins = {
    "Gorgle":{"minhealth":10, "maxhealth":20,"attack":10,"slots": 1,"specialMoves":True},
    "Snaggletooth":{"minhealth":15, "maxhealth":25,"attack":15,"slots": 1,"specialMoves":False},
    "Grizzle":{"minhealth":20, "maxhealth":30,"attack":20,"slots": 1,"specialMoves":False},
    "Fang":{"minhealth":25, "maxhealth":35,"attack":25,"slots": 1,"specialMoves":False},
    "Goblin the Third":{"minhealth":200, "maxhealth":200,"attack":40,"slots": 2,"specialMoves":True},
    "Gobblin":{"minhealth":30, "maxhealth":40,"attack":1,"slots": 1,"specialMoves":False},
    "Snoblin":{"minhealth":35, "maxhealth":45,"attack":20,"slots": 1,"specialMoves":False},
    "Boblin":{"minhealth":40, "maxhealth":50,"attack":15,"slots": 1,"specialMoves":False},
    "Fly": {"minhealth":1, "maxhealth":1,"attack":1,"slots": 0,"specialMoves":False},
    "Duke of Flies": {"minhealth":100, "maxhealth":100,"attack":50,"slots": 2,"specialMoves":True},
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
                        goblins[chosenGoblin]["specialMoves"])
    
        print(f"{goblin.name} enters the arena with {goblin.health} health.\n")
        print(f"{goblin.name} costed {goblins[chosenGoblin]['slots']} slots. {slots} slots remaining.")
        spawnedEnemies.append(goblin)
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
