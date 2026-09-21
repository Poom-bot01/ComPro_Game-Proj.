def save_score(player):
    # Load existing scores from the file into a dictionary
    scores = {}
    try:
        with open("scoreboard.txt", "r") as file:
            for line in file:
                name, deaths = line.strip().split(",")
                scores[name] = int(float(deaths))  # Convert deaths to float, then to int
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty scoreboard
        pass

    # Update the player's score (replace if exists, or add new if not)
    scores[player.name] = player.deaths

    # Write the updated scores back to the file
    with open("scoreboard.txt", "w") as file:
        for name, deaths in scores.items():
            file.write(f"{name},{deaths}\n")

def print_scoreboard():
    print("--------------------------------")
    print("\tSCOREBOARD")
    print("--------------------------------")
    scores = []

    # Load existing scores from the file into a list of tuples
    try:
        with open("scoreboard.txt", "r") as file:
            for line in file:
                name, deaths = line.strip().split(",")
                scores.append((name, int(float(deaths))))  # Convert deaths to float, then to int
    except FileNotFoundError:
        print("No scoreboard file found.")
        print("--------------------------------")
        return

    # Sort the scores by deaths in descending order
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Print the sorted scores
    for name, deaths in sorted_scores:
        print(f"Player: {name} | Deaths: {deaths}")
    
    print("--------------------------------")