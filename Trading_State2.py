import os
import random
import time

ITEM_FILE = "Item_list.txt"
SHOWN_FILE = "Shown Items.txt"
APPRAISE_COST = 30
ITEMS_PER_ROUND = 4
BOX_WIDTH = 66

FALLBACK_ITEMS = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_items(filename=ITEM_FILE):
    if not os.path.exists(filename):
        return FALLBACK_ITEMS

    items = []
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",", 5)
            if len(parts) >= 5:
                hp_val = int(parts[2].strip())
                items.append({
                    "name": parts[0].strip(),
                    "price": int(parts[1].strip()),
                    "HP": hp_val,
                    "Mana": int(parts[3].strip()),
                    "Attack": int(parts[4].strip()),
                    "clue": parts[5].strip() if len(parts) > 5 else "(No clue provided)",
                    "cursed": hp_val < 0
                })
    return items if items else FALLBACK_ITEMS

def get_shown_names(filename=SHOWN_FILE):
    """Reads previously displayed item names from Shown Items.txt."""
    shown = set()
    if not os.path.exists(filename):
        return shown
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if "|" in line:
                shown.add(line.split("|", 1)[1])
    return shown

def save_shown_items(round_number, items, filename=SHOWN_FILE):
    with open(filename, "a", encoding="utf-8") as fout:
        for item in items:
            fout.write(f"{round_number}|{item['name']}\n")

def reset_market(filename=SHOWN_FILE):
    if os.path.exists(filename):
        os.remove(filename)

def print_box(lines, border="=", title=None):
    width = max([BOX_WIDTH] + [len(line) for line in lines])
    print(border * (width + 4))
    if title:
        print(f"| {title.center(width)} |")
        print(border * (width + 4))
    for line in lines:
        print(f"| {line.ljust(width)} |")
    print(border * (width + 4))

def format_effect(item):
    parts = []
    if item["HP"] != 0: parts.append(f"{item['HP']:+} HP")
    if item["Mana"] != 0: parts.append(f"{item['Mana']:+} Mana")
    if item["Attack"] != 0: parts.append(f"{item['Attack']:+} ATK")
    return ", ".join(parts) if parts else "No stat changes"

def run_shop(player, visit_number):
    if visit_number == 1:
        reset_market()

    all_items = load_items()
    shown = get_shown_names()

    available = [
        i for i in all_items 
        if i["name"] not in shown and i["name"] not in player.inventory_list
    ]

    if not available:
        available = [i for i in all_items if i["name"] not in player.inventory_list]

    if not available:
        print("+----------------------------------------------------------+")
        print("| [!] THE BAZAAR HAS NO NEW ITEMS LEFT TO OFFER!           |")
        print("+----------------------------------------------------------+")
        time.sleep(1.5)
        return

    count = min(ITEMS_PER_ROUND, len(available))
    wares = random.sample(available, count)
    save_shown_items(visit_number, wares)

    while True:
        clear_screen()
        print("+====================================================================+")
        print(f"|                      TRADING BAZAAR                               |") 
        print("+====================================================================+")

        player.display_stats()

        item_lines = [
            f"[{n}] {item['name'].ljust(24)} - {item['price']:>3}$ | {item['clue']:<27}"
            for n, item in enumerate(wares, start=1)
        ]
        print_box(item_lines, "=", title="BAZAAR WARES")
        print("| [ Q ] SKIP SHOP & PROCEED TO NEXT STAGE                            |")
        print("+--------------------------------------------------------------------+")

        choice = input("\n>>> COMMAND (1-4 / Q) > ").strip().lower()

        if choice == "q":
            print("+----------------------------------------------------------+")
            print("| [>] SKIPPING SHOP... ADVANCING TO NEXT STAGE             |")
            print("+----------------------------------------------------------+")
            time.sleep(1.5)
            clear_screen()
            return

        if choice.isdigit() and 1 <= int(choice) <= len(wares):
            item = wares[int(choice) - 1]

            clear_screen()
            print_box([
                f"ITEM     : {item['name']}",
                f"PRICE    : {item['price']}$",
                f"LORE CLUE: {item['clue']}",
                "STATS    : ???"
            ], "*", title="SELECTED ITEM")

            print("\n+----------------------------------------------------------+")
            print("| [B] BUY NOW (BLIND PURCHASE)                              |")
            print(f"| [A] APPRAISE ({APPRAISE_COST}$ FEE TO REVEAL EXACT STATS)        |")
            print("| [C] CANCEL / GO BACK                                      |")
            print("+----------------------------------------------------------+")

            sub_choice = input(">>> ACTION (B/A/C) > ").strip().lower()

            if sub_choice == "a":
                if player.gold_balance < APPRAISE_COST:
                    print("| [!] INSUFFICIENT GOLD FOR APPRAISAL.")
                    time.sleep(1.5)
                    continue
                else:
                    player.gold_balance -= APPRAISE_COST
                    print("+----------------------------------------------------------+")
                    print("| APPRAISAL RESULT:                                        |")
                    print(f"| • EFFECT: {format_effect(item):<46} |")
                    print(f"| • GOLD REMAINING: {player.gold_balance:<38}$ |")
                    print("+----------------------------------------------------------+")
                    
                    confirm = input("\n>>> BUY ITEM NOW? (Y/N) > ").strip().lower()
                    if confirm != "y":
                        print("+----------------------------------------------------------+")
                        print("| [>] PURCHASE CANCELED. RETURNING TO BAZAAR...            |")
                        print("+----------------------------------------------------------+")
                        time.sleep(1.2)
                        continue

            elif sub_choice == "c":
                print("+----------------------------------------------------------+")
                print("| [>] RETURNING TO BAZAAR...                               |")
                print("+----------------------------------------------------------+")
                time.sleep(1.0)
                continue

            elif sub_choice == "b":
                confirm = input("\n>>> CONFIRM BLIND PURCHASE? (Y/N) > ").strip().lower()
                if confirm != "y":
                    print("+----------------------------------------------------------+")
                    print("| [>] PURCHASE DECLINED. RETURNING TO BAZAAR...            |")
                    print("+----------------------------------------------------------+")
                    time.sleep(1.2)
                    continue

            # Complete Purchase
            if player.gold_balance >= item["price"]:
                player.gold_balance -= item["price"]
                
                # Apply Caps: HP <= 50, Mana <= 45, Attack <= 50
                player.current_hp = min(50, max(1, player.current_hp + item["HP"]))
                player.mana = min(45, max(0, player.mana + item["Mana"]))
                player.attack_power = min(50, max(0, player.attack_power + item["Attack"]))
                player.inventory_list.append(item["name"])

                if item["cursed"] or item["HP"] < 0:
                    player.cursed_status = True

                clear_screen()
                print("+----------------------------------------------------------+")
                print(f"| [+] PURCHASE SUCCESSFUL: {item['name']:<31} |")
                print("+----------------------------------------------------------+")
                print(f"| EFFECT: {format_effect(item):<48} |")
                print(f"| HP [{player.current_hp:2d}/50] | MANA [{player.mana:2d}/45] | ATK [{player.attack_power:2d}/50] | GOLD: {player.gold_balance:<4}$ |")
                
                if player.cursed_status:
                    print("| [!] WARNING: RELIC IS CURSED! DARK ENVELOPMENT...        |")
                print("+----------------------------------------------------------+")

                time.sleep(3.0)
                clear_screen()
                return
            else:
                print("| [!] INSUFFICIENT GOLD TO PURCHASE ITEM.")
                time.sleep(1.5)

                