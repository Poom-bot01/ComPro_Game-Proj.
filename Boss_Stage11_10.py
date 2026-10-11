import os
import random
import time

# ---------- Starting Player and Boss Stats ----------
START_PLAYER_HP = 50
MAX_PLAYER_HP = 50
START_PLAYER_MANA = 30

START_BOSS_HP = 100

Boss_Art = r"""

⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⠿⠿⠶⣦⣀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⠶⢦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⠁⠀⠀⠀⠈⠹⣧⡀⠀⢠⣾⣿⠿⢿⣿⠁⠀⠀⠀⠈⢷⡄⠀⠀⠀
⠀⠀⠀⠀⣿⢸⡏⠀⢻⣦⡀⠀⠀⠀⠀⣿⣧⢠⡟⢽⡏⠀⠀⣿⣄⠀⠀⠀⠀⣸⣿⠀⠀⠀
⠀⠀⠀⢰⡏⠸⣧⣀⣸⡿⢷⣄⡀⣀⣰⣿⣿⢸⡇⠸⣷⣀⣀⣿⠿⢶⣄⣀⣤⣿⣿⠀⠀⠀
⠀⠀⣠⡶⢿⣄⠉⠻⢿⣦⣴⣿⣿⡿⠟⣱⠏⠘⣧⡀⠙⠻⢿⣿⣤⣴⣿⣿⠿⣫⣿⣄⠀⠀
⢀⣾⣯⣤⡀⠙⠳⢦⣤⣄⣀⣀⣤⡴⠞⠋⠀⠀⣈⠻⢦⣄⣀⣀⢈⣁⣀⣤⡶⠋⣠⣽⣧⠀
⣼⢃⡒⡘⢿⣆⠀⠀⠀⠈⠈⠁⠀⠀⠸⢿⣆⣠⡟⠃⠀⠈⠉⠉⠉⠉⠉⠁⢀⣾⠫⣐⢹⡇
⣿⡡⢌⠱⢚⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠧⡑⠬⢸⡧
⠸⣧⢊⠜⢲⡿⠀⠀⠀⠀⠀⢀⣠⡶⠾⠳⣶⣴⠶⠶⠶⣤⣄⠀⠀⠀⠀⠀⢻⡇⡜⣘⣾⠃
⠀⠙⠷⣮⡿⠃⢠⣄⣀⣀⣴⠟⠁⠀⢠⣟⠋⠛⣷⠀⠀⠀⠙⠻⢦⣤⣀⣀⡈⠻⣶⠟⠁⠀
⠀⠀⣴⠋⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⣰⡇⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠘⣧⠀⠀
⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⢀⣠⡿⠛⠋⠀⠀⠀⠈⠙⠛⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀
⢰⡏⠀⠀⠀⠘⠳⠶⠖⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠶⠶⠖⠀⠀⠀⠀⢿⡀
⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠉⠀⠀⠀⠉⠀⠐⠀⠀⠀⠀⠀⠀⠂⠀⠀⠠⠄⠤⠤⠄⠄⠤⠤⠀⠀⠀⠒⠀⠀⠂⠀⠈⠁

"""

Boss_Attack_Art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⡸⣞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣧⢿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣼⣞⡿⣞⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⣰⣟⢾⣽⢫⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⢤⣶⡻⣞⣿⣺⢯⣽⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⣀⣠⣤⣿⣽⣻⢾⣽⣷⣾⣽⣻⣞⣷⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣶⣄⡀⠀⠀⠀⣉⣲⣴⢶⣞⡿⣽⣞⡷⣯⢿⡽⣞⣿⠟⠋⠁⠉⠈⠳⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⢶⣾⣿⡽⣯⣟⡾⣽⡷⣯⣟⡽⡾⣽⡯⠁⠀⠀⠀⠀⠀⠀⢮⣭⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢞⣿⣿⢯⡿⣿⣯⣟⣷⣯⢿⣳⣟⡷⣽⣼⣻⣽⠀⠀⠀⠀⠀⠀⠀⢀⣼⡯⡗⠋⠤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣯⣽⣾⣿⣾⣗⡿⣯⡷⣯⣟⡷⣞⣼⣿⣀⠀⠀⠀⠀⢀⣠⡿⣏⡗⠈⠐⠈⠅⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠛⠏⠉⠉⠽⢟⢿⣿⣿⣿⣿⣷⣻⢾⡽⣞⡷⠄⡹⣶⢿⣻⢿⣻⡽⢯⣼⢦⠶⠁⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣯⠇⠀⠀⠀⠀⠀⠁⣽⣿⣿⣿⣷⣯⣿⣽⣛⡦⠀⠀⢩⣿⣹⢯⣷⢻⣟⠺⢣⡖⣘⠤⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡃⠁⠀⠀⠀⢀⣤⣾⣟⢿⣻⣿⣿⣟⡾⣽⡳⠄⠎⢳⣯⢯⣟⡾⢯⣞⣯⣓⠉⢀⠀⠀⡄⢢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣷⣶⣳⣶⣺⣿⣿⣳⢯⣟⣿⣿⣳⢯⠛⠅⠃⠀⠀⣴⣿⡿⣬⢶⠾⠙⣊⣥⠾⡒⠊⢁⢠⠣⣌⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡽⣾⡽⣯⣟⣿⡿⣯⣿⣿⣾⢿⣿⠳⢏⣈⢠⠀⠀⣰⢿⡿⣽⣉⡶⠌⠋⠉⣀⡀⠁⠀⠀⠀⣘⡐⣂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣽⣳⣟⣳⣟⣾⣽⣿⣿⣿⣿⣿⣦⣜⡻⡽⠆⠧⣴⡟⣯⢟⡳⣭⠲⠄⠐⠀⠀⠀⠈⠁⠉⠑⢊⡕⢃⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣾⣿⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⢧⠀⠹⠾⡵⡞⡽⢢⣃⠐⠀⠀⠄⡐⠀⠀⠀⡘⢦⠘⣌⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠒⡈⠀⡀⠄⡑⠢⣉⠴⣈⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣏⡴⣶⣵⣢⢤⢠⡀⡄⢠⠐⡰⢌⡱⠀⡁⡀⠆⡥⠆⡥⣛⡽⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠔⠉⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣻⢷⣯⡽⣞⣷⣻⡼⣡⢋⡔⠣⠜⡐⢐⠠⡓⣤⣙⣲⣽⣻⢷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣽⣞⣷⣻⡴⣣⢜⡱⣊⡕⣊⠠⡙⡰⣭⢷⣯⣿⢿

"""


PLAYER_FILE = "player_data.txt"


def load_player_data(path=PLAYER_FILE):
    """load player data from txt file (key=value per line)
    Example of player_data.txt:
        name=Player1
        score_total=0
        death_count=0
    """
    data = {"name": "Player1", "score_total": 0, "death_count": 0}
    if not os.path.exists(path):
        return data
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip()
            data[key] = int(value) if key in ("score_total", "death_count") else value
    return data


def save_player_data(player_data, path=PLAYER_FILE):
    """Write player data to txt file (one line per key=value)"""
    with open(path, "w", encoding="utf-8") as f:
        for key, value in player_data.items():
            f.write(f"{key}={value}\n")


def login_page():
    # ----- Login Page -----
    print("\n>>> Back to Login <<<")


def boss_stage(player_data):
    """player_data = {"name": ..., "score_total": ..., "death_count": ...}"""
    # ----- Start -----
    player_hp = START_PLAYER_HP
    player_mana = START_PLAYER_MANA
    boss_hp = START_BOSS_HP

    # Print Story / Boss_dialog

    print("\n*** Boss Stage ***")
    print(Boss_Art)
    print("Boss: What brings you here, mortal?")
    time.sleep(1)

    while True:
        # ----- Check Loss Conditions -----
        if player_hp <= 0:
            print("Player_Death...")
            defeat = True
        elif player_mana <= 0:
            print("You don't have any Mana left....")
            defeat = True
        else:
            defeat = False

        if defeat:
            print("Player_Defeat")
            player_data["death_count"] = player_data.get("death_count", 0) + 1
            save_player_data(player_data)
            login_page()
            return False

        # ----- Player Turn -----
        print("\n--- Player's Turn ---")
        print(f" Boss HP: {boss_hp}")
        print(f"\nHP: {player_hp} | Mana: {player_mana} ")
        print("[1] Attack (Mana 1)  [2] Heavy Attack (Mana 3)  [3] Heal (Mana 5)")

        while True:  # Loop until valid choice and sufficient mana
            choice = input("Choose Your Action: ").strip()
            if choice == "1" and player_mana >= 1:
                print("\n[Action] You chose: Attack Boss")
                boss_hp -= 3
                player_mana -= 1
                print(f"You used 1 Mana (Remaining: {player_mana})")
                print(f"[Result] Boss lost 3 HP (Remaining: {boss_hp})")
                time.sleep(1)
            elif choice == "2" and player_mana >= 3:
                print("\n[Action] You chose: Heavy Attack Boss")
                boss_hp -= 5
                player_mana -= 3
                print(f"You used 3 Mana (Remaining: {player_mana})")
                print(f"[Result] Boss lost 5 HP (Remaining: {boss_hp})")
                time.sleep(1)
            elif choice == "3" and player_mana >= 5:
                if player_hp >= MAX_PLAYER_HP:
                    print("You already full of Heal")
                    continue
                print("\n[Action] You chose: Heal")
                healed = min(5, MAX_PLAYER_HP - player_hp)
                player_hp += healed
                player_mana -= 5
                print(f"You used 5 Mana (Remaining: {player_mana})")
                print(f"[Result] You healed {healed} HP (Remaining: {player_hp})")
                time.sleep(1)
            elif choice in ("1", "2", "3"):
                print("You don't have enough mana Choose again")
                continue
            else:
                print("Invalid Choice Choose Again")
                continue
            break

        # ----- Check if Boss is Defeated -----
        if boss_hp <= 0:
            print("Player_Clear_Stage!!!")
            print("You have defeated the boss and cleared the stage!")
            player_data["score_total"] = player_data.get("score_total", 0) + 200
            save_player_data(player_data)
            time.sleep(1)
            login_page()
            return True

        # ----- Boss Turn (Boss_Tactical: Random) -----
        time.sleep(1)
        print("\n--- Boss's Turn ---")
        print(Boss_Art)
        time.sleep(0.5)
        
        print(Boss_Attack_Art)
        time.sleep(0.5)

        boss_action = random.choice(["attack", "heavy_attack", "heal"])

        if boss_action == "attack":
            print("[Action] Boss chose: Attack")
            player_hp -= 5
            print(f"[Result] You lost 5 HP (Remaining: {player_hp})")

        elif boss_action == "heavy_attack":
            print("[Action] Boss chose: Heavy Attack")
            player_hp -= 10
            print(f"[Result] You lost 10 HP (Remaining: {player_hp})")

        else:
            print("[Action] Boss chose: Heal")
            boss_hp += 20
            print(f"[Result] Boss healed 20 HP (Remaining: {boss_hp})")

        # Check if Boss HP exceeds starting HP

if __name__ == "__main__":
    data = load_player_data()
    boss_stage(data)