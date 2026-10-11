users = {"demo": "123456"}

def show_menu(title, options):
    print(f"\n=== {title} ===")
    for number, text in enumerate(options, 1):
        print(f"{number}. {text}")
    return input("Choose: ").strip()

def reset_password(name):
    print("\n--- Reset password ---")
    users[name] = input("New password: ")      # TODO: verify identity first
    print("Password changed. Please log in again.")

def login():
    name = input("Username: ")
    if name not in users:
        print("User not found.")
        return None

    for attempt in range(3):
        password = input("Password (blank = forgot password): ")
        if password == "":
            reset_password(name)
            return None
        if password == users[name]:
            return name
        print(f"Wrong password. {2 - attempt} tries left.")

    print("Too many wrong attempts.")
    reset_password(name)
    return None

def sign_up():
    name = input("New username: ")
    if name == "" or name in users:
        print("Invalid or already taken.")
    else:
        users[name] = input("New password: ")
        print("Account created!")

def game_hub(name):
    while True:
        choice = show_menu(f"GAME HUB ({name})",
                           ["Start game", "Load saved", "Leaderboard", "Log out"])
        if choice == "1":
            print("Starting game... (coming soon)")
        elif choice == "2":
            print("Loading save... (coming soon)")
        elif choice == "3":
            print("Leaderboard... (coming soon)")
        elif choice == "4":
            return
        else:
            print("Please choose 1-4.")


if __name__ == "__main__":
    print("***** ARCANE MERCHANT *****")
    while True:
        choice = show_menu("MAIN MENU", ["Login", "Sign up", "Exit"])
        if choice == "1":
            name = login()
            if name:
                game_hub(name)
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-3.")


