
import combat_system as cs


'''def light_attack(player):
    
    if player.stamina >= 10:
        print(f"{player.name} performs a light attack!")
        player.stamina -= 10

    else:
        print("Not enough stamina for a light attack.")'''
    
    
    

def heavy_attack(player):
    if player.stamina >= 20:
        print(f"{player.name} performs a heavy attack!")
        player.stamina -= 20
    else:
        print("Not enough stamina for a heavy attack.")

def healing_spells(player):
    if player.stamina >= 50:
        print(f"{player.name} has cast a healing spell!")
        player.stamina -= 50
    else:
        print("Not enough stamina to cast a healing spell.")

def magic_spells(player):
    if player.stamina >= 50:
        print(f"{player.name} has cast a magic spell!")
        player.stamina -= 50
    else:
        print("Not enough stamina to cast a magic spell.")


def block(player):
    print(f"{player.name} blocks the attack and regenerates stamina!")
    player.stamina += 15
    if player.stamina > 100:
        player.stamina = 100



if __name__ == "__main__":
    pass