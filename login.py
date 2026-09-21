def register():

    while True:
        username = input("Enter a new username: ")
        if len(username) < 8:
            print("Username should be at least 8 characters!")
        else:
            break

    while True:
        password = input("Enter a new password: ")
        if len(password) < 8:
            print("Password should be at least 8 characters!")
        else:
            break

    with open("users.txt", "a") as f:
        death = 0
        x = f"{username},{password},{death}\n"
        f.write(x)
    print("User registered successfully!")
    


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    with open("users.txt", "r") as f:
        users = f.readlines()
    
    for line in users:
        stored_username, stored_password,death = line.strip().split(',')
        if username == stored_username and password == stored_password:
            print("Login successful!")

            # Store the current user
            with open("cur_user.txt", "w") as f:
                f.write(username)

            # Immediately enter the game
            print(f"{username} has logged in. Welcome to the game!")
            return username
        
    print("Login failed. Invalid username or password.")
    return None

def main():
    while True:
        print("""    
                                                                welcome to
          
        ███    █▄  ███▄▄▄▄   ████████▄     ▄████████    ▄████████         ▄████████  ▄██████▄  ███    █▄   ▄█          ▄████████ 
        ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███        ███    ███ ███    ███ ███    ███ ███         ███    ███ 
        ███    ███ ███   ███ ███    ███   ███    █▀    ███    ███        ███    █▀  ███    ███ ███    ███ ███         ███    █▀  
        ███    ███ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀        ███        ███    ███ ███    ███ ███         ███        
        ███    ███ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀███████████ ███    ███ ███    ███ ███       ▀███████████ 
        ███    ███ ███   ███ ███    ███   ███    █▄  ▀███████████               ███ ███    ███ ███    ███ ███                ███ 
        ███    ███ ███   ███ ███   ▄███   ███    ███   ███    ███         ▄█    ███ ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
        ████████▀   ▀█   █▀  ████████▀    ██████████   ███    ███       ▄████████▀   ▀██████▀  ████████▀  █████▄▄██  ▄████████▀   
    """)
        choice = input("1. Register\n2. Login\n3. Quit\nEnter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:  # User successfully logged in
                while True:
                    play_choice = input("1. Start New Game\n2. Load Saved Game\nEnter your choice: ")
                    if play_choice == '1':
                        return 'new', user
                    elif play_choice == '2':
                        return 'load', user
                    else:
                        print("Invalid choice. Try again.")
        elif choice == '3':
            print("Exiting system.")
            exit()
        else:
            print("Invalid choice. Try again.")

        
if __name__ == "__main__":
    main()
