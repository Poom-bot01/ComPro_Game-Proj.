import atexit
import os
import random
import select
import sys
import time

# Try importing display_stats, or use fallback if module is standalone
try:
    from character import display_stats
except ImportError:
    def display_stats(player):
        if hasattr(player, "display_stats"):
            player.display_stats()
        else:
            hp = get_stat(player, "current_hp", 30)
            mana = get_stat(player, "mana", 10)
            atk = get_stat(player, "attack_power", 15)
            gold = get_stat(player, "gold_balance", 500)
            print(f"| HP: [{hp:2d}/50] | MANA: [{mana:2d}/45] | ATK: [{atk:2d}/50] | GOLD: {gold:<5}$ |")

if os.name == "nt":
    import msvcrt

    def kbhit() -> bool:
        return msvcrt.kbhit()

    def getwch() -> str:
        return msvcrt.getwch()
else:
    import termios

    _fd = sys.stdin.fileno()
    _old = termios.tcgetattr(_fd)
    _new = termios.tcgetattr(_fd)
    _new[3] &= ~(termios.ICANON | termios.ECHO | termios.ISIG)
    termios.tcsetattr(_fd, termios.TCSADRAIN, _new)
    atexit.register(termios.tcsetattr, _fd, termios.TCSADRAIN, _old)

    def kbhit() -> bool:
        return bool(select.select([_fd], [], [], 0)[0])

    def getwch() -> str:
        first = os.read(_fd, 1)
        if first[0] >= 0xC0:
            need = 1 if first[0] < 0xE0 else 2 if first[0] < 0xF0 else 3
            first += os.read(_fd, need)
        ch = first.decode("utf-8", "ignore")
        return "\x08" if ch == "\x7f" else ch

TOTAL_LEVELS = 3
INTERVAL = 0.05
QUIT_SIGNAL = object()

LEVEL_TIME = {1: 20.0, 2: 15.0, 3: 13.0}
COIN_BASE = {1: 50, 2: 100, 3: 125}
ATK_BONUS = {1: 2, 2: 3, 3: 5}
PENALTY_HP = {1: 3, 2: 5, 3: 8}
FAST_RATIO = 0.5
FAST_BONUS_COINS = 25

POOLS = {
    1: ["yoho", "god", "wallah", "ZOOS", "triplet", "doublet", "easymode", "superrevolution"],
    2: ["artemis", "fabledlegacy", "elephantintheroom", "iamconputerguy", "ambussingough", "triangledriod", "adrenalines", "antigenesis"],
    3: ["extraordinary", "responsibility", "claustrophobia", "misunderstanding", "uncomfortable", "revolutionary", "disproportionate", "unfortunateson"],
}

FORGE_ART = r"""
⠀⠐⠈⠀⠀⠀⠄⠀⠀⠠⠀⠀⠀⠄⠀⠀⢀⣤⡀⠀⠄⠀⠀⠠⠀⠀⠀⠄⠀⠀⠠⠀⠀⠀⠄⠀⠀⠐
⠀⢀⠠⠀⠐⠀⠀⠀⠂⠀⠀⠐⠀⠀⠠⠀⠸⠟⠳⢤⣀⠀⠂⠀⠀⠐⠀⠀⠀⠂⠀⠀⠐⠀⠀⡀⠈⠀
⠀⠀⠀⠀⠄⠈⠀⢀⠀⠁⠀⠀⠂⠀⠀⢰⣾⡦⢰⡏⠀⣤⠀⠈⠀⢀⠈⠀⢀⠀⠁⠀⠠⠀⠀⠀⠐
⠀⠐⠈⠀⠀⠀⠀⠄⠀⠀⡀⠈⠀⠀⣀⣶⣞⣟⠻⠛⠀⠠⣿⠀⠀⠄⠀⠀⠠⠀⠀⠀⠂⠀⢀⠀⠁⠀
⠀⠀⢀⠀⠰⠀⠀⠀⢀⠀⠀⠀⡀⠀⣿⠉⣿⣿⡁⠀⠀⠀⠉⡇⠀⠀⠀⠆⠀⠀⠀⠁⠀⢀⠀⠀⠀⠈
⠀⠈⠀⠀⠀⡀⠀⠁⠀⠀⠠⠀⠀⠤⠯⣼⣟⣿⢷⠶⣶⣶⣶⣃⣀⡀⠂⠀⢀⠈⠀⠀⠄⠀⠀⡀⠈⠀
⠀⠠⠐⠀⠁⠀⠀⠄⠂⠀⢀⠀⠄⠠⣼⣿⣿⣿⣿⡏⠉⠩⣭⣭⡉⠁⠀⠀⠀⠀⠀⠂⠀⠀⠄⠀⠀⠐
⠀⠀⢀⠀⠠⠀⠂⠀⠀⠠⠀⠀⠀⢰⡟⠀⠀⠈⢶⡁⢀⣤⣾⣿⣧⠀⠀⠀⠁⠀⠂⠀⠐⠀⠀⠈⠀
⠀⠈⠀⠀⠀⢀⠀⠄⠂⠀⠀⠐⠀⠛⠀⠀⠀⠠⠘⠃⠘⠛⠛⠛⠛⠃⠀⠈⠀⠀⠄⠐⠀⠀⠄⠀⠀⠐
"""


def get_stat(player, attr, default=0):
    """Helper to access stats from object attributes or dictionary keys."""
    if isinstance(player, dict):
        return player.get(attr, default)
    return getattr(player, attr, default)


def set_stat(player, attr, value):
    """Helper to update stats on object attributes or dictionary keys."""
    if isinstance(player, dict):
        player[attr] = value
    else:
        setattr(player, attr, value)


def clear_screen():
    """Clears terminal screen across OS environments."""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_status_line(time_left: float, typed: str) -> None:
    """Draws live timer line."""
    sys.stdout.write(f"\r\033[K| TIME LEFT: {max(time_left, 0):4.1f}s | CHANT > {typed}")
    sys.stdout.flush()


def read_input_with_timer(time_limit: float):
    """Reads non-blocking input with timer."""
    typed = ""
    start = time.monotonic()

    while True:
        time_left = time_limit - (time.monotonic() - start)
        if time_left <= 0:
            draw_status_line(0, typed)
            print()
            return None, 0.0

        draw_status_line(time_left, typed)

        if not kbhit():
            time.sleep(INTERVAL)
            continue

        ch = getwch()

        if ch in ("\r", "\n"):
            time_left = max(time_limit - (time.monotonic() - start), 0.0)
            print()
            return typed, time_left
        elif ch == "\x08":
            typed = typed[:-1]
        elif ch == "\x03":
            print()
            return QUIT_SIGNAL, 0.0
        elif ch.isprintable():
            typed += ch


def calculate_coins(time_remaining: float, time_limit: float, level: int) -> int:
    coins = COIN_BASE[level]
    if time_remaining / time_limit >= FAST_RATIO:
        coins += FAST_BONUS_COINS
    return coins


def run_typing_challenge(player):
    """Executes Stage 4 Real-Time Incantation Forge minigame."""
    clear_screen()
    print(FORGE_ART)
    print("+====================================================================+")
    print("|                STAGE 4: REAL-TIME INCANTATION FORGE                |")
    print("+====================================================================+")

    display_stats(player)

    print("\n+--------------------------------------------------------------------+")
    print("| INSTRUCTIONS: Type the arcane runes as fast as possible!           |")
    print("| • Fast answers earn Gold bonuses and Attack Power gains.           |")
    print("| • Wrong entries or timeouts cause Backlash HP Damage.              |")
    print("+--------------------------------------------------------------------+")
    input("\n>>> PRESS [ENTER] TO BEGIN FORGE CHALLENGE...")

    level = 1
    total_earned_gold = 0

    while level <= TOTAL_LEVELS and get_stat(player, "current_hp") > 0:
        clear_screen()
        word = random.choice(POOLS[level])
        time_limit = LEVEL_TIME[level]

        hp = get_stat(player, "current_hp")
        mana = get_stat(player, "mana")
        atk = get_stat(player, "attack_power")
        gold = get_stat(player, "gold_balance")

        print("+====================================================================+")
        print(f"| INCANTATION TRIAL [{level}/{TOTAL_LEVELS}]                                      |")
        print("+====================================================================+")
        print(f"| HP: [{hp:2d}/50] | MANA: [{mana:2d}/45] | ATK: [{atk:2d}/50] | GOLD: {gold:<5}$ |")
        print("+--------------------------------------------------------------------+")
        print(f"| INCANTATION RUNE: >> {word} <<")
        print(f"| TIME LIMIT: {time_limit:.1f} SECONDS")
        print("+--------------------------------------------------------------------+")

        input("\n>>> PRESS [ENTER] WHEN READY...")
        print("\n+--------------------------------------------------------------------+")

        typed, time_remaining = read_input_with_timer(time_limit)

        if typed is QUIT_SIGNAL:
            print("\n[!] Incantation aborted.")
            return False

        print("+--------------------------------------------------------------------+")
        if typed is None:
            penalty = PENALTY_HP[level]
            new_hp = max(1, hp - penalty)
            set_stat(player, "current_hp", new_hp)
            print(f"| [!] TIME EXHAUSTED! Arcane backlash deals -{penalty} HP damage!       |")
            level = max(1, level - 1)
        elif typed.strip() != word:
            penalty = PENALTY_HP[level]
            new_hp = max(1, hp - penalty)
            set_stat(player, "current_hp", new_hp)
            print(f"| [!] MISCAST! Typed '{typed}', expected '{word}'. (-{penalty} HP)    |")
            level = max(1, level - 1)
        else:
            earned_coins = calculate_coins(time_remaining, time_limit, level)
            atk_boost = ATK_BONUS[level]

            set_stat(player, "gold_balance", gold + earned_coins)
            set_stat(player, "attack_power", min(50, atk + atk_boost))
            total_earned_gold += earned_coins

            print(f"| [*] PERFECT CAST! Solved in {time_limit - time_remaining:.2f}s!                     |")
            print(f"| REWARDS: +{earned_coins}$ Gold | +{atk_boost} ATK Power                       |")
            level += 1

        updated_hp = get_stat(player, "current_hp")
        updated_atk = get_stat(player, "attack_power")
        updated_gold = get_stat(player, "gold_balance")

        print(f"| UPDATED STATS -> HP: [{updated_hp}/50] | ATK: [{updated_atk}/50] | GOLD: {updated_gold}$ |")
        print("+--------------------------------------------------------------------+")
        time.sleep(2.5)

    clear_screen()
    final_atk = get_stat(player, "attack_power")
    print("+====================================================================+")
    print("|             STAGE 4 COMPLETED: FORGE TRIAL MASTERED                |")
    print("+====================================================================+")
    print(f"| TOTAL GOLD GAINED : +{total_earned_gold:<38}$ |")
    print(f"| FINAL ATTACK POWER: {final_atk:<39} |")
    print("+====================================================================+")
    time.sleep(2.5)
    clear_screen()
    return True
