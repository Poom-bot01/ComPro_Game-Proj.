import clear_screen

import time


def courtyard(player):
    time.sleep(2)
    print("""
    ──────────────────────────────────────────────────────
                        The Courtyard
    ──────────────────────────────────────────────────────
    You stand at the heart of the decaying kingdom of Eldoria.
    The once majestic courtyard is now overgrown with dark vines,
    the fountain that once flowed with pure water is now cracked
    and dry. Shadows linger in the corners, and an eerie silence
    pervades the air.
    
    Your journey begins here, but the path ahead is dangerous.
    You must prepare yourself and gather strength.
    """)

    input("\n[PRESS ENTER TO CONTINUE]\n") 
    clear_screen.clear_screen()
    time.sleep(2)
    return 'courtyard'


def armory():
    time.sleep(2)
    print("""
    ──────────────────────────────────────────────────────
                        The Armory
    ──────────────────────────────────────────────────────
    You enter the Armory, a once grand hall filled with weapons and
    armor that now lies in ruin. Broken swords and shattered shields
    are scattered across the ground. However, you can still salvage
    some items to help you in your quest.
    
    The walls echo with the battles fought here long ago, and you feel
    the presence of the warriors who came before you.
    """)

    input("\n[PRESS ENTER TO CONTINUE]\n")
    clear_screen.clear_screen()
    time.sleep(2)
    return 'armory'


def treasury():
    time.sleep(2)
    print("""
    ──────────────────────────────────────────────────────
                        The Treasury
    ──────────────────────────────────────────────────────
    You step into the Treasury, where once the riches of Eldoria
    were stored. The chests are now empty, and most of the wealth
    has been stolen or lost. However, a mysterious box sits in the
    center of the room. The lock has a number code.

    If you can guess the right number, the box will open, revealing
    a prize.
    """)

    input("\n[PRESS ENTER TO CONTINUE]\n")
    clear_screen.clear_screen() 
    time.sleep(2)
    return 'treasury'

def library():
    time.sleep(2)
    print("""
    ──────────────────────────────────────────────────────
                        The Abyssal Library
    ──────────────────────────────────────────────────────
    You enter the Abyssal Library, a place where forbidden knowledge
    is kept. The shelves stretch endlessly, and the books are covered
    in dust. This place is a maze of ancient texts and shadowy corridors.

    To proceed, you must find your way through the maze of the library.
    """)
    input("\n[PRESS ENTER TO CONTINUE]\n")
    clear_screen.clear_screen() 
    time.sleep(2)
    return 'library'

def throne_room():
    time.sleep(2)
    print("""
    ──────────────────────────────────────────────────────
                  The Abyssal Throne Room
    ──────────────────────────────────────────────────────
    You finally reach the heart of Eldoria, the Abyssal Throne Room.
    A grand hall shrouded in darkness, where the Abyss King awaits.
    
    The air is thick with power, and you can feel the weight of the
    Abyss pressing down on you. This is your final confrontation,
    the battle that will determine the fate of the kingdom.
    
    Will you reclaim the light, or will you fall to the darkness?
    """)

    input("\n[PRESS ENTER TO CONTINUE]\n")
    clear_screen.clear_screen()
    time.sleep(2)
    return 'throne_room'