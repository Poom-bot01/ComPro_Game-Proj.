import os

User_data = "./Data/Userdata.txt"
worldle_data = "./Data/Worldle_data.txt"
Typing_QTE_data = "./Data/Typing_QTE_data.txt"
Boss_fight_data = "./Data/Boss_fight_data.txt"




def saveUser_data(filename, data):
    tmp = filename + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for name, pw in data.items():
            f.write(f"{name}={pw}\n")
    os.replace(tmp, filename)

def loadUser_data(filename=User_data):
    data = {}
    if filename is None or not os.path.exists(filename):
        return data
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" not in line:
                continue
            name, pw = line.split("=", 1)
            data[name.strip()] = pw.strip()
    return data

def Typing_QTE_Record(player, wpm, correct, total):
    player["typing_rounds"] += 1
    player["wpm_total"] += wpm
    player["chars_correct"] += correct
    player["chars_total"] += total

def Worldle_Record(player, seconds):
    player["wordle_solves"] += 1
    player["wordle_time_total"] += seconds

def Boss_fight_Record(player, stage):
    if stage not in player["bosses_defeated"]:
        player["bosses_defeated"].append(stage)


#if __name__ == "__main__":
#    name = input("Username: ")
#    pw = input("Password: ")
#    if create_user(name, pw):
#        print("User created.")
#    else:
#        print("User already exists or invalid username.")
#    user_data = load_user(name)
#    if user_data:
#        print("Loaded user:", user_data)
#    else:
#        print("Failed to load user.")
