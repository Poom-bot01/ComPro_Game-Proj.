import os

LEADERBOARD_FILE = "leaderboard.txt"

def show_leaderboard():
    """Reads leaderboard.txt, sorts scores descending, and displays top players."""
    print("\n+====================================================================+")
    print("|                       GLOBAL HIGH SCORES                           |")
    print("+====================================================================+")

    if not os.path.exists(LEADERBOARD_FILE):
        print("| NO HIGH SCORES RECORDED YET.                                       |")
        print("+====================================================================+")
        input("\n>>> PRESS [ENTER] TO RETURN...")
        return

    entries = []
    with open(LEADERBOARD_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line and ":" in line:
                user, score = line.split(":", 1)
                try:
                    entries.append((user, int(score)))
                except ValueError:
                    continue

    # Sort descending by highest score
    entries.sort(key=lambda x: x[1], reverse=True)

    print("| RANK | USERNAME             | HIGH SCORE                           |")
    print("+--------------------------------------------------------------------+")
    if not entries:
        print("| NO VALID LEADERBOARD ENTRIES FOUND.                                |")
    else:
        for rank, (user, score) in enumerate(entries[:10], 1):
            print(f"| {rank:<4} | {user:<20} | {score:<36} |")
    print("+====================================================================+")

    input("\n>>> PRESS [ENTER] TO RETURN...")
    
