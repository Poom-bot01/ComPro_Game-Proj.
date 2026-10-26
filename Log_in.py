users = {}

def menu(title, options):
    print("\n=== " + title + " ===")
    for i, text in enumerate(options, 1):
        print(str(i) + ". " + text)
    return input("Choose: ")

def show_title():
    print(f"""
   ✦       ·        ⋆      ˚       ✧       ·       ⋆       ˚       ✦ 
      ·    █████  ██████   ██████  █████  ███    ██ ███████    ✧      
    ⋆     ██   ██ ██   ██ ██      ██   ██ ████   ██ ██            ·   
  ˖    ˚  ███████ ██████  ██      ███████ ██ ██  ██ █████      ⋆    
      ⋆   ██   ██ ██   ██ ██      ██   ██ ██  ██ ██ ██            ✧    
   ˚      ██   ██ ██   ██  ██████ ██   ██ ██   ████ ███████    ·     
 ·   ✦       ·        ⋆      ˚    ✧  ⋆         ·       ⋆       ˚    ✦
███    ███ ███████ ██████   ██████ ██   ██  █████  ███    ██ ████████ 
████  ████ ██      ██   ██ ██      ██   ██ ██   ██ ████   ██    ██    
██ ████ ██ █████   ██████  ██      ███████ ███████ ██ ██  ██    ██    
██  ██  ██ ██      ██   ██ ██      ██   ██ ██   ██ ██  ██ ██    ██    
██      ██ ███████ ██   ██  ██████ ██   ██ ██   ██ ██   ████    ██ 
 ˚    ⋆    ✧     ·     ✦    ˚     ˖    ⋆     ·    ✦  ˖     ˚    ⋆   
✦    ⋆   ˚    ˖   ⋆   The Spellbound Journey  ✧   ·   ˚    ˖   ⋆    ✦     
   ˚       ✧        ·       ˚     ✦   ⋆       ·      ✧        ˚    ⋆   
""")

def main():
    show_title()
    while True:
        choice = menu("MAIN MENU", ["Login", "Sign up", "Exit"])
        if choice == "1":
            name = login()
            if name:
                hub()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-3")

def valid_password(password):
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
    if has_upper and has_lower and has_number and has_special:
        return True
    return False

def password_taken(password, own_name):
    for other_name in users:                        
        if other_name != own_name and users[other_name] == password:
            return True                             
    return False

def sign_up():
    while True:
        name = input("New username (blank to cancel): ")
        if name == "":
            return                       
 
        password = input("New password: ")
 
        if name in users:                
            print("Invalid name or password")
        elif valid_password(password) == False:
            print("Invalid name or password")
        elif password_taken(password, name):   
            print("Invalid name or password")
        else:
            input("[ Sign up ] Press Enter...")
            users[name] = password       
            print("Account created!")
            return

def reset_password(name):
    print("--- Reset password ---")
    while True:
        password = input("New password: ")
 
        if valid_password(password) == True and password_taken(password, name) == False:
            input("[ Reset password ] Press Enter...")
            users[name] = password       
            print("Password changed. Please log in again.")
            return
        else:
            print("Invalid name or password")

def login():
    name = input("Username: ")
    tries_left = 3
 
    while tries_left > 0:
        password = input("Password (blank = forgot password): ")
 
        if password == "" and name in users:          
            reset_password(name)
            return None
        elif name in users and password == users[name]:   
            return name
        else:                                          
            tries_left = tries_left - 1
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
