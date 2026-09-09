from goblin import Goblin

goblinNames = ["Gorgle", "Snaggletooth", "Grizzle", "Fang", "Goblin The Third", 
               "Gobblin","Snoblin","Boblin","Moglin","Zoglin"]
ARENA_NAME = "The Arena"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gorgle")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
