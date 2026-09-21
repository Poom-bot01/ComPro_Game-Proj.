def thaijai(player):
    attempts1 = 0
    max_attempts = 3
    question = 1

    while attempts1 < max_attempts:
        answer1 = input("""
              Rearrange the letters to form the word
                        
████████╗    ███████╗    ██╗          ██████╗     █████╗     ███████╗
╚══██╔══╝    ██╔════╝    ██║         ██╔════╝    ██╔══██╗    ██╔════╝
   ██║       ███████╗    ██║         ██║         ███████║    █████╗  
   ██║       ╚════██║    ██║         ██║         ██╔══██║    ██╔══╝  
   ██║       ███████║    ███████╗    ╚██████╗    ██║  ██║    ███████╗
   ╚═╝       ╚══════╝    ╚══════╝     ╚═════╝    ╚═╝  ╚═╝    ╚══════╝': 
                
                        
                Ans: """).lower()
        if answer1 == "castle":
            print("Correct! Moving on to the next word.")
            question += 1
            break
        else:
            attempts1 += 1
            print(f"Incorrect! You have made {attempts1} incorrect attempts.")
            if attempts1 == max_attempts:
                print("You have used all 3 attempts.")
                print("You will not receive any souls for this.")
                break


    if question == 2:


        while attempts1 < max_attempts:
            answer2 = input("""
                Rearrange the letters to form the word 
                            
████████╗    ██╗    ██╗   ██╗     ██████╗     ██████╗     ██████╗     ██╗   ██╗
╚══██╔══╝    ██║    ██║   ██║    ██╔════╝    ██╔═══██╗    ██╔══██╗    ╚██╗ ██╔╝
   ██║       ██║    ██║   ██║    ██║         ██║   ██║    ██████╔╝     ╚████╔╝ 
   ██║       ██║    ╚██╗ ██╔╝    ██║         ██║   ██║    ██╔══██╗      ╚██╔╝  
   ██║       ██║     ╚████╔╝     ╚██████╗    ╚██████╔╝    ██║  ██║       ██║   
   ╚═╝       ╚═╝      ╚═══╝       ╚═════╝     ╚═════╝     ╚═╝  ╚═╝       ╚═╝   
                                                                               
                            
                Ans: """).lower()
            if answer2 == "victory":
                print("Correct! Moving on to the next word.")
                question += 1
                break
            else:
                attempts1 += 1
                print(f"Incorrect! You have made {attempts2} incorrect attempts.")
                if attempts1 == max_attempts:
                    print("You have used all 3 attempts.")
                    print("You will not receive any souls for this.")
                    break


    if question == 3:

        while attempts1 < max_attempts:
            answer3 = input("""
                    Rearrange the letters to form the word.
                            
███████╗    ██╗   ██╗     ██████╗    ███████╗    ███████╗    ███████╗    ███████╗    ██╗   ██╗    ██╗          ██████╗
██╔════╝    ██║   ██║    ██╔════╝    ██╔════╝    ██╔════╝    ██╔════╝    ██╔════╝    ██║   ██║    ██║         ██╔════╝
███████╗    ██║   ██║    ██║         █████╗      ███████╗    █████╗      ███████╗    ██║   ██║    ██║         ██║     
╚════██║    ██║   ██║    ██║         ██╔══╝      ╚════██║    ██╔══╝      ╚════██║    ██║   ██║    ██║         ██║     
███████║    ╚██████╔╝    ╚██████╗    ███████╗    ███████║    ██║         ███████║    ╚██████╔╝    ███████╗    ╚██████╗
╚══════╝     ╚═════╝      ╚═════╝    ╚══════╝    ╚══════╝    ╚═╝         ╚══════╝     ╚═════╝     ╚══════╝     ╚═════╝
                                                                                                                      
                    Ans: """).lower()
            if answer3 == "successful":
                print("Correct! You have completed all the words.")
                print("You got 1000 souls for your braindog")
                player.souls += 1000
                print(f"Souls: {player.souls}")
                break
            else:
                attempts1 += 1
                print(f"Incorrect! You have made {attempts3} incorrect attempts.")
                if attempts1 == max_attempts:
                    print("You have used all 3 attempts.")
                    print("You will not receive any souls for this.")
                    break


if __name__ == "__main__":
    import main
    player = main.Character("John")
    thaijai(player)