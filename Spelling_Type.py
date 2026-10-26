import os
import random
import sys
import time
 
if os.name == "nt":
    import msvcrt
 
    def kbhit() -> bool:
        return msvcrt.kbhit()
 
    def getwch() -> str:
        return msvcrt.getwch()
else:
    import atexit
    import select
    import termios
 
    _fd = sys.stdin.fileno()
    _old = termios.tcgetattr(_fd)
    _new = termios.tcgetattr(_fd)
    _new[3] &= ~(termios.ICANON | termios.ECHO | termios.ISIG) # ctrl+c arrives as "\x03"
    termios.tcsetattr(_fd, termios.TCSADRAIN, _new)
    atexit.register(termios.tcsetattr, _fd, termios.TCSADRAIN, _old) # restore terminal on exit
 
    def kbhit() -> bool:
        return bool(select.select([_fd], [], [], 0)[0])
 
    def getwch() -> str:
        first = os.read(_fd, 1)
        if first[0] >= 0xC0: # multi-byte character, read the rest
            need = 1 if first[0] < 0xE0 else 2 if first[0] < 0xF0 else 3
            first += os.read(_fd, need)
        ch = first.decode("utf-8", "ignore")
        return "\x08" if ch == "\x7f" else ch

total_levels = 3 # total lvls

level_time = {
    1: 20.0,
    2: 15.0,
    3: 13.0,
} # timer based on lvls

pools = {
    1: ["yoho", "god", "wallah", "ZOOS", "triplet", "doublet", "easymode", "superrevolution"],
    2: ["artemis", "fabledlegacy", "elephantintheroom", "iamconputerguy", "ambussingough", "triangledriod", "adrenalines", "antigenesis"],
    3: ["extraordinary", "responsibility", "claustrophobia", "misunderstanding",
        "uncomfortable", "revolutionary", "disproportionate", "unfortunateson"],
} # word pools based on lvl (words are subject to change)

interval = 0.05 # how often countdown redraws

quit = object() # qutting game via ctrl c

score_base = {1: 100, 2: 200, 3: 300} # max points per lvl
min_fraction = 0.5 # correct answer at the last second still earns 50% of max
max_fraction = 0.9 # instant answer earns 90% of max
penalty = {1: 20, 2: 40, 3: 60} # points lost per lvl on wrong word or timeout

coin_base = {1: 50, 2: 100, 3: 125} # coins earned per correct answer per lvl
fast_ratio = 0.5 # finish with at least 50% of the time left to get the bonus
fast_bonus = 1 # extra coins for a fast answer


def calculate_score_gain(time_remaining: float, time_limit: float, level: int) -> int:
    time_ratio = time_remaining / time_limit
    multiplier = min_fraction + (max_fraction - min_fraction) * time_ratio
    return round(score_base[level] * multiplier)


def calculate_score_loss(level: int) -> int:
    return penalty[level]


def calculate_coins(time_remaining: float, time_limit: float, level: int) -> int: # coins for a correct answer
    coins = coin_base[level]
    if time_remaining / time_limit >= fast_ratio:
        coins += fast_bonus
    return coins


def pick_word(level: int) -> str: # pick random words from pools
    return random.choice(pools[level])


def get_time_limit(level: int) -> float: # return time limit for given lvls
    return level_time[level]


def wait_for_key(message: str) -> bool: # pauses the game untill player press any key
    print(message)
    ch = getwch()
    if ch == "\x03":
        return False
    return True


def draw_status_line(time_left: float, typed: str) -> None: # player status in game
    sys.stdout.write(f"\r\033[K  time left: {max(time_left, 0):4.1f}s  |  > {typed}")
    sys.stdout.flush()


def read_input_with_timer(time_limit: float): # read player typing character while showing live timer
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
            time.sleep(interval)
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
            return quit, 0.0
        elif ch.isprintable():
            typed += ch


def play_level(level: int): # during lvls, returns none if player quits
    word = pick_word(level)
    time_limit = get_time_limit(level)

    print(f"=== progress {level} / {total_levels} ===")
    print(f"time limit: {time_limit:.1f}s\n")
    if not wait_for_key("press any key if you ready"):
        return None

    print(f"type this:  >>> {word} <<<\n") # display word and tell player to type THERE

    typed, time_remaining = read_input_with_timer(time_limit)

    if typed is quit:
        return None
    if typed is None: # when player fail
        print("\n  times up")
        return False, 0.0, time_limit
    if typed.strip() != word:
        print(f"\n  wrong you typed '{typed}', expected '{word}'.")
        return False, time_remaining, time_limit

    print("correct")
    return True, time_remaining, time_limit


def next_level_after(level: int, success: bool) -> int: # to next lvl
    if success:
        return level + 1
    return max(1, level - 1)


def show_result(success: bool, score: int, amount: int, coins_earned: int, total_coins: int) -> None: # display current scores and coins
    print(f"  {'+' if success else '-'}{amount} score")
    if success:
        print(f"  +{coins_earned} coins")
    print(f"  current score: {score}")
    print(f"  total coins: {total_coins}")
    time.sleep(1.5)


def show_intro() -> bool: # intro (subject to change), returns False if ctrl+c
    print("=====")
    print("typer game")
    print("=====")
    print("welcome... to type game... type as fast as you can")
    return wait_for_key("press any key to start")


def start_next_stage(score: int, coins: int) -> int: # called when player clear last lvl
    print("=" * 40)
    print("nice one. to the next stage")
    print("=" * 40)
    print(f"score: {score}")
    print(f"coins earned: {coins}\n")
    time.sleep(2)
    # next stage
    return score


def play_game():
    score = 0
    coins = 0
    level = 1
    cleared = set()   # levels that already paid out

    if not show_intro():
        return None

    while level <= total_levels:
        result = play_level(level)
        if result is None:
            return None
        success, time_remaining, time_limit = result

        coins_earned = 0
        if success:
            if level in cleared:
                amount = 0   # replay: no reward
                print("  already cleared before, no reward")
            else:
                cleared.add(level)
                amount = calculate_score_gain(time_remaining, time_limit, level)
                score += amount
                coins_earned = calculate_coins(time_remaining, time_limit, level)
                coins += coins_earned
        else:
            amount = calculate_score_loss(level)
            score = max(0, score - amount)   # optional: don't go below 0

        show_result(success, score, amount, coins_earned, coins)
        level = next_level_after(level, success)


def main() -> None:
    score = play_game()
    if score is None:
        print("\n\ngame aborted. bye")


if __name__ == "__main__":
    main()