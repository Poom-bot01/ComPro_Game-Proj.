import time
import clear_screen

def level_up(player):
    souls_cost = player.level * 10 + 50
    choice = input("Level up all at once[1]/Just one level[2]: ")

    try:
        choice = int(choice)
        if choice == 1:
            while player.souls >= souls_cost:
                player.level += 1
                player.max_health += 100
                player.max_stamina += 10
                player.souls -= souls_cost
                souls_cost = player.level * 10 + 50
            print("You do not have enough souls to level up further.")
        elif choice == 2:
            if player.souls >= souls_cost:
                player.level += 1
                player.max_health += 20
                player.max_stamina += 10
                player.souls -= souls_cost
            else:
                print("You do not have enough souls to level up.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def want_level_up(player):
    while True:
        souls_cost = player.level * 10 + 50
        print(f"You have {player.souls} souls. Leveling up will cost {souls_cost} souls.")
        want_lv_up = input("Do you want to level up? [Y/N]: ")
        
        if want_lv_up.lower() == "y":
            old_level = player.level
            old_souls = player.souls
            old_health = player.max_health
            old_stamina = player.max_stamina
            
            level_up(player)
            
            print(f"Congratulations! You are now level {player.level}!")
            print(f"Health: {old_health} >> {player.max_health}")
            print(f"Stamina: {old_stamina} >> {player.max_stamina}")
            print(f"Souls: {old_souls} >> {player.souls}")
            time.sleep(2)
            clear_screen.clear_screen()
            break
        elif want_lv_up.lower() == "n":
            time.sleep(2)
            clear_screen.clear_screen()
            break
        else:
            print("Invalid choice. Please enter Y or N.")

if __name__ == "__main__":
    pass
