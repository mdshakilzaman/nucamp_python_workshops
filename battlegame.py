# Make an infinite loop
while True:
    # Task 1: setting up variables
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 130

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 60

    dragon_hp = 300
    dragon_damage = 50
    # Task 2 and 3: choose from a list of option and infinite loop
    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        character = input("choose your character: ")

        if character == "1" or character.lower() == wizard.lower():
            print("You have chosen character: ", wizard)
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("Health: ", my_hp)
            print("Damage: ", my_damage)
            print("\n")
            break
        elif character == "2" or character.lower() == elf.lower():
            print("You have chosen character: ", elf)
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("Health: ", my_hp)
            print("Damage: ", my_damage)
            print("\n")
            break
        elif character == "3" or character.lower() == human.lower():
            print("You have chosen character: ", human)
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("Health: ", my_hp)
            print("Damage: ", my_damage)
            print("\n")
            break
        elif character == "4" or character.lower() == orc.lower():
            print("You have chosen character: ", orc)
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print("Health: ", my_hp)
            print("Damage: ", my_damage)
            print("\n")
            break
        else:
            print("Unknown character")

    # Task 4: Battle with dragon
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The dragon's hitpoints are now: ", dragon_hp)
        print("\n")
        if dragon_hp <= 0:
            print("The dragon has lost the battle.")
            print("\n")
            break
        print("The dragon strikes back at", character)
        my_hp = my_hp - dragon_damage
        print("The", character, "'s hitpoints are now: ", my_hp)
        print("\n")
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            print("\n")
            break

    ex = input("Exit? Yes:'Y' or No:'N' \n")
    if ex == 'Y' or ex == 'y':
        break
    else:
        continue
