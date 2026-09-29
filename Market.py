print("========================================")
print("\t\tMARKET")
print("========================================")
print("1. Item 1 ( A strange gift from an unknown source. )")
print("2. Item 2 ( An ancient symbol with a forgotten meaning. )")
print("3. Item 3 ( Something unusual lies within this mysterious object. )")
print("4. Item 4 ( Its secret can only be discovered by using it. )")
print("======================================== ")
choice = int(input("Choose one item: "))
while choice < 1 or choice > 4:
    print("\nInvalid choice. Choose again.")
    choice = int(input("Choose one item: "))


if choice == 1:
    print("\nGift of the Gods")
    player.xp = player.xp * 2
    print("Something strange happened to your XP.")

elif choice == 2:
    print("\nDeath Mark")
    player.xp = 0
    print("Something strange happened to your XP.")

elif choice == 3:
    print("\nXP Poison")
    player.xp = player.xp - 30
    print("Something strange happened to your XP.")

elif choice == 4:
    print("\nXP Potion")
    player.xp = player.xp + 40
    print("Something strange happened to your XP.")


print(f"\nYour current XP: {player.xp}")