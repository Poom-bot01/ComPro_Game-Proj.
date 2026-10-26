import os          # lets us check whether a file exists
import random      # lets us pick random items

# input/output files
PLAYER_FILE = "Player Starting Information.txt"   # input file: Gold, HP, Mana, Attack
ITEM_FILE = "Item_list.txt"                       # input file: the 12 items
SHOWN_FILE = "Shown Items.txt"                    # output file: items already shown
APPRAISE_COST = 30                                # gold needed to appraise (same for every item)
ITEMS_PER_ROUND = 4                               # how many items are shown each round
STAT_NAMES = ["HP", "Mana", "Attack"]             # the stats an item can change
BOX_WIDTH = 38                                    # minimum inner width of the boxes


# file
def load_player_stats(filename=PLAYER_FILE):
    names = {"gold": "Gold", "hp": "HP", "mana": "Mana", "attack": "Attack"}  # file key -> dict key
    player = {}                                        # start with an empty dict
    with open(filename, "r", encoding="utf-8") as f:   # open the file for reading
        for line in f:                                 # go through it line by line
            line = line.strip()                        # remove spaces and the newline
            if ":" in line:                            # "Gold: 500" style
                key, value = line.split(":", 1)
            elif "=" in line:                          # "Gold = 500" style
                key, value = line.split("=", 1)
            else:                                      # blank or bad line -> skip
                continue
            key = key.strip().lower()                  # "Gold" -> "gold"
            if key in names:                           # only accept the 4 known keys
                player[names[key]] = int(value.strip())  # save the number
    return player                                      # e.g. {"Gold":500,"HP":30,...}


def load_items(filename=ITEM_FILE):
    items = []                                         # list that will hold every item
    with open(filename, "r", encoding="utf-8") as f:   # open the item file
        for line in f:                                 # one item per line
            line = line.strip()                        # clean the line
            if not line or line.startswith("#"):       # skip blank lines and the # header
                continue
            parts = line.split(",", 5)                 # Name,Price,HP,Mana,Attack,Clue (clue may contain commas)
            items.append({
                "name": parts[0].strip(),              # item name
                "price": int(parts[1]),                # gold price
                "HP": int(parts[2]),                   # HP change (can be negative)
                "Mana": int(parts[3]),                 # Mana change
                "Attack": int(parts[4]),               # Attack change
                "clue": parts[5].strip() if len(parts) > 5 else "",  # clue text shown after choosing
            })
    return items                                       # the full list of items


def get_shown_names(filename=SHOWN_FILE):
    shown = set()                                      # empty set
    if not os.path.exists(filename):                   # no file yet = nothing shown yet
        return shown
    with open(filename, "r", encoding="utf-8") as f:   # open the output file
        for line in f:                                 # lines look like "1|Healing Herb"
            line = line.strip()                        # clean the line
            if "|" in line:                            # ignore blank lines
                shown.add(line.split("|", 1)[1])       # keep only the name part
    return shown                                       # e.g. {"Healing Herb", ...}


def save_shown_items(round_number, items, filename=SHOWN_FILE):
    with open(filename, "a", encoding="utf-8") as f:   # "a" = append, keeps old rounds
        for item in items:                             # each shown item
            f.write(f"{round_number}|{item['name']}\n")  # write "round|name"


def reset_market(filename=SHOWN_FILE):
    if os.path.exists(filename):                       # only delete if it exists
        os.remove(filename)                            # remove the old record


# display
def print_box(lines, border="=", title=None):
    width = max([BOX_WIDTH] + [len(line) for line in lines])  # inner width
    print(border * (width + 4))                        # top border
    if title:                                          # optional centered title
        print(f"| {title.center(width)} |")
    for line in lines:                                 # each text line
        print(f"| {line.ljust(width)} |")
    print(border * (width + 4))                        # bottom border


def show_status(player):
    print()
    print_box([
        f"GOLD   : {player['Gold']} G",
        f"HP     : {player['HP']}",
        f"Mana   : {player['Mana']}",
        f"Attack : {player['Attack']}",
    ], "=", title="TRADING STAGE")


def show_items(items):
    width = max(len(item["name"]) for item in items)   # to line the prices up
    lines = [f"[{n}] {item['name'].ljust(width)} - {item['price']} G"
             for n, item in enumerate(items, start=1)]  # numbering starts at 1
    print()
    print_box(lines, "=", title="BAZAAR WARES")


def show_selected(item):
    clue = item["clue"] if item["clue"] else "(none)"  # no clue written in the file
    print()
    print_box([
        f"SELECTED: {item['name']}",
        f"CLUE: {clue}",
        "REVEALED STATS: ???",
    ], "*")


def format_effect(item):
    parts = [f"{item[s]:+} {s}" for s in STAT_NAMES if item[s] != 0]  # only changed stats
    return ", ".join(parts) if parts else "No effect"  # nothing changes -> "No effect"


# round
def pick_round_items(round_number):
    all_items = load_items()                           # all 12 items
    shown = get_shown_names()                          # names already shown
    available = [i for i in all_items if i["name"] not in shown]  # only the unseen ones
    count = min(ITEMS_PER_ROUND, len(available))       # safety: never ask for more than exist
    chosen = random.sample(available, count)           # random pick, no repeats
    save_shown_items(round_number, chosen)             # remember them in the output file
    return chosen                                      # list of item dicts


def ask_yes_no(question):
    while True:                                        # repeat until a valid answer
        answer = input(question).strip().lower()       # read and clean the answer
        if answer == "y":                              # yes
            return True
        if answer == "n":                              # no
            return False
        print("Please type Y or N.")                   # anything else -> ask again


def appraise_item(player, item):
    if player["Gold"] < APPRAISE_COST:                 # can the player afford it?
        print("Not enough gold for appraisal.")        # no -> tell the player
        print("Try something new or quit.")            # hint, as in the flowchart
        return False                                   # nothing happened
    player["Gold"] -= APPRAISE_COST                    # yes -> pay the fee
    print()
    print("APPRAISAL COMPLETE")                        # header
    print(f"EFFECT: {format_effect(item)}")            # e.g. "EFFECT: -30 HP, +15 Mana"
    print(f"Gold : {player['Gold']} G")                # gold left
    return True                                        # appraisal done


def buy_item(player, item, blind):
    if player["Gold"] < item["price"]:                 # can the player afford it?
        print("Not enough gold.")                      # no -> tell the player
        print("Try something new or quit.")            # hint, as in the flowchart
        return False                                   # nothing bought
    player["Gold"] -= item["price"]                    # yes -> pay the price
    for stat in STAT_NAMES:                            # HP, Mana, Attack in turn
        player[stat] = max(0, player[stat] + item[stat])  # add (or subtract); never below 0
    print()
    print("You bought the item blindly." if blind else "Item bought!")
    print(f"EFFECT: {format_effect(item)}")            # what the item did
    for stat in STAT_NAMES:                            # show the new value of changed stats
        if item[stat] != 0:
            print(f"Your {stat} is now {player[stat]}.")
    print(f"Gold : {player['Gold']} G")                # gold left
    return True                                        # purchase done


def choose_action(player, item):
    show_selected(item)                                # name, clue, stats hidden
    print()
    print(f"[B] Buy Blind ({item['price']}G)")         # option b
    print(f"[A] Appraise ({APPRAISE_COST}G)")          # option a

    while True:                                        # wrong action -> ask the action again
        action = input("ACTION > ").strip().lower()    # read the action

        if action == "a":                              # APPRAISE
            if not appraise_item(player, item):        # not enough gold for the fee
                return False                           # back to choosing an item
            if ask_yes_no("Buy item? (Y/N): "):        # Y -> check price and buy
                return buy_item(player, item, blind=False)  # False if too poor
            return False                               # N -> back to choosing an item

        if action == "b":                              # BUY BLIND
            return buy_item(player, item, blind=True)  # check price and buy (False if too poor)

        print("Invalid action. Type A or B.")          # anything else -> ask again


def check_game_over(player):
    if player["HP"] <= 0:                              # no HP left
        print()
        print_box(["Your HP reached 0."], "=", title="GAME OVER")
        return True
    return False


def play_market_round(player, round_number):
    items = pick_round_items(round_number)             # pick 4 random unseen items and save them
    if not items:                                      # every item was already shown
        print("\nThe market has nothing left to sell.")
        return player                                  # nothing to do, leave the market
    show_status(player)                                # Gold, HP, Mana, Attack
    show_items(items)                                  # Print Market (printed once)
    print()
    print(f"[1-{len(items)}] Select Item")             # instructions
    print("[Q] Quit")

    while True:                                        # input stage: repeat until buy or quit
        choice = input("COMMAND > ").strip().lower()   # read the command

        if choice == "q":                              # player wants to leave
            print()
            print("You left the Trading Stage.")
            return player                              # exit, nothing bought

        if not choice.isdigit() or not 1 <= int(choice) <= len(items):
            print()
            print("Invalid command.")                  # not 1-4 or Q
            print(f"Please choose 1-{len(items)} or Q.")
            continue                                   # back to the input stage

        item = items[int(choice) - 1]                  # the item the player picked
        if choose_action(player, item):                # True = bought something
            check_game_over(player)                    # show GAME OVER if HP is 0
            return player                              # one purchase per round -> leave the market
        # False = not enough gold, or said N -> back to the input stage


# main
def run_market_3(player):
    """Run round 3 (the last 4 items). Updates and returns the player dict."""
    return play_market_round(player, 3)                # picks from the items still unseen


# test
if __name__ == "__main__":                             # runs only when you run this file directly
    hero = load_player_stats()                         # read the starting stats
    run_market_3(hero)
    print("Player now:", hero)
