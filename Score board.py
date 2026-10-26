from New_save import Player_records, loadPlayer_records, savePlayer_records


def save_score(player, total_score=None):
    """Save a player's cumulative score after a boss stage is completed."""
    if isinstance(player, dict):
        username = player.get("username") or player.get("name")
        if total_score is None:
            total_score = player.get("total_score")
    else:
        username = getattr(player, "name", None)
        if total_score is None:
            total_score = getattr(player, "total_score", None)

    if not username:
        raise ValueError("Player must have a username or name.")
    if total_score is None:
        raise ValueError("Pass the player's cumulative score as total_score.")

    records = loadPlayer_records(Player_records)
    player_record = records.setdefault(username, {})
    player_record["total_score"] = int(total_score)
    savePlayer_records(Player_records, records)


def print_scoreboard():
    print("--------------------------------")
    print("\tSCOREBOARD")
    print("--------------------------------")

    records = loadPlayer_records(Player_records)
    sorted_scores = sorted(
        ((name, data.get("total_score", 0)) for name, data in records.items()),
        key=lambda item: item[1],
        reverse=True,
    )

    if not sorted_scores:
        print("No scores saved yet.")
    else:
        for rank, (name, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. Player: {name} | Total score: {score}")

    print("--------------------------------")
