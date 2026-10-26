import os
import sys
import time
import random

# Import modularized components
from login import menu, show_title, login, sign_up, clear_screen
from intro import play_intro, show_stage_intro
from Wordle_Stage import run_wordle
from trading import run_shop
from typing import run_typing_challenge
from Boss_Stage import start_fight
from character import ArcaneMerchant
from save_system import save_game, load_game, update_leaderboard, LEADERBOARD_FILE


def start_game(player):
    """Executes Stages 1 to 6 sequentially with automatic saving at checkpoints."""
    play_intro()
    
    # Reset character state for a fresh run
    player.current_hp = 30
    player.mana = 10
    player.attack_power = 15
    player.gold_balance = 500
    player.inventory_list = []
    player.cursed_status = False
    player.latest_score = 0
    player.current_stage = 1

    # Stage 1: Catacomb Gates Bazaar (Shop Visit #1)
    player.current_stage = 1
    show_stage_intro(1)
    run_shop(player, visit_number=1)
    save_game(player)

    # Stage 2: Ancient Rune Gate (Wordle)
    player.current_stage = 2
    show_stage_intro(2)
    run_wordle(player)
    save_game(player)

    # Stage 3: Underworld Bazaar (Shop Visit #2)
    player.current_stage = 3
    show_stage_intro(3)
    run_shop(player, visit_number=2)
    save_game(player)

    # Stage 4: Arcane Forge Real-Time Typing Minigame
    player.current_stage = 4
    show_stage_intro(4)
    run_typing_challenge(player)
    save_game(player)

    # Stage 5: Abyssal Threshold Merchant (Shop Visit #3)
    player.current_stage = 5
    show_stage_intro(5)
    run_shop(player, visit_number=3)
    save_game(player)

    # Stage 6: Lair of Demon Lord Malakor (Final Boss)
    player.current_stage = 6
    show_stage_intro(6)
    victory = start_fight(player)

    # Update leaderboard & save state after boss conclusion
    if victory:
        update_leaderboard(player.name, player.high_score)
    save_game(player)

    if not victory:
        player.deaths += 1
        save_game(player)
        print("\n+====================================================================+")
        print("|                        *** YOU HAVE DIED ***                       |")
        print("| Your gold and relics crumble to dust in the dark catacombs...      |")
        print("+====================================================================+")
        time.sleep(2.0)
        input("\n>>> Press [ENTER] to return to hub...")
    else:
        print("\n+====================================================================+")
        print("|                  *** CONGRATULATIONS CHAMPION ***                  |")
        print("| Valen the Merchant saved the realm and amassed great fortune!      |")
        print("+====================================================================+")
        time.sleep(2.0)
        input("\n>>> Press [ENTER] to return to hub...")


def show_scoreboard():
    """Displays global high scores read directly from leaderboard.txt."""
    clear_screen()
    print("+====================================================================+")
    print("|                      HALL OF ARCANE MERCHANTS                      |")
    print("+====================================================================+")
    
    if not os.path.exists(LEADERBOARD_FILE):
        print("| No leaderboard records found yet! Complete a run to log scores.   |")
    else:
        scores = []
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    user, score_str = line.split(":", 1)
                    try:
                        scores.append((user, int(score_str)))
                    except ValueError:
                        continue
        
        if not scores:
            print("| No leaderboard records found yet! Complete a run to log scores.   |")
        else:
            scores.sort(key=lambda x: x[1], reverse=True)
            for rank, (user, score) in enumerate(scores, 1):
                print(f"| #{rank:<2} {user:<20} High Score: {score:<15} |")
                
    print("+====================================================================+")
    input("\n>>> Press [ENTER] to return to hub...")


def hub(name):
    """Main Game Hub menu for logged-in players with persistent save/load support."""
    player = load_game(name)
    if not player:
        player = ArcaneMerchant(name)
        save_game(player)

    while True:
        clear_screen()
        choice = menu(f"GAME HUB - {name.upper()}",
                      ["Start New Game Run", "View Player Card Stats", "Scoreboard", "Save Game", "Log Out"])

        if choice == "1":
            start_game(player)
        elif choice == "2":
            clear_screen()
            player.display_stats()
            input("\n>>> Press [ENTER] to return...")
        elif choice == "3":
            show_scoreboard()
        elif choice == "4":
            clear_screen()
            save_game(player)
            update_leaderboard(player.name, player.high_score)
            input("\n>>> Press [ENTER] to return...")
        elif choice == "5":
            clear_screen()
            save_game(player)
            update_leaderboard(player.name, player.high_score)
            print(f"\n[*] Progress saved. Logged out from {name}.")
            time.sleep(1.5)
            return
        else:
            print("[!] Invalid option. Please choose 1-5.")
            time.sleep(1.2)


def main():
    """Application Entry Point with automatic screen clearing and title display."""
    while True:
        clear_screen()
        show_title()
        choice = menu("MAIN MENU", ["Login", "Sign Up", "Exit Game"])
        
        if choice == "1":
            name = login()
            if name:
                print(f"\n[*] Authenticated! Entering game hub for {name}...")
                time.sleep(1.5)
                clear_screen()
                hub(name)
            else:
                time.sleep(1.2)
                
        elif choice == "2":
            new_user = sign_up()
            if new_user:
                print(f"\n[*] Account '{new_user}' created! Returning to Main Menu...")
                time.sleep(1.8)
            else:
                time.sleep(1.0)
                
        elif choice == "3":
            clear_screen()
            print("\n+====================================================================+")
            print("|            Thank you for playing The Spellbound Journey!           |")
            print("+====================================================================+")
            sys.exit(0)
            
        else:
            print("[!] Invalid option. Please choose 1-3.")
            time.sleep(1.2)


if __name__ == "__main__":
    main()
