import random
import sys
from pathlib import Path

# Game rules.
word_length = 5
max_attempts = 6
first_guess_reward = 9999
normal_win_reward = 300

# Player status placeholders; replace them when the team data is available.
player_name = "[PENDING]"
player_stage = "[PENDING]"
player_score = "[PENDING]"
player_health = "[PENDING]"
player_mana = "[PENDING]"
player_gold = "[PENDING]"
player_power = "[PENDING]"
player_attack = "[PENDING]"
player_xp = "[PENDING]"

# Use colors only when the game is running in a terminal.
use_colors = sys.stdout.isatty()


def colorize(text, marker):
    """Add green or yellow terminal color to a feedback marker."""
    if not use_colors:
        return text
    if marker == "G":
        return "\033[32m" + text + "\033[0m"
    if marker == "Y":
        return "\033[33m" + text + "\033[0m"
    return text


# Load possible answers from a text file beside this script.
answer_words_file = Path(__file__).with_name("answer_words.txt")
answer_words = []
with open(answer_words_file, "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip().lower()
        if word:
            answer_words.append(word)

if not answer_words:
    raise ValueError(f"No answer words found in {answer_words_file}.")
for word in answer_words:
    if len(word) != word_length or not word.isascii() or not word.isalpha():
        raise ValueError(
            f"Every word in {answer_words_file} must be a 5-letter English word."
        )


def score_guess(secret_word, guess):
    """Return G for a match, Y for a misplaced letter, and _ for no match."""
    feedback = ["_"] * word_length
    remaining_letters = list(secret_word)

    for index in range(word_length):
        if guess[index] == secret_word[index]:
            feedback[index] = "G"
            remaining_letters.remove(guess[index])

    for index in range(word_length):
        letter = guess[index]
        if feedback[index] != "G" and letter in remaining_letters:
            feedback[index] = "Y"
            remaining_letters.remove(letter)

    return feedback


def render_dashboard(guesses, message=""):
    """Print the player panel, guess grid, and letter-status keyboard."""
    print()
    print("=" * 82)
    print("ANCIENT WORDLE STAGE")
    print("=" * 82)
    print(
        f"PLAYER: {player_name} | STAGE: {player_stage} | "
        f"SCORE: {player_score}"
    )
    print(
        f"HEALTH: {player_health} | MANA: {player_mana} | GOLD: {player_gold}"
    )
    print(f"POWER: {player_power} | ATK: {player_attack} | XP: {player_xp}")
    print("-" * 82)
    print(" MONOLITH RUNE GRID")

    for attempt in range(max_attempts):
        if attempt < len(guesses):
            guess, feedback = guesses[attempt]
            guess_cells = ""
            result_cells = ""
            for index in range(word_length):
                letter = guess[index]
                marker = feedback[index]
                if not letter:
                    letter = " "
                if marker == "_":
                    shown_marker = "-"
                else:
                    shown_marker = marker
                guess_cells += f"[ {letter} ] "
                result_cells += colorize(f"[{shown_marker}]", marker) + " "
            print(f" ATTEMPT {attempt + 1}: {guess_cells}  ->  {result_cells}")
        else:
            blank_cells = ""
            for _ in range(word_length):
                blank_cells += "[   ] "
            print(f" ATTEMPT {attempt + 1}: {blank_cells}")

    print("-" * 82)
    print(
        " LEGEND: "
        f"{colorize('[G]', 'G')} Correct spot | "
        f"{colorize('[Y]', 'Y')} Wrong spot | [-] Not in word / invalid"
    )
    print(" DUPLICATES: Only as many copies as in the answer can be G/Y; extras are [-].")

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

    available_letters = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in tried_letters:
            available_letters.append(letter)

    revealed_letters = []
    absent_letters = []
    for letter in sorted(letter_statuses):
        marker = letter_statuses[letter]
        if marker == "G" or marker == "Y":
            shown_letter = f"[{letter.upper()}:{marker}]"
            revealed_letters.append(colorize(shown_letter, marker))
        elif marker == "_":
            absent_letters.append(letter)

    print(" RUNE KEYBOARD STATUS")
    print(f" AVAILABLE: {' '.join(available_letters) if available_letters else '-'}")
    print(f" FOUND:     {' '.join(revealed_letters) if revealed_letters else '-'}")
    print(f" DISCARDED: {' '.join(absent_letters) if absent_letters else '-'}")
    print("-" * 82)
    if message:
        print(f" {message}")


def play_game():
    """Run one terminal game from selecting an answer through win or loss."""
    secret_word = random.choice(answer_words)
    guesses = []

    for attempt in range(1, max_attempts + 1):
        render_dashboard(guesses)
        guess = input(f"\nAttempt {attempt}/{max_attempts}: ").strip().lower()
        if len(guess) != word_length or not guess.isascii() or not guess.isalpha():
            displayed_guess = []
            for letter in guess[:word_length].ljust(word_length):
                if letter.isascii() and letter.isalpha():
                    displayed_guess.append(letter)
                else:
                    displayed_guess.append("")
            guesses.append((displayed_guess, ["-"] * word_length))
            message = "Invalid format. This attempt has been used."
        else:
            feedback = score_guess(secret_word, guess)
            guesses.append((list(guess), feedback))
            if guess == secret_word:
                if attempt == 1:
                    reward = first_guess_reward
                else:
                    reward = normal_win_reward
                render_dashboard(
                    guesses,
                    f"GATE UNLOCKED! Solved in {attempt} guesses."
                    f"\n REWARD: +{reward:,} COINS (DISPLAY ONLY; NOT SAVED)",
                )
                return
            message = ""


        if attempt == max_attempts:
            render_dashboard(guesses, f"Attempts FAIL. The word was {secret_word}.")
        else:
            render_dashboard(guesses, message)


if __name__ == "__main__":
    play_game()
