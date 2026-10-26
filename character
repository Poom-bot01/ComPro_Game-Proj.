class ArcaneMerchant:
    def __init__(self, name):
        # 1. Authentication
        self.name = name  # Username
        
        # 2. Character State
        self.current_hp = 30  # Current HP
        self.mana = 10        # Mana
        self.attack_power = 15 # Attack Power
        
        # 3. Economy Data
        self.gold_balance = 500  # Gold Balance
        self.inventory_list = [] # Inventory List
        self.cursed_status = False # Cursed Status
        
        
        # 5. Progress & Score
        self.current_stage = 1  # Current Stage [1-6]
        self.high_score = 0     # High Score
        self.latest_score = 0    # Latest Run Score

    def restore_full(self):
        """Restores player HP to max capacity."""
        self.current_hp = 50
        self.mana = 45
        print("+----------------------------------------------------------+")
        print("| *** [RESTORATION] HP & MANA RESTORED TO MAXIMUM ***      |")
        print("+----------------------------------------------------------+")

    def display_stats(self):
        inv = ", ".join(self.inventory_list) if self.inventory_list else "NONE"
        cursed = "YES (CURSED)" if self.cursed_status else "NO"
        print("+====================================================================+")
        print(f"| MERCHANT CARD: {self.name:<22} STAGE: [{self.current_stage}/6]              |")
        print("+--------------------------------------------------------------------+")
        print(f"| HP: [{self.current_hp:2d}/50] | MANA: [{self.mana:2d}/45] | ATK: [{self.attack_power:2d}/50]")
        print(f"| GOLD: [{self.gold_balance:4d}$]")
        print(f"| RELICS: {inv:<58} ")
        print(f"| CURSED: {cursed:<12} ")
        print(f"| HIGH SCORE: {self.high_score:<10} | LATEST RUN SCORE: {self.latest_score:<14}")
        print("+====================================================================+")

    
