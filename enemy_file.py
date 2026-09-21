
import random
import main

class weakEnemy():
    def charecter(self):
        print("""
          
⠀⠀⠀⠀⠀⠀⠀⣠⢴⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⡄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠄⢇⠀⠀⠀⠀⣠⠒⡐⢂⠀⠀⠀⣸⠩⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡄⢠⠊⣙⠕⠁⠰⢀⣁⠼⡙⠕⡎⠢⢈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡄⣸⣰⢝⡎⠀⡆⠂⢐⣬⠉⢢⠈⣜⢪⣇⠠⢤⡀⠀
⠀⠀⠀⠀⡠⠋⠀⡔⠩⢿⠀⠘⢦⣀⡨⢟⣀⣸⠀⣟⠣⠕⠒⡀⢡⠀
⠀⠀⢀⢴⠁⠀⣜⡀⠀⠸⠀⠀⣀⢤⠒⣒⠺⠆⠀⡇⠀⢀⢤⠇⢀⡆
⡀⠀⣘⣵⢀⢠⡦⠇⠀⠀⡇⣬⣧⣆⣣⣋⣃⣸⣤⠁⠀⢸⣴⠀⠈⡹
⠻⡽⠭⢿⡟⢩⠁⠀⢀⡠⢗⠙⣉⣁⣒⡊⠒⡅⡎⠀⠀⠀⠑⠚⠚⠁
⠀⠈⡩⢋⠕⣉⠄⢊⢡⠔⠈⣇⠀⠀⠀⠀⢀⡇⠃⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢤⣭⡰⠬⠒⢁⠔⠈⠀⠈⠉⠉⠉⠁⠀⠑⠤⠁⢒⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠃⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⢀⠏⠀⠀⠀⠀
⠀⠀⠀⢀⣤⢤⠤⡃⠀⠱⠀⠀⠀⠀⠀⠀⢀⣜⠀⡠⢦⠠⣄⠀⠀⠀
⠀⠀⠀⠘⠣⠧⠤⠄⠀⠐⠁⠀⠀⠀⠀⠀⠘⠒⠒⠀⠘⠒⠛⠀⠀⠀

                    """)
        
    def __init__(self,name):
        self.name = name
        self.health = random.randint(20,40)


    def rand_atk(self):
        atk_type = random.choice(["light", "heavy", "special"])
        if atk_type == "light":
            return atk_type, self.light_atk_dmg()
        elif atk_type == "heavy":
            return atk_type, self.heavy_atk_dmg()
        elif atk_type == "special":
            return atk_type, self.special_atk_dmg()
    
    def light_atk_dmg(self):
        return 50#random.randint(3,7)

    def heavy_atk_dmg(self):
        return 50#random.randint(10,15)
    
    def special_atk_dmg(self):
        return 50#random.randint(20,30)
    
    def souls(self):
        return random.randint(20,40)
    

class strongEnemy():
    def charecter(self):
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⣤⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⢸⣄⠉⠁⠉⢉⡲⢤
⠀⠀⠀⢀⡠⠴⠊⣭⠃⠀⣀⣀⡤⠴⢶⠤⠤⢤⣀⠀⢸⠸⠈⠣⡀⢠⠃⠀⠀
⠀⢀⢔⡉⢀⣀⠐⠐⢧⣾⣴⣿⡿⠀⠀⡏⡄⠀⠀⢱⡧⢀⡠⠤⠬⣎⣧⠀⠀
⠐⠋⠁⠀⠀⢸⠔⢢⣿⣿⣿⡿⠃⠀⢠⠃⠀⠠⢚⣉⣠⢯⠀⠀⠀⠈⠛⠀⠀
⠀⠀⠀⠀⠀⠈⠀⣼⠙⠛⠉⠀⢀⣠⢊⠆⠀⠀⠈⣴⠃⣼⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡌⢦⣀⣀⠬⡺⠕⠁⠀⠀⠀⢀⠟⠸⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⣀⠀⡦⢄⣠⣾⣿⣾⣦⠀⢀⠼⢱⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡏⠉⠁⣀⠈⠻⣿⣿⠉⠀⠈⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡏⠁⠈⠙⣿⢟⡀⢀⠄⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠀⡤⠃⠫⡉⠙⠃⠁⠀⠈⠠⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠐⡀⠀⠀⠀⠀⣨⠆⠀⣀⠤⠒⠀⠙⠣⠤⠐⠒⠒⠄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⡉⠀⠀⡜⠄⠀⠘⣏⡄⠀⣀⡠⠤⠠⢄⠘⡄⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⡔⣳⠒⠒⠚⣿⠀⠰⢎⠀⠈⠁⠀⠀⠀⠀⢠⠇⡼⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠳⢌⡘⢄⡀⠀⠘⠦⣀⣉⣉⣁⠒⣄⠀⠀⠀⣸⢼⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡧⣸⠀⠀⠀⠀⢠⠔⠋⢀⡼⠀⠀⠀⠉⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠊⠁⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠤⠠⠤⠴⠠⠠⠠⠤⠤⠀⠠⠲⠀⠆⠤⠦⠴⠰⠀⠀⠀⠀
""")    
        
    def __init__(self,name):
        self.name = name
        self.health = random.randint(60,80)

    def rand_atk(self):
        atk_type = random.choice(["light", "heavy", "special"])
        if atk_type == "light":
            return atk_type, self.light_atk_dmg()
        elif atk_type == "heavy":
            return atk_type, self.heavy_atk_dmg()
        elif atk_type == "special":
            return atk_type, self.special_atk_dmg()
        
    def light_atk_dmg(self):
        return random.randint(10,15)

    def heavy_atk_dmg(self):
        return random.randint(20,25)
    
    def special_atk_dmg(self):
        return random.randint(30,40)
    
    def souls(self):
        return random.randint(60,80)
    
class eliteEnemy():
    def charecter(self):
         print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡗⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡤⠤⠶⠿⣶⣦⣄⣙⣦⠙⢿⡓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠭⣉⠓⠒⠚⠽⡄⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⡿⠀⠀⠀⣀⡽⠀⠀⠀⠘⢈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡆⢠⠖⠚⣇⠀⣙⡶⠄⠈⠰⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠐⣧⣾⡄⣄⠘⣆⡈⠷⠄⣤⣶⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠛⣦⣘⢿⣇⣿⣿⠉⠹⣗⠦⣈⠘⣾⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⡾⠛⣏⠿⠧⡀⠈⠳⣄⡙⠊⠉⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⣤⡴⠉⠀⠀⠈⢳⡀⠑⠦⡀⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣬⠷⢮⣙⣒⣤⡤⠀⠀⢹⡄⡄⢱⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠳⣄⠀⠀⠀⠀⠠⣌⣩⠿⠀⠒⣼⡇⠇⠈⠳⡄⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣹⣤⣖⣸⣍⣿⠽⠤⠒⠚⠋⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠋⠉⠉⠀⠀⠀⠀⣠⡤⠂⠀⠀⢠⡀⢰⠋⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⠤⣶⡾⠅⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⢺⠀⠀⠀⢈⣇⠜⠃⠀⣾⡈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠇⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠋⠈⠀⠀⢠⠞⠋⠀⢀⡾⠁⠉⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣏⡼⠁⠀⠀⠀⢀⡤⠤⠔⠊⢉⣡⠼⠓⠀⠀⢀⣴⣋⣀⡠⠶⠻⣄⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡿⠁⢠⠔⠒⠚⢋⡤⠖⠊⢩⡟⠀⠀⢀⣠⠞⠋⠉⠁⠀⠀⠀⠀⠀⠉⢹⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢼⢻⠇⡤⠇⠀⢀⣴⠋⠀⠀⠀⣼⣠⠴⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⣿⡰⠂⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⣏⢻⡀⢀⣠⠴⠛⠉⠓⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣄⡀⠘⢆⡙⠋⠀⢀⡠⠔⠦⠐⠒⣚⠙⣲⡦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢧⡀⠀⠈⠉⠉⠁⣀⠀⣀⡴⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣶⣤⡀⠉⠘⠛⠻⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⡌⠁⠒⢄⠀⠈⠑⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⣄⣁⣀⣀⣀⣛⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
""")
         
    def __init__(self,name):
        self.name = name
        self.health = random.randint(150,200)

    def rand_atk(self):
        atk_type = random.choice(["light", "heavy", "special"])
        if atk_type == "light":
            return atk_type, self.light_atk_dmg()
        elif atk_type == "heavy":
            return atk_type, self.heavy_atk_dmg()
        elif atk_type == "special":
            return atk_type, self.special_atk_dmg()
        
    def light_atk_dmg(self):
        return random.randint(30,40)

    def heavy_atk_dmg(self):
        return random.randint(50,70)
    
    def special_atk_dmg(self):
        return random.randint(80,80)
    
    def souls(self):
        return random.randint(150,200)
    

class Abyss_Walker():
    def charecter(self):
         print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡗⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡤⠤⠶⠿⣶⣦⣄⣙⣦⠙⢿⡓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠭⣉⠓⠒⠚⠽⡄⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⡿⠀⠀⠀⣀⡽⠀⠀⠀⠘⢈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡆⢠⠖⠚⣇⠀⣙⡶⠄⠈⠰⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠐⣧⣾⡄⣄⠘⣆⡈⠷⠄⣤⣶⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠛⣦⣘⢿⣇⣿⣿⠉⠹⣗⠦⣈⠘⣾⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⡾⠛⣏⠿⠧⡀⠈⠳⣄⡙⠊⠉⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⣤⡴⠉⠀⠀⠈⢳⡀⠑⠦⡀⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣬⠷⢮⣙⣒⣤⡤⠀⠀⢹⡄⡄⢱⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠳⣄⠀⠀⠀⠀⠠⣌⣩⠿⠀⠒⣼⡇⠇⠈⠳⡄⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣹⣤⣖⣸⣍⣿⠽⠤⠒⠚⠋⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠋⠉⠉⠀⠀⠀⠀⣠⡤⠂⠀⠀⢠⡀⢰⠋⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⠤⣶⡾⠅⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⢺⠀⠀⠀⢈⣇⠜⠃⠀⣾⡈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠇⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠋⠈⠀⠀⢠⠞⠋⠀⢀⡾⠁⠉⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣏⡼⠁⠀⠀⠀⢀⡤⠤⠔⠊⢉⣡⠼⠓⠀⠀⢀⣴⣋⣀⡠⠶⠻⣄⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡿⠁⢠⠔⠒⠚⢋⡤⠖⠊⢩⡟⠀⠀⢀⣠⠞⠋⠉⠁⠀⠀⠀⠀⠀⠉⢹⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢼⢻⠇⡤⠇⠀⢀⣴⠋⠀⠀⠀⣼⣠⠴⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⣿⡰⠂⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡇⠀⠀⣏⢻⡀⢀⣠⠴⠛⠉⠓⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣄⡀⠘⢆⡙⠋⠀⢀⡠⠔⠦⠐⠒⣚⠙⣲⡦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢧⡀⠀⠈⠉⠉⠁⣀⠀⣀⡴⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣶⣤⡀⠉⠘⠛⠻⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⡌⠁⠒⢄⠀⠈⠑⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⣄⣁⣀⣀⣀⣛⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
""")
    def __init__(self,name):
        self.name = name
        self.health = 500

    def rand_atk(self):
        atk_type = random.choice(["light", "heavy", "special"])
        if atk_type == "light":
            return atk_type, self.light_atk_dmg()
        elif atk_type == "heavy":
            return atk_type, self.heavy_atk_dmg()
        elif atk_type == "special":
            return atk_type, self.special_atk_dmg()
        
    def light_atk_dmg(self):
        return random.randint(50,55)

    def heavy_atk_dmg(self):
        return random.randint(100,120)
    
    def special_atk_dmg(self):
        return random.randint(200,300)
    
    def souls(self):
        return random.randint(500,500)
    

def generate_enemies(player_level):
    num_enemies = random.randint(1,5)
    enemies = []
    enemy_type = ["weak", "strong", "elite"]

    if player_level <= 6:
        #enemy_type = ["weak", "strong", "elite"]
        weights = [80,19,1]
    elif player_level <= 12:
        #enemy_type = ["weak", "strong", "elite"]
        weights = [60,30,10]
    elif player_level <= 20:
        #enemy_type = ["weak", "strong", "elite"]
        weights = [40,40,20]
    else:
        weights = [20,40,40]



    for _ in range(num_enemies):
        enemy_choice = random.choices(enemy_type, weights = weights, k=1)[0]

        if enemy_choice == "weak":
            enemies.append(weakEnemy("Abyssal Minion"))
        elif enemy_choice == "strong":
            enemies.append(strongEnemy("Abyssal strong"))
        elif enemy_choice == "elite":
            enemies.append(eliteEnemy("Abyssal elite"))

    return enemies
    
if __name__ == "__main__":
    player_level = 5
    enemies = generate_enemies(player_level)
    player = main.Character("John")
    for enemy in enemies:
        main.battle(player,enemy)
