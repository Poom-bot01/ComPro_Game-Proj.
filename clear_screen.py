import os
import time 

def clear_screen():
    if os.name == 'nt':
        
        os.system('cls')
    else:
        os.system('clear')