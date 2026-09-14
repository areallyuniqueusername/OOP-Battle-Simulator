def chooseName():
    while True:
        heroName = str(input("Enter your hero's name: "))
        if heroName.strip() == "" or len(heroName) > 20 or len(heroName) < 3:
            print("Please enter a valid name.")
            continue
        else:
            return heroName

def chooseClass():
    classes = ["Warrior", "Mage", "Rogue","Ranger"]
    print("Please type 'back' or 'z' to go back to name selection.\nChoose your class:")
    for i, class_name in enumerate(classes, start=1):
        print(f"{i}. {class_name}")
    
    while True:
        choice = input("Enter the number of your chosen class: ")
        if choice.isdigit() and 1 <= int(choice) <= len(classes):
            return classes[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
        if choice.lower() == "back" or choice.lower() == "z":
            return None