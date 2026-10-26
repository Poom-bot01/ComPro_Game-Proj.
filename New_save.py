import os

User_data = "/home/dev/Vs-code project/Gameproj./Data/User_data.txt"
worldle_data = "/home/dev/Vs-code project/Gameproj./Data/Worldle_data.txt"
Typing_QTE_data = "/home/dev/Vs-code project/Gameproj./Data/Typing_QTE_data.txt"
Boss_fight_data = "/home/dev/Vs-code project/Gameproj./Data/Boss_fight_data.txt"




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



#Code pass see more in Savefile(inprocess)
