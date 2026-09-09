from goblin import Goblin
import random
goblins = {
    "Gorgle":{"minhealth":10, "maxhealth":20,"attack":10},
    "Snaggletooth":{"minhealth":15, "maxhealth":25,"attack":15},
    "Grizzle":{"minhealth":20, "maxhealth":30,"attack":20},
    "Fang":{"minhealth":25, "maxhealth":35,"attack":25},
    "Goblin the Third":{"minhealth":200, "maxhealth":200,"attack":40},
    "Gobblin":{"minhealth":30, "maxhealth":40,"attack":1},
    "Snoblin":{"minhealth":35, "maxhealth":45,"attack":20},
    "Boblin":{"minhealth":40, "maxhealth":50,"attack":15},
    "Fly": {"minhealth":1, "maxhealth":1,"attack":1},
    "Duke of Flies": {"minhealth":100, "maxhealth":100,"attack":50},
}
ARENA_NAME = "The Arena"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    chosenGoblin = random.choice(list(goblins.keys()))

    goblin = Goblin(chosenGoblin, goblins[chosenGoblin]["minhealth"], goblins[chosenGoblin]["maxhealth"], goblins[chosenGoblin]["attack"])

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
