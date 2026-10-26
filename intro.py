import os
import time

ECLIPSE_ART = r"""
            *   .   *   .  *  .  *  .   *   .   *                 
          .   .     .                 
       .    .           .                    .   *
     .                  .      .   *
⡇⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.   *
⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣀⣤⣤⣤⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀.   *⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⢀⣤⣾⣿⣿⣿⡟⣿⠯⠹⢉⣉⠉⠃⠀⠀⠀⠀⠀⠀.   * . .      .⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⢨⡝⢀⣴⣿⣿⣿⣿⡟⠙⢃⠏⡠⠚⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠄⠀⠀⠀⠀⠀⠀⠦⠠⢁⢡⣟⣿⣿⣿⡿⠫⠥⢐⠆⠈⠁⠬⠅⠤⢀⠀⠀⠀⠀⠀⠘⣤⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⠀⠓⣲⣿⣿⣿⣿⡋⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠀⠀⠀⠀⢀⠀⠂⢠⣿⣿⣿⣿⣿⡇⠀⠀⠉⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢰⣹⣷⡀⠀⠀⠀⠐⠀⠀⠀
⠀⡀⠀⠀⢀⠀⢀⡶⣈⣿⣿⣿⣿⣿⡈⠹⠀⠀⢀⡸⢱⠀⠀⠀⡈⠇⠀⠀⠀⠀⠀⠀⠀⠈⣾⣿⡇⠀⠀⠀⠀⠀⠀⢀
⠀⠀⠀⠠⠀⠀⠨⢤⣠⣿⣿⣿⣿⣿⡉⣏⠉⡀⠀⠙⡃⠠⡀⠃⠆⠸⠤⠄⠀⠀⡀⠀⢠⡐⣿⣿⡇⠀⠀⠀⠁⠀⠀⠀
⠀⠁⠀⠀⠀⠀⠀⠤⠨⢻⣿⣿⣹⣿⣷⣻⢍⠓⠀⠀⠁⣤⡴⢤⢖⡊⢤⡍⠀⠀⠀⠰⠌⢰⣻⣿⠃⠀⠀⠠⠀⠀⠀⠈
⠀⠂⠀⠈⠀⢀⠀⢘⠋⢛⣿⣯⣾⣿⣿⣷⢿⡿⠄⠂⢠⡭⠒⡇⡞⢘⢒⡂⠀⠀⢠⡰⣰⣿⣿⡟⠂⠀⢀⠀⠀⠄⠀⠈
⠠⠀⠂⠁⠀⠀⠀⠈⣠⣼⡛⣿⣿⣿⣿⣿⡿⢿⣯⡀⠐⢻⢘⣹⠠⠆⣤⣤⣤⣣⣿⣵⣿⣿⣿⠁⠀⠀⠀⠀⠠⠀⠀⢈
⠀⡀⠀⠠⠀⠁⠀⠀⠁⣡⣘⣿⢿⣿⣿⣿⣿⣿⣿⡶⠄⡼⣿⣭⣴⣛⣳⣧⣿⣿⣿⣿⣿⡿⡍⠀⠀⠀⠈⠀⢀⠀⠀⠠
⠀⢀⠀⠄⠀⢀⠈⠀⠀⠥⠩⢑⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠈⠀⢀⠀⠀⠀⠐
⠀⡀⠀⠀⠠⠀⠀⠠⠀⠀⠀⠫⠢⠏⣹⢉⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⠀⠀⠀⠀⠐⠀⠈⠀⠀⠠⠀⢈
⠀⡀⠀⠂⠀⠀⠐⠀⠀⡀⠀⠀⠠⠉⣽⠀⠐⣿⠙⣿⢽⣿⣿⣻⣿⣿⣿⣿⠟⠀⢿⣿⠀⠀⢀⠈⠀⠀⠄⠐⠀⠀⠀⠠
⠀⡀⠀⠄⠀⠁⠀⠠⠀⠀⠀⠄⠀⠀⠛⠀⠀⣿⠀⠈⠀⢸⣿⢿⣿⣟⣿⣽⠀⠀⢸⡯⠀⠀⠀⠀⠀⠂⠀⢀⠀⠈⠀⠐
⠀⡀⠀⢀⠀⠂⠀⡀⠠⠐⠀⠀⠠⠀⠀⠀⢠⡟⠀⠁⠀⢸⣿⢸⣿⣯⣿⠉⠀⠀⢸⡔⠀⠀⠈⠀⠠⠀⢀⠀⠀⠠⠀⢈
⠀⡀⠄⠀⠀⡀⠄⠀⠀⠀⡀⠐⠀⠀⠐⠀⢸⡇⠀⠀⠀⠸⣿⢸⣿⢣⡟⠀⠀⠀⠘⠀⠀⠀⠂⠀⢀⠀⠀⠀⠠⠀⠀⠄
⠀⢀⠀⠀⠄⠀⠀⠀⡀⠁⠀⠀⠀⠂⠀⠀⠸⠇⠀⠀⠀⠀⣇⠘⣿⠈⠃⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠁⠀⠀⠀⢈
⠀⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠄⠂⠀⠀⠄⠀⠀⠀⠀⠀⠀⡏⢈⣿⠀⠘⠀⠀⠀⠠⠀⠀⢀⠀⠀⡀⠄⠂⠀⠀⠈⠀⢀
⠀⠀⠀⠐⠈⠀⠀⠀⠀⠐⠀⠀⠀⠀⡀⠀⠀⡀⠠⠐⠀⠀⡂⢈⣿⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀
⠀⠈⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢀⠀⠀⠀⠠⠀⠁⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠈⠀⠀⠀⠁⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠂⠀⠀⠠⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⠀⠀⠀⡀⠐⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

MERCHANT_ART = r"""
        ⠀⠀⠀⠀⠀⠀⡠⢄⠶⢖⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣮⣬⡁⠐⠀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢰⣿⣿⣷⣦⡄⠈⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢸⣿⣿⡿⢛⡲⢝⢻⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⣰⣽⡾⣻⠛⠓⠊⠈⢭⣲⠄⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢲⣍⣞⣿⠟⢜⡢⣄⠀⠒⢞⡄⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⣮⠞⡱⠃⢫⣎⢊⠐⠂⠢⠤⠘⡄⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢠⠇⣼⣇⢀⢡⣹⢷⡡⡀⠉⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⣮⣾⣯⢿⣌⣾⣴⣾⣿⣦⡀⠀⠀⠀⠈⠓⡀⠀⠀⠀⠀
        ⠀⢰⢿⣾⣿⢿⢈⠍⢻⣧⣟⢾⣧⡁⠀⠐⠄⢉⠘⡢⣀⠀⠀
        ⠀⣶⣯⣾⢨⣧⡣⡄⠸⡽⣟⣟⢿⢷⣄⡀⣌⠠⠈⠢⣇⠀⠀
        ⢰⣿⣇⢸⣸⠉⢳⣄⡀⠈⠢⠀⠀⠪⣇⠙⢣⠑⠲⣄⠈⢢⡀
        ⠈⠃⠀⠛⣇⣧⢤⣿⢻⢄⡠⡈⠐⠦⣈⢦⡀⣧⠈⠋⠢⠏⠉
        ⠀⠈⠁⠀⢻⡝⢆⢾⣾⣷⣿⡀⠀⢀⡨⣵⢇⠀⠀⠠⠤⠀⠀
        ⠀⠀⠀⠀⠀⠉⠸⡚⣿⣿⣟⢽⣞⢉⠇⠉⠒⠓⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠐⣖⠣⢧⢠⠿⠿⢤⠈⠁⠀⠀⢀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⡝⢁⡊⠈⣤⠠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢀⢀⠤⠶⠦⠅⠤⠻⠥⠤⣷⡷⡇⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀
        ⠀⠀⠉⠁⠀⠀⠀⠒⠀⠈⠓⠒⠛⠠⠶⠔⡖⠲⠶⠺⢒⣶⠄
"""


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def play_intro():
    """Displays story background and objective screens."""
    clear_screen()
    print(ECLIPSE_ART)
    slow_print("\n+----------------------------------------------------------+")
    slow_print("| PROLOGUE: THE FALL OF HEROES                             |")
    slow_print("+----------------------------------------------------------+")
    slow_print("When the Eclipse of the Seven Seals shattered the catacombs,")
    slow_print("prophecy spoke of holy paladins and archmages rising to defend mankind.")
    slow_print("None came.")
    slow_print("The grand army was obliterated before reaching the abyss.\n")
    
    input(">>> Press [ENTER] to continue...")

    clear_screen()
    print(MERCHANT_ART)
    slow_print("\n+----------------------------------------------------------+")
    slow_print("| THE UNLIKELY HERO                                        |")
    slow_print("+----------------------------------------------------------+")
    slow_print("Left in the wake of chaos is Valen, an opportunistic traveling peddler")
    slow_print("stranded at the dungeon gates.")
    slow_print("Equipped with nothing but 500 Gold, a wagon of dubious wares,")
    slow_print("a sharp eye for cursed relics, and lightning-fast reflexes...")
    slow_print("If no hero will save the world, a merchant will have to buy,")
    slow_print("decipher, type, and bargain his way to salvation.\n")

    input(">>> Press [ENTER] to begin journey...")


def show_stage_intro(stage_number):
    """Displays ASCII dialogues and lore before starting each specific stage."""
    clear_screen()
    print("+====================================================================+")
    
    if stage_number == 1:
        print("|                   STAGE 1: CATACOMB GATES BAZAAR                   |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Scavenger Merchant: \"Ah, another brave soul or a foolish one?     |")
        print("| The catacombs ahead are sealed by dark magic. Take a look at my    |")
        print("| wares... but choose wisely. You may only purchase ONE item!\"       |")
        print("+====================================================================+")
        print("| OBJECTIVE: Purchase 1 relic or skip to preserve your 500 Gold.     |")

    elif stage_number == 2:
        print("|                   STAGE 2: ANCIENT RUNE GATE                       |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Monolith Spirit: \"Halt, traveler! None pass without speaking the    |")
        print("| ancient 5-letter password. Deduce the rune word in 6 attempts...   |")
        print("| or suffer magical backlash!\"                                       |")
        print("+====================================================================+")
        print("| OBJECTIVE: Guess the 5-letter rune word using positional feedback. |")

    elif stage_number == 3:
        print("|                   STAGE 3: UNDERWORLD BAZAAR                       |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Black-Market Trader: \"You survived the Rune Gate? Impressive.      |")
        print("| Deep in the catacombs, my prices are higher, but my relics hold    |")
        print("| raw abyssal power. Pick one relic before going deeper.\"             |")
        print("+====================================================================+")
        print("| OBJECTIVE: Upgrade your stats with an underworld artifact.         |")

    elif stage_number == 4:
        print("|                   STAGE 4: THE ARCANE FORGE                        |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Forge Keeper: \"The furnace glows! Recite the ancient incantation  |")
        print("| with speed and accuracy. Perfect chanting will imbue your weapon   |")
        print("| with massive bonus Attack Power!\"                                  |")
        print("+====================================================================+")
        print("| OBJECTIVE: Type the spell accurately before the countdown expires. |")

    elif stage_number == 5:
        print("|                   STAGE 5: ABYSSAL THRESHOLD MERCHANT              |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Dying Paladin: \"Beyond this door lies Demon Lord Malakor...       |")
        print("| I can go no further. Take my remaining relics and prepare your     |")
        print("| health and mana. This is your final chance to buy gear!\"          |")
        print("+====================================================================+")
        print("| OBJECTIVE: Final shop visit to maximize stats before the Boss.     |")

    elif stage_number == 6:
        print("|                   STAGE 6: LAIR OF DEMON LORD MALAKOR              |")
        print("+====================================================================+")
        print("| DIALOGUE:                                                          |")
        print("| Demon Lord Malakor: \"A mere peddler stands before me? Your armor   |")
        print("| is stolen, your spells are bought, yet you dare challenge me?      |")
        print("| Come, merchant... let us see if your coin can buy your life!\"      |")
        print("+====================================================================+")
        print("| OBJECTIVE: Defeat Malakor using Normal Attack, Heavy Attack & Heal.|")

    print("+====================================================================+")
    input("\n>>> PRESS [ENTER] TO START STAGE...")
