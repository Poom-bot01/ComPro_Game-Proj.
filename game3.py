import msvcrt
import os
import random
import sys
import time

os.system("")


TOTAL_LEVELS = 3 # total lvls

LEVEL_TIME_LIMITS = {
    1: 10.0,
    2: 7.0,
    3: 5.0,
} # timer based on lvls

WORD_POOLS = {
    1: ["apple", "house", "river", "cloud", "happy", "music", "green", "table"],
    2: ["keyboard", "mountain", "elephant", "computer", "umbrella", "triangle", "calendar", "universe"],
    3: ["extraordinary", "responsibility", "claustrophobia", "misunderstanding",
        "uncomfortable", "revolutionary", "disproportionate", "unconventional"],
} # word pools based on lvl (words are subject to change)

REFRESH_INTERVAL = 0.05 # how often countdown redraws



def calculate_score_gain(time_remaining: float, time_limit: float, level: int) -> int:
# score calc here
    return 0


def calculate_score_loss(level: int) -> int:
# score calc here
    return 0

def clear_screen() -> None: # clear screen in terminal
    os.system("cls")


def pick_word(level: int) -> str: # pick random words from pools
    return random.choice(WORD_POOLS[level])


def get_time_limit(level: int) -> float: # return time limit for given lvls
    return LEVEL_TIME_LIMITS[level]


def flush_keyboard_buffer() -> None: # discard players who typed input too early
    while msvcrt.kbhit():
        msvcrt.getwch()


def draw_status_line(time_left: float, typed: str) -> None: # player status
    sys.stdout.write(f"\r\033[K  Time left: {max(time_left, 0):4.1f}s  |  > {typed}")
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
            time.sleep(REFRESH_INTERVAL)
            continue

        ch = msvcrt.getwch()

        if ch in ("\r", "\n"):
            time_left = max(time_limit - (time.monotonic() - start), 0.0)
            print()
            return typed, time_left
        elif ch == "\x08":
            typed = typed[:-1]
        elif ch == "\x03":
            raise KeyboardInterrupt
        elif ch in ("\x00", "\xe0"):
            msvcrt.getwch()
        elif ch.isprintable():
            typed += ch


def play_level(level: int): # playing lvls
    word = pick_word(level)
    time_limit = get_time_limit(level)

    clear_screen()
    print(f"=== PROGRESS {level} / {TOTAL_LEVELS} ===")
    print(f"Time limit: {time_limit:.1f}s\n")
    input("Press Enter when you're ready...")

    print(f"\n  Type this word:  >>> {word} <<<\n") # display word

    typed, time_remaining = read_input_with_timer(time_limit)

    if typed is None: # when player fail
        print("\n  Time's up!")
        return False, 0.0, time_limit
    if typed.strip() != word:
        print(f"\n  Wrong! You typed '{typed}', expected '{word}'.")
        return False, time_remaining, time_limit

    print("\n  Correct!")
    return True, time_remaining, time_limit


def next_level_after(level: int, success: bool) -> int: # to next lvl
    if success:
        return level + 1
    return max(1, level - 1)


def show_result(success: bool, score: int, amount: int) -> None: # display current scores
    print(f"  {'+' if success else '-'}{amount} score")
    print(f"  Current score: {score}")
    time.sleep(1.5)


def show_intro() -> None: # intro (subject to change)
    clear_screen()
    print("=" * 40)
    print("        typer game")
    print("=" * 40)
    print(f"""
Rules:
  - There are {TOTAL_LEVELS} progress levels. Words get harder and the
    timer gets shorter as you progress.
  - Type the word shown, then press Enter before time runs out.
  - Correct + in time  -> you gain score.
  - Wrong or too slow  -> you lose score and go back one level.
  - Clear level {TOTAL_LEVELS} to move on to the next stage!
""")
    input("Press Enter to start...")


def start_next_stage(score: int) -> int: # called when player clear last lvl
    clear_screen()
    print("=" * 40)
    print("   LEVELS CLEARED! ENTERING NEXT STAGE...")
    print("=" * 40)
    print(f"\n  Score carried over: {score}\n")
    time.sleep(2)
    # next stage
    return score


def play_game() -> int:
    score = 0
    level = 1

    show_intro()

    while level <= TOTAL_LEVELS:
        success, time_remaining, time_limit = play_level(level)

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
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame aborted. Bye!")


#if __name__ == "__main__":
#    main()
