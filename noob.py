import random 
import os

clear = lambda: os.system('cls')

#roll dice simulator
def roll_dice():
    return random.randint(1,6)

def main():
    while 1:
        clear()
        dice_roll = roll_dice()
        print("The dice rolled a " + str(dice_roll))
        i = input("Press enter to roll the dice")
        if i == "q":
            return
        clear()


main()
