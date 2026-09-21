attempts1 = 0
max_attempts = 3

while attempts1 < max_attempts:
    answer1 = int(input("(18*2) + 15 = "))
    if answer1 == 51:
        print("Correct! Moving on to the next question.")
        break
    else:
        attempts1 += 1
        print(f"Incorrect! You have made {attempts1} incorrect attempts.")
        if attempts1 == max_attempts:
            print("You have used all 3 attempts.")
            print("You will not receive any coins for this question!")
            break


attempts2 = 0

while attempts2 < max_attempts:
    answer2 = float(input("log10(6+2) - 2^2 = "))
    if answer2 == 4:
        print("Correct! You have answered this question correctly.")
        if attempts1 < max_attempts:
            print("You will receive coins for answering both questions correctly.")
        break
    else:
        attempts2 += 1
        print(f"Incorrect! You have made {attempts2} incorrect attempts.")
        if attempts2 == max_attempts:
            print("You have used all 3 attempts.")
            print("You will not receive any coins for this question!")