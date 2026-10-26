users = {}

def menu(title, options):
    print("\n=== " + title + " ===")
    for i, text in enumerate(options, 1):
        print(str(i) + ". " + text)
    return input("Choose: ")

def show_title():
    print(f"""
✦   ˚    ·        ⋆      ˚       ✧       ·       ⋆       ˚        ✦ 
      ·    █████  ██████   ██████  █████  ███    ██ ███████    ✧      
    ⋆     ██   ██ ██   ██ ██      ██   ██ ████   ██ ██         ˖   ·   
  ˖    ˚  ███████ ██████  ██      ███████ ██ ██  ██ █████    ⋆    
      ⋆   ██   ██ ██   ██ ██      ██   ██ ██  ██ ██ ██           ✧    
   ˚      ██   ██ ██   ██  ██████ ██   ██ ██   ████ ███████    ·     
 ·   ✦       ·        ⋆      ˚      ⋆         ·       ⋆       ˚    ✦
███    ███ ███████ ██████   ██████ ██   ██  █████  ███    ██ ████████ 
████  ████ ██      ██   ██ ██      ██   ██ ██   ██ ████   ██    ██    
██ ████ ██ █████   ██████  ██      ███████ ███████ ██ ██  ██    ██    
██  ██  ██ ██      ██   ██ ██      ██   ██ ██   ██ ██  ██ ██    ██    
██      ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██   ████    ██ 
   ˚       ✦     ⋆        ˚     ⋆      ·      ˖    ˖   ˚       ⋆   
 ˚    ✦      ·  ✧   The Spellbound Journey   ✧  ·       ⋆   ✦  ˚   
   ˚     ✧    ˖          ⋆    ˚     ✦      ·      ˖        ˚    ⋆   
""")

def main():
    show_title()
    while True:
        choice = menu("MAIN MENU", ["Login", "Sign up", "Exit"])
        if choice == "1":
            name = login()
            if name:
                hub(name)
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-3")

def valid_password(password):
    upper = lower = number = special = False
    for sixseven in password:
        if sixseven.isupper():
            upper = True
        elif sixseven.islower():
            lower = True
        elif sixseven.isdigit():
            number = True
        else:
            special = True
    return len(password) >= 8 and upper and lower and number and special

def sign_up():
    while True:
        name = input("New username: ")
        if name == "":
            return
        password = input("New password: ")
        if name not in users and valid_password(password):
            input("[ Sign up ] Press Enter...")
            users[name] = password
            print("Account created!")
            return
        print("Invalid name or password")

def reset_password(name):
    print("--- Reset password ---")
    while True:
        password = input("New password: ")
        if valid_password(password):
            input("[ Reset password ] Press Enter...")
            users[name] = password
            print("Password changed. Please log in again.")
            return
        print("Invalid name or password")

def login():
    name = input("Username: ")
    for tries_left in [2, 1, 0]:
        password = input("Password (blank = forgot password): ")
        if password == "" and name in users:
            reset_password(name)
            return None
        if name in users and password == users[name]:
            return name
        print("Invalid name or password. " + str(tries_left) + " tries left")
    print("Too many wrong attempts.")
    if name in users:
        reset_password(name)
    return None

def hub(name):
    while True:
        choice = menu("GAME HUB - " + name,
                      ["Start game", "Load saved", "Scoreboard", "Log out"])
 
        if choice == "1":
            start_game(name)
        elif choice == "2":
            load_saved(name)
        elif choice == "3":
            show_scoreboard(name)
        elif choice == "4":
            print("Logged out.")
            return                          
        else:
            print("Please choose 1-4")
