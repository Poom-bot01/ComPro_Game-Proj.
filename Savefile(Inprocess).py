import ast
import csv
import os
from default_playerFunc import new_player as default_new_player


# Build paths from this file so the program works from any current directory.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Data")

User_data = os.path.join(DATA_DIR, "User_data.txt")
Player_records = os.path.join(DATA_DIR, "Player_records.txt")

# Kept as paths for game modules that may use separate record files later.
worldle_data = os.path.join(DATA_DIR, "Worldle_data.txt")
Typing_QTE_data = os.path.join(DATA_DIR, "Typing_QTE_data.txt")
Boss_fight_data = os.path.join(DATA_DIR, "Boss_fight_data.txt")

PLAYER_NUMBER_FIELDS = (
    "Maxhp", "hp", "gold", "ATK", " Max_Atk", "stage", "mana", " Max_ mana",
    "typing_rounds", "wpm_total", "chars_correct", "chars_total",
    "wordle_solves", "wordle_time_total",
)
PLAYER_LIST_FIELDS = ("items", "bosses_defeated")
PLAYER_RECORD_FIELDS = PLAYER_NUMBER_FIELDS + PLAYER_LIST_FIELDS


def saveUser_data(filename, data):
    """Save usernames and passwords in the existing name=password format."""
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    tmp = filename + ".tmp"
    with open(tmp, "w", encoding="utf-8") as file:
        for name, password in data.items():
            file.write(f"{name}={password}\n")
    os.replace(tmp, filename)


def loadUser_data(filename=User_data):
    """Load usernames and passwords from a name=password file."""
    data = {}
    if filename is None or not os.path.exists(filename):
        return data

    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "=" not in line:
                continue
            name, password = line.split("=", 1)
            data[name.strip()] = password.strip()
    return data


def new_player_record():
    """Start with the canonical player defaults, then add game-record fields."""
    player = default_new_player()
    player.update({
        "typing_rounds": 0,
        "wpm_total": 0,
        "chars_correct": 0,
        "chars_total": 0,
        "wordle_solves": 0,
        "wordle_time_total": 0,
        "bosses_defeated": [],
    })
    return player


def loadPlayer_records(filename=Player_records):
    """Load player state and game records from a tab-separated text file."""
    if filename is None or not os.path.exists(filename):
        return {}

    records = {}
    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            username = row.get("username")
            if not username:
                continue
            try:
                player = new_player_record()
                for field in PLAYER_NUMBER_FIELDS:
                    if row.get(field) not in (None, ""):
                        player[field] = int(row[field])
                for field in PLAYER_LIST_FIELDS:
                    if row.get(field) not in (None, ""):
                        raw_value = row[field]
                        if field == "bosses_defeated" and not raw_value.lstrip().startswith("["):
                            player[field] = [stage for stage in raw_value.split(";") if stage]
                            continue
                        value = ast.literal_eval(raw_value)
                        if isinstance(value, list):
                            player[field] = value
                records[username] = player
            except ValueError:
                # Ignore a malformed record row without losing other users' data.
                continue
            except (SyntaxError, TypeError):
                continue
    return records


def savePlayer_records(filename, records):
    """Atomically save player state and game records as tab-separated text."""
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    tmp = filename + ".tmp"
    fields = ["username", *PLAYER_RECORD_FIELDS]
    with open(tmp, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for username, player in records.items():
            row = {"username": username}
            for field in PLAYER_NUMBER_FIELDS:
                row[field] = player.get(field, 0)
            for field in PLAYER_LIST_FIELDS:
                row[field] = repr(player.get(field, []))
            writer.writerow(row)
    os.replace(tmp, filename)


def Typing_QTE_Record(player, wpm, correct, total):
    player.setdefault("typing_rounds", 0)
    player.setdefault("wpm_total", 0)
    player.setdefault("chars_correct", 0)
    player.setdefault("chars_total", 0)
    player["typing_rounds"] += 1
    player["wpm_total"] += wpm
    player["chars_correct"] += correct
    player["chars_total"] += total


def Worldle_Record(player, seconds):
    player.setdefault("wordle_solves", 0)
    player.setdefault("wordle_time_total", 0)
    player["wordle_solves"] += 1
    player["wordle_time_total"] += seconds


def Boss_fight_Record(player, stage):
    player.setdefault("bosses_defeated", [])
    if stage not in player["bosses_defeated"]:
        player["bosses_defeated"].append(stage)
