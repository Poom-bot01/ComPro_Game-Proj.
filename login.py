import os
import sys
import time
from character import ArcaneMerchant
from save_system import save_game

# In-memory user database (or file-backed)
users = {}

def clear_screen():
    """Clears terminal screen across Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(title, options):
    """Displays a standardized ASCII menu and prompts user choice."""
    print("+====================================================================+")
    print(f"| {title.center(66)} |")
    print("+--------------------------------------------------------------------+")
    for i, text in enumerate(options, 1):
        print(f"|  [{i}] {text:<60} |")
    print("+====================================================================+")
    return input(">>> CHOOSE OPTION: ").strip()

def show_title():
    """Displays the main ASCII title art for the game."""
    print(r"""
   ✦        ·        ⋆      ˚        ✧        ·        ⋆        ˚        ✦ 
      ·    █████  ██████   ██████  █████  ███    ██ ███████    ✧      
    ⋆      ██   ██ ██   ██ ██      ██   ██ ████   ██ ██            ·   
  ˖    ˚   ███████ ██████  ██      ███████ ██ ██  ██ █████      ⋆    
      ⋆    ██   ██ ██   ██ ██      ██   ██ ██  ██ ██ ██            ✧    
    ˚      ██   ██ ██   ██  ██████ ██   ██ ██   ████ ███████    ·     
 ·   ✦        ·        ⋆      ˚    ✧  ⋆          ·        ⋆        ˚    ✦
███    ███ ███████ ██████   ██████ ██   ██  █████  ███    ██ ████████ 
████  ████ ██      ██   ██ ██      ██   ██ ██   ██ ████   ██    ██    
██ ████ ██ █████   ██████  ██      ███████ ███████ ██ ██  ██    ██    
██  ██  ██ ██      ██   ██ ██      ██   ██ ██   ██ ██  ██ ██    ██    
██      ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██   ████    ██  
 ˚    ⋆    ✧      ·     ✦    ˚      ˖    ⋆      ·    ✦  ˖    ˚    ⋆   
✦    ⋆   ˚    ˖   ⋆   The Spellbound Journey  ✧    ·   ˚    ˖    ⋆    ✦     
    ˚        ✧        ·        ˚      ✦    ⋆        ·      ✧        ˚    ⋆   
""")

def valid_password(password):
    """Checks if password is at least 8 chars long with upper, lower, digit & special char."""
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for letter in password:
        if letter.isupper():
            has_upper = True
        elif letter.islower():
            has_lower = True
        elif letter.isdigit():
            has_number = True
        else:
            has_special = True

    if len(password) < 8:
        return False
    return has_upper and has_lower and has_number and has_special

def password_taken(password, own_name):
    """Ensures password uniqueness across all registered users."""
    for other_name in users:
        if other_name != own_name and users[other_name] == password:
            return True
    return False

def sign_up():
    """Registers a new user account, initializes their save file, and returns to main menu."""
    clear_screen()
    print("+====================================================================+")
    print("|                     ARCANE MERCHANT REGISTRATION                   |")
    print("+====================================================================+")
    print("| REQUIREMENT: Password must be 8+ chars with uppercase, lowercase,  |")
    print("|              numbers, and special characters.                      |")
    print("+--------------------------------------------------------------------+")
    
    while True:
        name = input("\n>>> Enter new username (blank to cancel): ").strip()
        if name == "":
            return None

        if name in users:
            print("[!] Username already taken! Choose another.")
            continue

        password = input(">>> Enter secure password: ")

        if not valid_password(password):
            print("[!] Weak password! Must have 8+ chars, upper, lower, digit & special.")
            continue
        elif password_taken(password, name):
            print("[!] Password is already in use by another merchant. Choose another.")
            continue
        else:
            users[name] = password
            
            # AUTOMATICALLY INITIALIZE SAVE FILE FOR NEW USER
            new_player = ArcaneMerchant(name)
            save_game(new_player)

            print("\n+--------------------------------------------------------------------+")
            print("| [*] SUCCESS: Account created & Save File initialized!              |")
            print("+--------------------------------------------------------------------+")
            time.sleep(1.8)
            return name

def reset_password(name):
    """Allows user to reset their password with clear prompts."""
    print("\n+====================================================================+")
    print("|                      PASSWORD RECOVERY PORTAL                      |")
    print("+====================================================================+")
    print("| Enter a new password meeting the security requirements (8+ chars,  |")
    print("| uppercase, lowercase, number, and special character).              |")
    print("+--------------------------------------------------------------------+")
    
    while True:
        password = input(">>> Enter new password: ")

        if valid_password(password) and not password_taken(password, name):
            print("+--------------------------------------------------------------------+")
            input(">>> Press [ENTER] to confirm password reset...")
            users[name] = password
            print("[*] SUCCESS: Password updated. Please log in again.")
            print("+--------------------------------------------------------------------+")
            time.sleep(1.5)
            return
        else:
            print("[!] Invalid or insecure password! Try again.")

def login():
    """Logs in an existing user with up to 3 attempts and clear ASCII status frames."""
    clear_screen()
    print("+====================================================================+")
    print("|                      MERCHANT AUTHENTICATION                       |")
    print("+====================================================================+")
    
    name = input(">>> Username: ").strip()
    
    if name not in users:
        print("[!] Username not found in the realm archives.")
        time.sleep(1.5)
        return None

    tries_left = 3

    while tries_left > 0:
        print(f"\n[?] Attempts remaining: {tries_left}/3")
        password = input(">>> Password (leave blank to initiate password reset): ")

        if password == "":
            reset_password(name)
            return None
        elif users[name] == password:
            print("\n+--------------------------------------------------------------------+")
            print(f"| [*] ACCESS GRANTED: Welcome back, {name}!                          |")
            print("+--------------------------------------------------------------------+")
            time.sleep(1.5)
            return name
        else:
            tries_left -= 1
            print(f"[!] Invalid password! {tries_left} tries left.")

    print("\n[!] SECURITY LOCKOUT: Too many failed attempts.")
    reset_password(name)
    return None
