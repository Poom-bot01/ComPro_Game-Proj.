import os
from character import ArcaneMerchant

SAVE_FILE = "player_saves.txt"
LEADERBOARD_FILE = "leaderboard.txt"
USER_FILE = "users.txt"

def save_game(player):
    """Saves player data including death count into 'player_saves.txt'."""
    inventory_str = ",".join(player.inventory_list) if player.inventory_list else "NONE"
    
    player_data_line = (
        f"{player.name}|{player.current_hp}|{player.mana}|{player.attack_power}|"
        f"{player.gold_balance}|{inventory_str}|{player.cursed_status}|"
        f"{player.current_stage}|{player.high_score}|{player.latest_score}|{player.deaths}"
    )

    saves = {}
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "|" in line:
                    parts = line.split("|")
                    saves[parts[0]] = line

    saves[player.name] = player_data_line

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        for line in saves.values():
            f.write(line + "\n")

    # Sync death count with users.txt
    sync_users_txt(player.name, player.deaths)

    print("+----------------------------------------------------------+")
    print(f"| [SYSTEM] DATA SAVED TO MASTER FILE: {SAVE_FILE:<20} |")
    print("+----------------------------------------------------------+")

def sync_users_txt(username, death_count):
    """Updates the death count column inside users.txt."""
    if not os.path.exists(USER_FILE):
        return

    updated_lines = []
    with open(USER_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "," in line:
                parts = line.split(",")
                if parts[0].strip() == username:
                    pwd = parts[1].strip()
                    updated_lines.append(f"{username},{pwd},{death_count}")
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)

    with open(USER_FILE, "w", encoding="utf-8") as f:
        for line in updated_lines:
            f.write(line + "\n")

def load_game(username):
    """Loads player data from 'player_saves.txt' including deaths attribute."""
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue

            parts = line.split("|")
            if parts[0] == username:
                player = ArcaneMerchant(parts[0])
                player.current_hp = int(parts[1])
                player.mana = int(parts[2])
                player.attack_power = int(parts[3])
                player.gold_balance = int(parts[4])
                player.inventory_list = [] if parts[5] == "NONE" else parts[5].split(",")
                player.cursed_status = parts[6] == "True"
                player.current_stage = int(parts[7])
                player.high_score = int(parts[8])
                player.latest_score = int(parts[9])
                player.deaths = int(parts[10]) if len(parts) >= 11 else 0

                print("+----------------------------------------------------------+")
                print(f"| [SYSTEM] MASTER SAVE LOADED! STAGE [{player.current_stage}/6]              |")
                print("+----------------------------------------------------------+")
                return player

    return None

def update_leaderboard(username, new_score):
    """Updates leaderboard.txt keeping only the highest score per user."""
    scores = {}

    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    user, score_str = line.split(":", 1)
                    try:
                        scores[user] = int(score_str)
                    except ValueError:
                        continue

    if username in scores:
        scores[username] = max(scores[username], new_score)
    else:
        scores[username] = new_score

    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        for user, score in scores.items():
            f.write(f"{user}:{score}\n")

    print("+----------------------------------------------------------+")
    print(f"| [LEADERBOARD] UPDATED HIGH SCORE FOR {username:<19} |")
    print("+----------------------------------------------------------+")
