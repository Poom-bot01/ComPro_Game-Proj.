import random
import time

BOSS_ART_PHASE1 = r"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⡀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡏⠉⠙⡀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢧⠀⠀⢹⠀⠀⠱⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡌⡆⠀⠸⡄⡄⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠸⡠⣤⠱⣿⡀⠀⠀⠀⠀⠓⢤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠙⠺⢳⣸⡄⠀⠐⣄⠀⠀⢰⠋⠁⢀⡽⠦⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠎⠀⠀⢆⠀⠀⠀⢏⡇⠀⠀⠈⢦⠀⣙⠀⢰⠃⣤⢄⢠⡍⡷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡖⠉⠙⠦⡀⠀⠸⡄⠀⠀⠈⠇⠀⠀⠀⠀⠳⡌⠀⠸⣗⢿⠸⣾⣿⡿⡇⠀⠀⠀⠀
⠀⣀⣤⣒⡤⠴⠋⠀⢱⡄⠀⠹⡀⢠⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⢻⣆⠀⢉⠈⣁⠐⢄⠀⠀⠀
⢸⠿⢻⡷⠖⠶⢛⠇⡞⠠⠀⠀⠉⢼⡈⣇⠀⠀⢶⡀⠀⠀⠀⠀⠀⠈⢦⠀⠹⣦⣺⣆⡙⢗⠪⣧⡀⠀
⠀⠀⠘⠇⠀⠀⢳⡎⠁⠀⢃⣶⠀⢺⠀⠘⡆⠀⠸⣧⠀⠀⠀⠀⠘⣆⠀⠱⢄⠈⠻⣥⣭⣻⣇⠘⢧⡀
⠀⠀⠀⠀⠀⠀⠘⣧⢸⣇⡌⡿⡇⡏⠀⠀⠘⢦⡀⠳⣷⣄⠀⠀⠀⠙⣷⡀⠀⠹⣕⠒⠒⢝⢾⣀⡀⠁
⠀⠀⠀⠀⠀⠀⠀⠘⡇⡟⢿⡇⢹⣇⠀⠀⠀⠀⠙⢢⡈⢿⣧⠈⢇⠀⠈⢿⣶⣀⠈⢷⡀⠀⠉⠙⢷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠘⣌⣧⡆⠘⣆⠀⠀⠙⢯⡳⣄⠳⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣼⡜⡀⠈⢷⣤⡀⠀⠻⣌⠣⣹⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣳⠑⢤⣀⠉⠻⡶⣄⠘⢧⠘⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣀⠈⠙⠢⡘⣎⠳⣌⢷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢢⡀⣌⠻⡆⠘⢿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡹⡳⣿⠀⠀⠙⠻⠷⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠾⢷⣠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ⠙⡇⠀⠀⠀⠀

"""


BOSS_ART_PHASE2 = r"""
⠀⠀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⢴⣿⣿⠟⠒⠂⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀
⠀⢸⠋⠘⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣧⠀⠀⠀⠀⠀⢰⠒⢺⣿⣧⡀
⠀⣿⠀⠀⣇⠀⠀⠀⠀⠀⠀⢀⣿⠛⠍⠹⢻⣇⠀⠀⠀⠀⠀⠀⠈⠛⠛⠃
⠀⣿⡆⠀⢻⣿⣶⣦⣤⣤⣤⣼⣿⡄⠀⠀⣸⣿⣤⣤⣤⣀⠀⠀⠀⡇⠀⠀
⢀⣿⠇⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡿⣧⠰⡇
⢸⡇⢰⣼⡀⠋⢻⣸⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⢹⡟⣏⡇⠀⢠⣷
⠘⡗⢸⣿⣷⠀⠀⠞⡿⢹⣷⢻⣿⠀⠀⠀⠈⣻⢺⣿⣏⡄⠁⡇⠀⢀⣸⡇
⠀⠧⢸⡿⣿⠀⠀⠀⠁⡾⢻⠸⣿⡄⠀⠀⠀⡟⡾⡏⢹⠇⠀⢠⠇⢼⡟⠁
⠀⠀⠀⢷⢹⠀⠀⠀⠀⠁⣾⢺⣿⠇⠀⠀⢸⡍⡁⡇⣿⣲⠀⢸⠀⡏⠀⠀
⠀⠀⠀⢸⠆⠃⠀⠀⢸⣸⣽⡈⢿⣆⠀⠀⢰⡧⡿⢿⢹⡿⠐⠻⡴⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⠀⣿⠀⠀⠀⣷⣇⣸⠚⡇⠀⢸⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠘⡏⠀⠀⠀⣿⣯⣟⡆⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⠀⠱⠀⠀⠀⣼⣿⠟⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⡆⠀⠀⠀⢀⡟⢇⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢸⠀⠀⠀⣾⢁⡇⢸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⡟⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def render_hp_bar(current, max_hp=50, length=20):
    percent = max(0, min(1, current / max_hp))
    filled = int(length * percent)
    return "[" + "#" * filled + "-" * (length - filled) + "]"

def start_fight(player):
    """Stage 6: Two-Phase Boss Battle vs Demon Lord Malakor."""
    print(BOSS_ART_PHASE1)
    print("+====================================================================+")
    print("|          FINAL STAGE: DEMON LORD MALAKOR BATTLE                    |")
    print("+====================================================================+")

    boss_hp = 100
    boss_max_hp = 100
    boss_atk = 12

    # --- PHASE 1 COMBAT LOOP ---
    while player.current_hp > 0 and boss_hp > 0:
        print(f"\n| {player.name} HP: {render_hp_bar(player.current_hp, 50)} {player.current_hp}/50 | MANA: {player.mana}/45")
        print(f"| MALAKOR : {render_hp_bar(boss_hp, boss_max_hp)} {boss_hp}/{boss_max_hp}")
        print("+--------------------------------------------------------------------+")
        print("| 1. NORMAL ATTACK (FREE)                                            |")
        print("| 2. HEAVY ATTACK  (COSTS 15 MANA, 1.8X DAMAGE)                     |")
        print("| 3. HEAL          (COSTS 10 MANA, RESTORES +20 HP)                  |")
        print("+--------------------------------------------------------------------+")

        action = input(">>> CHOOSE ACTION (1-3): ").strip()

        if action == "1":
            damage = player.attack_power
            boss_hp -= damage
            print(f"| [>] YOU STRIKE MALAKOR FOR {damage} DAMAGE!")
        elif action == "2":
            if player.mana >= 15:
                player.mana -= 15
                damage = int(player.attack_power * 1.8)
                boss_hp -= damage
                print(f"| [*] HEAVY ATTACK DEALS {damage} DAMAGE!")
            else:
                print("| [!] INSUFFICIENT MANA! TURN SKIPPED.")
        elif action == "3":
            if player.mana >= 10:
                player.mana -= 10
                player.current_hp = min(50, player.current_hp + 20)
                print(f"| [+] HEALED +20 HP! CURRENT HP: {player.current_hp}/50")
            else:
                print("| [!] INSUFFICIENT MANA!")
        else:
            print("| [!] INVALID ACTION! TURN SKIPPED.")

        if boss_hp <= 0:
            print("\n+----------------------------------------------------------+")
            print("| [*] MALAKOR COLLAPSES!                 |")
            print("+----------------------------------------------------------+")
            break

        # Boss Turn (Phase 1)
        if boss_hp < 50 and random.random() < 0.35:
            heal_amount = random.randint(25, 40)
            boss_hp = min(boss_max_hp, boss_hp + heal_amount)
            print(f"| [!] DARK RECOVERY! MALAKOR HEALS +{heal_amount} HP! (HP: {boss_hp}/{boss_max_hp})")
        else:
            boss_damage = random.randint(boss_atk - 3, boss_atk + 4)
            if player.cursed_status:
                boss_damage += 3
            player.current_hp -= boss_damage
            print(f"| [-] MALAKOR RETALIATES FOR {boss_damage} DAMAGE!")

    if player.current_hp <= 0:
        return False

    # --- PHASE TRANSITION STORY INTRO ---
    time.sleep(1.5)
    print("\n+====================================================================+")
    print("|                  *** ABYSSAL RESURRECTION ***                      |")
    print("+====================================================================+")
    print("| As Malakor falls to one knee, dark smoke surges from the catacombs!|")
    print("| The Demon Lord's armor shatters and transforms into pure shadows...|")
    print("| Demon Lord Malakor awakens in his TRUE SHADOW FORM!                |")
    print("| WARNING: Malakor is now highly evasive! Attacks have a miss chance!|")
    print("+====================================================================+")
    input("\n>>> PRESS [ENTER] TO FACE PHASE 2...")

    # Phase 2 Stats
    print(BOSS_ART_PHASE2)
    print("+====================================================================+")
    print("|          FINAL STAGE: DEMON LORD MALAKOR BATTLE                    |")
    print("+====================================================================+")

    boss_hp = 200
    boss_max_hp = 200
    boss_atk = 16
    miss_chance = 0.35

    # --- PHASE 2 COMBAT LOOP ---
    while player.current_hp > 0 and boss_hp > 0:
        print(f"\n| {player.name} HP: {render_hp_bar(player.current_hp, 50)} {player.current_hp}/50 | MANA: {player.mana}/45")
        print(f"| MALAKOR : {render_hp_bar(boss_hp, boss_max_hp)} {boss_hp}/{boss_max_hp}")
        print("+--------------------------------------------------------------------+")
        print("| 1. NORMAL ATTACK (FREE)                                            |")
        print("| 2. HEAVY ATTACK  (COSTS 15 MANA, 1.8X DAMAGE)                      |")
        print("| 3. HEAL          (COSTS 10 MANA, RESTORES +20 HP)                  |")
        print("+--------------------------------------------------------------------+")

        action = input(">>> CHOOSE ACTION (1-3): ").strip()

        if action in ["1", "2"]:
            if random.random() < miss_chance:
                if action == "2":
                    if player.mana >= 15:
                        player.mana -= 15
                    else:
                        print("| [!] INSUFFICIENT MANA! TURN SKIPPED.")
                        continue
                print("| [!] ATTACK MISSED! Malakor shifted into shadows and dodged your blow!")
            else:
                if action == "1":
                    damage = player.attack_power
                    boss_hp -= damage
                    print(f"| [>] DIRECT HIT! YOU STRIKE MALAKOR FOR {damage} DAMAGE!")
                elif action == "2":
                    if player.mana >= 15:
                        player.mana -= 15
                        damage = int(player.attack_power * 1.8)
                        boss_hp -= damage
                        print(f"| [*] CRITICAL HIT! HEAVY ATTACK DEALS {damage} DAMAGE!")
                    else:
                        print("| [!] INSUFFICIENT MANA! TURN SKIPPED.")

        elif action == "3":
            if player.mana >= 10:
                player.mana -= 10
                player.current_hp = min(50, player.current_hp + 20)
                print(f"| [+] HEALED +20 HP! CURRENT HP: {player.current_hp}/50")
            else:
                print("| [!] INSUFFICIENT MANA!")
        else:
            print("| [!] INVALID ACTION! TURN SKIPPED.")

        if boss_hp <= 0:
            print("\n+----------------------------------------------------------+")
            print("| [*] FINAL VICTORY! DEMON LORD MALAKOR DESTROYED FOREVER! |")
            
            run_score = player.gold_balance + (player.current_hp * 10) + 200
            player.latest_score = run_score
            player.high_score = max(player.high_score, run_score)
            
            print(f"| LATEST RUN SCORE : {player.latest_score:<38} |")
            print(f"| ALL-TIME HIGH    : {player.high_score:<38} |")
            print("+----------------------------------------------------------+")
            return True

        # Boss Turn (Phase 2)
        if boss_hp < 100 and random.random() < 0.40:
            heal_amount = random.randint(30, 45)
            boss_hp = min(boss_max_hp, boss_hp + heal_amount)
            print(f"| [!] VOID RECOVERY! MALAKOR DRAINS SHADOWS AND HEALS +{heal_amount} HP!")
        else:
            boss_damage = random.randint(boss_atk - 3, boss_atk + 5)
            if player.cursed_status:
                boss_damage += 4
            player.current_hp -= boss_damage
            print(f"| [-] MALAKOR STRIKES FROM THE SHADOWS FOR {boss_damage} DAMAGE!")

    return False
