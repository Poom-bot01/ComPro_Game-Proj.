# SHOW PLAYER STATUS
with open("Player Starting Information.txt") as fin:
    gold = int(fin.readline().split("=")[1].strip())
    hp = int(fin.readline().split("=")[1].strip())
    mana = int(fin.readline().split("=")[1].strip())
    attack = int(fin.readline().split("=")[1].strip())

def show_status():
    print()
    print("==========================================")
    print("|             TRADING STAGE              |")
    print("==========================================")
    print(f"| GOLD   : {gold} G                         |")
    print(f"| HP     : {hp}                            |")
    print(f"| Mana   : {mana}                            |")
    print(f"| Attack : {attack}                            |")
    print("==========================================")

# SHOW SHOP

def show_shop():
    print()
    print("============== BAZAAR WARES ==============")
    print("| [1] Ironclad Breastplate   - 120 G     |")
    print("| [2] Crown of Fallen King   - 200 G     |")
    print("| [3] Amulet of Endless Void - 180 G     |")
    print("| [4] Rune-Carved Dagger     - 150 G     |")
    print("==========================================")

# MAIN GAME
if __name__ == "__main__":

    show_status()
    show_shop()

    print()
    print("[1-4] Select Item")
    print("[Q] Quit")

    purchase = 0

    while purchase < 1:

        choice = input("COMMAND > ")

        # ITEM 1

        if choice == "1":

            print()
            print("**************************************************")
            print("| SELECTED: Ironclad Breastplate                 |")
            print("| CLUE: Cold metal remembers battles of the past.|")
            print("| REVEALED STATS: ???                            |")
            print("**************************************************")

            print()
            print("[B] Buy Blind (120G)")
            print("[A] Appraise (30G)")

            action = input("ACTION > ").lower()

            if action == "a":

                if gold >= 30:
                    gold = gold - 30

                    print()
                    print("APPRAISAL COMPLETE")
                    print("EFFECT: Double HP, +20 Attack")
                    print(f"Gold : {gold} G")

                    buy = input("Buy item? (Y/N): ").lower()

                    if buy == "y":

                        if gold >= 120:
                            gold = gold - 120
                            hp = hp * 2
                            attack = attack + 20
                            purchase += 1
                            print("Item bought!")
                            print(f"Your HP have been increased to {hp}.")
                            print(f"Your Attack have been increased to {attack}.")
                            print(f"Gold : {gold} G")

                        else:
                            print("Not enough gold.")

                    elif buy == "n":
                        purchase = purchase
                    

                else:
                    print("Not enough gold for appraisal.")

            elif action == "b":

                if gold >= 120:
                    gold = gold - 120
                    hp = hp * 2
                    attack = attack + 20
                    purchase += 1

                    print("You bought the item blindly.")
                    print("EFFECT: Double HP, +20 Attack")
                    print(f"Your HP have been increased to {hp}.")
                    print(f"Your Attack have been increased to {attack}.")
                    print(f"Gold : {gold} G")

                else:
                    print("Not enough gold.")

        # ITEM 2

        elif choice == "2":

            print()
            print("***************************************************")
            print("| SELECTED: Crown of Fallen King                  |")
            print("| CLUE: The inner rim is stained with dried blood.|")
            print("| REVEALED STATS: ???                             |")
            print("***************************************************")

            print()
            print("[B] Buy Blind (200G)")
            print("[A] Appraise (30G)")

            action = input("ACTION > ").lower()

            if action == "a":

                if gold >= 30:
                    gold = gold - 30

                    print()
                    print("APPRAISAL COMPLETE")
                    print("WARNING: CURSED ITEM!")
                    print(f"Gold : {gold} G")

                    buy = input("Buy item? (Y/N): ").lower()

                    if buy == "y":

                        if gold >= 200:
                            gold = gold - 200
                            hp = 0
                            purchase += 1

                            print("You bought the cursed crown.")
                            print(f"You just have {hp} HP because the curse removed all your HP.")
                            print(f"Gold : {gold} G")

                        else:
                            print("Not enough gold.")

                    elif buy == "n":
                        purchase = purchase

                else:
                    print("Not enough gold for appraisal.")

            elif action == "b":

                if gold >= 200:
                    gold = gold - 200
                    hp = 0
                    purchase += 1

                    print("You bought the item blindly.")
                    print("You bought the cursed crown.")
                    print(f"You just have {hp} HP because the curse removed all your HP.")
                    print(f"Gold : {gold} G")

                else:
                    print("Not enough gold.")

        # ITEM 3

        elif choice == "3":
    
            print()
            print("*****************************************************")
            print("| SELECTED: Amulet of Endless Void                  |")
            print("| CLUE: A silent darkness follows whoever holds it. |")
            print("| REVEALED STATS: ???                               |")
            print("*****************************************************")
    
            print()
            print("[B] Buy Blind (180G)")
            print("[A] Appraise (30G)")
    
            action = input("ACTION > ").lower()
    
            if action == "a":
    
                if gold >= 30:
                    gold = gold - 30
    
                    print()
                    print("APPRAISAL COMPLETE")
                    print("EFFECT: -30 HP, +15 Mana")
                    print(f"Gold : {gold} G")
    
                    buy = input("Buy item? (Y/N): ").lower()
    
                    if buy == "y":
    
                        if gold >= 180:
                            gold = gold - 180
                            hp = hp - 30
                            mana = mana + 15
                            purchase += 1
    
                            if hp < 0:
                                hp = 0
    
                            print("Item bought!")
                            print("HP decreased by 30. Mana increased by 15.")
                            print(f"Now, your HP is {hp}.")
                            print(f"Now, your Mana is {mana}.")
                            print(f"Gold : {gold} G")
    
                        else:
                            print("Not enough gold.")

                    elif buy == "n":
                        purchase = purchase
    
                else:
                    print("Not enough gold for appraisal.")
    
            elif action == "b":
    
                if gold >= 180:
                    gold = gold - 180
                    hp = hp - 30
                    mana = mana + 15
                    purchase += 1
    
                    if hp < 0:
                        hp = 0
    
                    print("You bought the item blindly.")
                    print("HP decreased by 30. Mana increased by 15.")
                    print(f"Now, your HP is {hp}.")
                    print(f"Now, your Mana is {mana}.")
                    print(f"Gold : {gold} G")
    
                else:
                    print("Not enough gold.")

        # ITEM 4

        elif choice == "4":
    
            print()
            print("*******************************************************")
            print("| SELECTED: Rune-Carved Dagger                        |")
            print("| CLUE: Ancient symbols glow beneath the worn handle. |")
            print("| REVEALED STATS: ???                                 |")
            print("*******************************************************")
    
            print()
            print("[B] Buy Blind (150G)")
            print("[A] Appraise (30G)")
    
            action = input("ACTION > ").lower()
    
            if action == "a":
    
                if gold >= 30:
                    gold = gold - 30
    
                    print()
                    print("APPRAISAL COMPLETE")
                    print("EFFECT: +40 HP, -10 Attack")
                    print(f"Gold : {gold} G")
    
                    buy = input("Buy item? (Y/N): ").lower()
    
                    if buy == "y":
    
                        if gold >= 150:
                            gold = gold - 150
                            hp = hp + 40
                            attack = attack - 10
                            purchase += 1
    
                            print("Item bought!")
                            print("HP increased by 40. Attack decreased by 10.")
                            print(f"Your HP have raised to {hp}.")
                            print(f"Your Attack is now {attack}.")
                            print(f"Gold : {gold} G")
    
                        else:
                            print("Not enough gold.")

                    elif buy == "n":
                        purchase = purchase
    
                else:
                    print("Not enough gold for appraisal.")
    
            elif action == "b":
    
                if gold >= 150:
                    gold = gold - 150
                    hp = hp + 40
                    attack = attack - 10
                    purchase += 1
    
                    print("You bought the item blindly.")
                    print("HP increased by 40. Attack decreased by 10.")
                    print(f"Your HP have raised to {hp}.")
                    print(f"Your Attack is now {attack}.")
                    print(f"Gold : {gold} G")
    
                else:
                    print("Not enough gold.")
                    

        # QUIT

        elif choice.lower() == "q":

            print()
            print("You left the Trading Stage.")
            print("Thank you for playing!")
            break

        # INVALID INPUT

        else:

            print()
            print("Invalid command.")
            print("Please choose 1-4 or Q.")

        # CHECK GAME STATUS

        if hp <= 0:

            print()
            print("==========================================")
            print("|                GAME OVER               |")
            print("==========================================")
            print("Your HP reached 0.")


        if hp >= 100:

            print()
            print("==========================================")
            print("|             STAGE COMPLETE             |")
            print("==========================================")
            print("You reached 100 HP!")
            print("Congratulations!")
        
