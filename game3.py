import msvcrt
import random
import sys
import time
# import os

total_levels = 3 # total lvls

level_time = {
    1: 10.0,
    2: 7.0,
    3: 5.0,
} # timer based on lvls

pools = {
    1: ["yoho", "god", "wallah", "ZOOS", "triplet", "doublet", "easymode", "superrevolution"],
    2: ["artemis", "fabledlegacy", "elephantintheroom", "iamconputerguy", "ambussingough", "triangledriod", "adrenalines", "typethisasfastasyoucanusuallyyoucantlol"],
    3: ["extraordinary", "responsibility", "claustrophobia", "misunderstanding",
        "uncomfortable", "revolutionary", "disproportionate", "mostunconventionalpickeverlikeifyougotthisinplaythroughthengg"],
} # word pools based on lvl (words are subject to change)

interval = 0.05 # how often countdown redraws

quit = object() # qutting game via ctrl c


def calculate_score_gain(time_remaining: float, time_limit: float, level: int) -> int:
# score calc here
    return 0


def calculate_score_loss(level: int) -> int:
# score calc here
    return 0


def pick_word(level: int) -> str: # pick random words from pools
    return random.choice(pools[level])


def get_time_limit(level: int) -> float: # return time limit for given lvls
    return level_time[level]


def flush_keyboard_buffer() -> None: # discard players who typed input too early
    while msvcrt.kbhit():
        msvcrt.getwch()


def wait_for_key(message: str) -> bool: # pauses the game untill player press any key
    print(message)
    ch = msvcrt.getwch()
    if ch == "\x03":
        return False
    return True


def draw_status_line(time_left: float, typed: str) -> None: # player status in game
    sys.stdout.write(f"\r\033[K  time left: {max(time_left, 0):4.1f}s  |  > {typed}")
    sys.stdout.flush()


def read_input_with_timer(time_limit: float): # read player typing character while showing live timer
    typed = ""
    flush_keyboard_buffer()
    start = time.monotonic()

    while True:
        time_left = time_limit - (time.monotonic() - start)
        if time_left <= 0:
            draw_status_line(0, typed)
            print()
            return None, 0.0

        draw_status_line(time_left, typed)

        if not msvcrt.kbhit():
            time.sleep(interval)
            continue

        ch = msvcrt.getwch()

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
    if not wait_for_key("press any key"):
        return None

    print(f"type this:  >>> {word} <<<\n") # display word

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


def show_result(success: bool, score: int, amount: int) -> None: # display current scores
    print(f"  {'+' if success else '-'}{amount} score")
    print(f"  current score: {score}")
    time.sleep(1.5)


def show_intro() -> bool: # intro (subject to change), returns false if ctrl+c
    print("=====")
    print("typer game")
    print("=====")
    print("welcome... to type game... type as fast as you can")
    return wait_for_key("press any key")


def start_next_stage(score: int) -> int: # called when player clear last lvl
    print("=" * 40)
    print("nice one. to the next stage")
    print("=" * 40)
    print(f"score: {score}\n")
    time.sleep(2)
    # next stage
    return score


def play_game(): # returns final score, or none if player quits
    score = 0
    level = 1

    if not show_intro():
        return None

    while level <= total_levels:
        result = play_level(level)
        if result is None:
            return None
        success, time_remaining, time_limit = result

        if success:
            amount = calculate_score_gain(time_remaining, time_limit, level)
            score += amount
        else:
            amount = calculate_score_loss(level)
            score -= amount

        show_result(success, score, amount)
        level = next_level_after(level, success)

    score = start_next_stage(score)
    return score


def main() -> None:
    score = play_game()
    if score is None:
        print("\n\ngame aborted. bye")
