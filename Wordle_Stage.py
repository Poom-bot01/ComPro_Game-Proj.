import os
import random
import sys
import time
from pathlib import Path


# Game rules
word_length = 5
max_attempts = 6
first_guess_reward = 9999
normal_win_reward = 300


# Use terminal colors when supported
use_colors = sys.stdout.isatty()


def clear_screen():
    """Clears the terminal screen across Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colorize(text, marker):
    """Add green or yellow terminal color to a feedback marker."""
    if not use_colors:
        return text
    if marker == "G":
        return "\033[32m" + text + "\033[0m"
    if marker == "Y":
        return "\033[33m" + text + "\033[0m"
    return text

def load_rune_clues():
    """Load valid answer words and their clues from rune_clues.txt."""
    clues_file = Path(__file__).with_name("rune_clues.txt")
    clues = {}

    with open(clues_file, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            word, separator, clue = line.partition("|")
            word = word.strip().lower()
            clue = clue.strip()
            if not separator or not word or not clue:
                raise ValueError(
                    f"Invalid clue format in {clues_file.name} at line {line_number}; "
                    "expected word|clue."
                )
            if len(word) != word_length or not word.isascii() or not word.isalpha():
                raise ValueError(
                    f"Invalid answer word in {clues_file.name} at line {line_number}; "
                    f"expected a {word_length}-letter English word."
                )
            clues[word] = clue

    if not clues:
        raise ValueError(f"No answer words and clues found in {clues_file}.")

    return clues

def score_guess(secret_word, guess):
    """Return G for exact match, Y for misplaced letter, and _ for no match."""
    feedback = ["_"] * word_length
    remaining_letters = list(secret_word)

    # Pass 1: Exact matches (Green)
    for index in range(word_length):
        if guess[index] == secret_word[index]:
            feedback[index] = "G"
            remaining_letters.remove(guess[index])

    # Pass 2: Misplaced matches (Yellow)
    for index in range(word_length):
        letter = guess[index]
        if feedback[index] != "G" and letter in remaining_letters:
            feedback[index] = "Y"
            remaining_letters.remove(letter)

    return feedback

def render_dashboard(guesses, player, clue, message=""):
    """Print the live player panel, clue, guess grid, and ASCII letter-status keyboard."""
    clear_screen()
    print("+====================================================================+")
    print("|                      ANCIENT RUNE WORDLE GATE                      |")
    print("+====================================================================+")
    
    # Live Player Status Display (Mapped to 10-attribute schema)
    print(f"| PLAYER: {player.name:<12} | STAGE: [{player.current_stage}/6] | HIGH SCORE: {player.high_score:<8} |")
    print(f"| HEALTH: [{player.current_hp:2d}/50]       | MANA: [{player.mana:2d}/45]    | GOLD: {player.gold_balance:<6}$    |")
    print(f"| ATK POWER: [{player.attack_power:2d}/50]   | LATEST SCORE: {player.latest_score:<21} |")
    print("+--------------------------------------------------------------------+")
    print(f"| RUNE LORE CLUE: \"{clue}\"")
    print("+--------------------------------------------------------------------+")
    print("| MONOLITH RUNE GRID                                                 |")

    for attempt in range(max_attempts):
        if attempt < len(guesses):
            guess, feedback = guesses[attempt]
            guess_cells = ""
            for index in range(word_length):
                letter = guess[index] if guess[index] else " "
                marker = feedback[index]
                guess_cells += colorize(f"[ {letter.upper()} ]", marker) + " "
            print(f"|  ATTEMPT {attempt + 1}: {guess_cells}")
        else:
            blank_cells = "[   ] " * word_length
            print(f"|  ATTEMPT {attempt + 1}: {blank_cells}")

    print("+--------------------------------------------------------------------+")
    print(
        "| LEGEND: "
        f"{colorize('[G]', 'G')} Correct spot | "
        f"{colorize('[Y]', 'Y')} Wrong spot | [-] Not in word / invalid"
    )

    # Track letter status
    letter_statuses = {}
    tried_letters = []
    for guess, feedback in guesses:
        for index in range(word_length):
            letter = guess[index]
            marker = feedback[index]
            if not letter or marker == "-":
                continue
            if letter not in tried_letters:
                tried_letters.append(letter)

            if letter not in letter_statuses:
                letter_statuses[letter] = marker
            elif marker == "G":
                letter_statuses[letter] = marker
            elif marker == "Y" and letter_statuses[letter] != "G":
                letter_statuses[letter] = marker

    available_letters = [l for l in "abcdefghijklmnopqrstuvwxyz" if l not in tried_letters]
    revealed_letters = []
    absent_letters = []

    for letter in sorted(letter_statuses):
        marker = letter_statuses[letter]
        if marker in ["G", "Y"]:
            shown_letter = f"[{letter.upper()}:{marker}]"
            revealed_letters.append(colorize(shown_letter, marker))
        elif marker == "_":
            absent_letters.append(letter.upper())

    print("| RUNE KEYBOARD STATUS                                               |")
    print(f"| AVAILABLE: {' '.join([l.upper() for l in available_letters]) if available_letters else '-'}")
    print(f"| FOUND:     {' '.join(revealed_letters) if revealed_letters else '-'}")
    print(f"| DISCARDED: {' '.join(absent_letters) if absent_letters else '-'}")
    print("+--------------------------------------------------------------------+")
    if message:
        print(f"| {message}")

def run_wordle(player):
    """Executes Stage 2 Wordle using the player profile state."""
    rune_clues = load_rune_clues()
    secret_word = random.choice(list(rune_clues))
    clue = rune_clues[secret_word]
    
    guesses = []
    start_time = time.time()

    for attempt in range(1, max_attempts + 1):
        render_dashboard(guesses, player, clue)
        guess = input(f"\n>>> Attempt {attempt}/{max_attempts} - Enter 5-letter rune: ").strip().lower()

        # Handle invalid inputs
        if len(guess) != word_length or not guess.isascii() or not guess.isalpha():
            displayed_guess = [c if (c.isascii() and c.isalpha()) else "" for c in guess[:word_length].ljust(word_length)]
            guesses.append((displayed_guess, ["-"] * word_length))
            message = "[!] Invalid format! This attempt has been used."
        else:
            feedback = score_guess(secret_word, guess)
            guesses.append((list(guess), feedback))

            # WINNING CONDITION
            if guess == secret_word:
                elapsed = round(time.time() - start_time, 2)

                reward = first_guess_reward if attempt == 1 else normal_win_reward
                player.gold_balance += reward
                player.latest_score += 200
                player.high_score = max(player.high_score, player.latest_score)

                render_dashboard(
                    guesses,
                    player,
                    clue,
                    f"[*] GATE UNLOCKED! Solved in {attempt} guesses ({elapsed}s)."
                    f"\n | [+] REWARD: +{reward:,} Gold and +200 score!"
                )
                time.sleep(3.5)
                clear_screen()
                return True

            message = ""

        # FAILURE CONDITION
        if attempt == max_attempts:
            elapsed = round(time.time() - start_time, 2)
            player.current_hp = max(1, player.current_hp - 10)

            render_dashboard(
                guesses,
                player,
                clue,
                f"[!] ATTEMPTS EXHAUSTED! Secret rune was [{secret_word.upper()}]."
                f"\n | [-] Gate backlash deals 10 HP damage!"
            )
            time.sleep(3.5)
            clear_screen()
            return True
        else:
            if message:
                render_dashboard(guesses, player, clue, message)
