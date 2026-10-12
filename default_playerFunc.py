DEFAULT_PLAYER = {
    "hp": 100,
    "gold": 500,
    "xp": 0,
    "items": [],
    "stage": 1,
}

def new_player():
    player = dict(DEFAULT_PLAYER)
    player["items"] = list(DEFAULT_PLAYER["items"])  
    return player

def fill_defaults(data):
    player = new_player()
    player.update(data)
    return player
