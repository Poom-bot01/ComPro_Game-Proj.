import enemy_file
import leveling_system
import login as lg
import random
import intro
import map
import clear_screen
import gvocab
import time
import maze
import score_board111

class Character:

    def __init__(self,name):
        self.level = 1
        self.name = name
        self.max_health = 100 + (self.level * 50)
        self.health = self.max_health
        self.max_stamina = 50 + (self.level * 20)
        self.stamina = self.max_stamina
        self.souls = 0
        self.deaths = 0


    def attack(self,attack_type):
        if attack_type.lower() == "light":
                if self.stamina >= 15:
                    print(f"{self.name} performs a [LIGHT] attack!\n")
                    
                    self.stamina -= 15
                    return random.randint(10,15) + self.level * 1.5

                else:
                    print("Not enough stamina for a [LIGHT] attack.\n")
                    return 0
            
        if attack_type.lower() == "heavy":
                if self.stamina >= 25:
                    print(f"{self.name} performs a [HEAVY] attack!\n")
                    self.stamina -= 25
                    return random.randint(100,1000) +    self.level * 3

                else:
                    print("Not enough stamina for a [HEAVY] attack.\n")
                    return 0

    def cast_spell(self,spell_type):
        if spell_type == "heal":
            if self.stamina >= 50:
                print(f"{self.name} has cast a [HEALING] spell!\n")
                self.stamina -= 50
                self.health += (self.level * 5) + 50
                if self.health > self.max_health:
                    self.health = self.max_health
            else:
                print("Not enough stamina to cast a [HEALING] spell.\n")

        elif spell_type == "magic":
            if player.stamina >= 50:
                print(f"{self.name} has cast a [MAGIC] spell!\n")
                self.stamina -= 50
                return random.randint(40,60) + (self.level * 2.0)
            else:
                print("Not enough stamina to cast a [MAGIC] spell.\n")
                return 0
        


    def block(self):
        print(f"{self.name} blocks the attack and regenerates stamina!\n")
        self.stamina += 15
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina


    def get_souls(self, enemy):
        self.souls += enemy.souls()
        print(f"\nYou have gained {enemy.souls()} souls from  defeating {enemy.name}!")
        print(f"Total Souls: {self.souls}\n")

    def up_grade(self,player):
        leveling_system.level_up(player)

    def restore_health_and_stamina(self):
        self.health = self.max_health
        self.stamina = self.max_stamina
        print("Restored Health and Stamina")


def battle(player,enemy):
    print(f"You are facing {enemy.name}!")
    

    while player.health > 0 and enemy.health > 0:
        print(f"{enemy.name} Health: {enemy.health}")
        enemy.charecter()
        print(f"Name: {player.name}")
        print(f"\nHealth: {player.health}, Stamina: {player.stamina}, Souls: {player.souls}")
        

        action = input("Choose your action: (light/heavy/spell/block) ").lower()

        if action == "light":
            dmg = player.attack(action)
        elif action == "heavy":
            dmg = player.attack(action)

        elif action == "spell":
            select_spell = input("Magic / Heal: ").lower()
            if select_spell == "magic":
                dmg = player.cast_spell(select_spell)
            elif select_spell == "heal":
                before_heal = player.health
                player.cast_spell(select_spell)
                dmg = 0
                print(f"Cast a healing spell, now your health is {before_heal} >> {player.health}")
            else:
                print("Wrong input! Try again.")
                continue

        elif action == "block":
            player.block()
        else:
            print("Invalid action!")
            continue
        

        if action in ["light", "heavy", "spell"]:
            enemy.health = enemy.health - dmg
            print(f"{player.name} was dealt {dmg} to {enemy.name}!")

        

        if enemy.health <= 0:
            print(f"You defeated the {enemy.name}!")
            player.get_souls(enemy)
            leveling_system.want_level_up(player)

        else:
            atk_type, enemy_dmg = enemy.rand_atk()
            if action == "block":
                player.health -= enemy_dmg * 0.8
            else:
                player.health -= enemy_dmg
            print(f"{enemy.name} used a {atk_type} attack and dealt {enemy_dmg} damage to you!")
 

        if player.health <= 0:
            print(f"""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗ ██╗   ██╗███████╗    ███████╗ █████╗ ██╗     ██╗     ███████╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║  ██║██╔══██╗██║   ██║██╔════╝    ██╔════╝██╔══██╗██║     ██║     ██╔════╝████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ███████║███████║██║   ██║█████╗      █████╗  ███████║██║     ██║     █████╗  ██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝      ██╔══╝  ██╔══██║██║     ██║     ██╔══╝  ██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║ ╚████╔╝ ███████╗    ██║     ██║  ██║███████╗███████╗███████╗██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝
                                                                                                                      .""")
            time.sleep(2)
            clear_screen.clear_screen()
            player.deaths += 1
            return False
        
        print(f"Your stamina {player.stamina} >> {player.stamina + 5}\n")
        player.stamina += 5
        
        time.sleep(1)
        #clear_screen.clear_screen()
    return True


def save_game(player, current_map):
    with open(f"{player.name}save_game.txt", "w") as save_file:
        save_file.write(f"{player.name}\n")
        save_file.write(f"{player.level}\n")
        save_file.write(f"{player.max_health}\n")
        save_file.write(f"{player.health}\n")
        save_file.write(f"{player.max_stamina}\n")
        save_file.write(f"{player.stamina}\n")
        save_file.write(f"{player.souls}\n")
        save_file.write(f"{player.deaths}\n")
        save_file.write(f"{current_map}\n")

    print("Game saved successfully.")
    

def load_game(player_name):
    try:
        with open(f"{player_name}save_game.txt", "r") as save_file:
            lines = save_file.readlines()
        
        # Reconstruct the player object
        player = Character(lines[0].strip())  # Player name
        player.level = int(lines[1].strip())
        player.max_health = float(lines[2].strip())
        player.health = float(lines[3].strip())
        player.max_stamina = float(lines[4].strip())
        player.stamina = float(lines[5].strip())
        player.souls = float(lines[6].strip())
        player.deaths = float(lines[7].strip())

        # Get the current map
        current_map = lines[8].strip()
        
        print("Game loaded successfully.")
        return player, current_map
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        return None, None

def main_loop(player,current_map):
    while True:

        if current_map.lower() == 'courtyard':
            player.restore_health_and_stamina()
            map.courtyard(player)
            print("You have entered the Courtyard.")
            enemies_courtyard = enemy_file.generate_enemies(player.level)
            print(f"You are facing {len(enemies_courtyard)} enemies! Prepare for your battle.")
            for enemy in enemies_courtyard:
                if not battle(player,enemy):
                    score_board111.save_score(player)
                    print("You must replay the Courtyard.")
                    current_map = 'courtyard'  
                    break
                else:
                    
                    
                    current_map = "armory"
                    save_game(player, current_map)
     
        elif current_map.lower() == 'armory':
            print("You have cleared the Courtyard!\n")
            player.restore_health_and_stamina()
            map.armory()
            enemies_armory = enemy_file.generate_enemies(player.level)
            print(f"You are facing {len(enemies_armory)} enemies! Prepare for your battle.")
            for enemy in enemies_armory:
                if not battle(player,enemy):
                    score_board111.save_score(player)
                    print("You must replay the Armory.")
                    current_map = 'armory'  
                else:
                    
                
                    save_game(player, current_map)
                    current_map ="treasury"


        elif current_map == 'treasury':
            player.restore_health_and_stamina()
            print("You have cleared the Armory!\n")
            current_map = map.treasury()
            player.restore_health_and_stamina()
            gvocab.thaijai(player)
            current_map = map.library()
            save_game(player, current_map)
            current_map ="library"


        elif current_map == 'library':
            player.restore_health_and_stamina()
            maze.main(player)
            player.up_grade(player)
            current_map = map.throne_room()
            save_game(player, current_map)
            current_map ="throne_room"

            
        elif current_map == 'throne_room':
            

            player.restore_health_and_stamina()
            boss = enemy_file.Abyss_Walker("Abyss Walker")
            if not battle(player, boss):
                score_board111.save_score(player)
                print("You must replay the Throne Room.")
                current_map = 'throne_room'  
                
            else:
                break
        
    
    save_game(player, current_map)
    print(f"Congratulation! You have defeated Abyss Walker")
    score_board111.print_scoreboard()


if __name__ == "__main__":
    clear_screen.clear_screen()
    game_choice, username = lg.main()
 
    if game_choice == 'load':
        player, current_map = load_game(username)
        if not player:
            print("No saved game found. Starting a new game.")
            player = Character(username)
            current_map = 'courtyard'  
    else:
        player = Character(username) 
        current_map = 'courtyard'  
    
    intro.game_intro()  
    main_loop(player,current_map)



    
    """#courtyard
    map.courtyard(player)
    print("You have entered the Courtyard.")
    enemies_courtyard = enemy_file.generate_enemies(player.level)
    print(f"You are facing {len(enemies_courtyard)} enemies! Prepare for your battle.")
    for enemy in enemies_courtyard:
        battle(player,enemy)
    print("You have cleared the Courtyard!\n")
    current_map = map.courtyard(player)
    save_game(player, current_map)

    map.armory()
    enemies_armory = enemy_file.generate_enemies(player.level)
    print(f"You are facing {len(enemies_armory)} enemies! Prepare for your battle.")
    for enemy in enemies_armory:
        battle(player,enemy)
    print("You have cleared the Armory!\n")
    current_map = map.armory()
    save_game(player, current_map)


    map.treasury()
    gvocab.thaijai(player)
    current_map = map.treasury()
    save_game(player, current_map)

    map.library()
    maze.main(player)
    current_map = map.library()
    save_game(player, current_map)

    map.throne_room()
    boss = enemy_file.Abyss_Walker("Abyss Walker")
    battle(player,boss)
    current_map = map.treasury()
    save_game(player, current_map)"""