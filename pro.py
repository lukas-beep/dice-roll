import random 
import os

clear = lambda: os.system('cls')

NUMBERS = [[1,4,6,3],[1,2,6,5]] # numbers that the dice can roll

#roll dice simulator
def roll_dice():
    speed = random.randint(1,5) # speed/second
    time = random.randint(1,30) # time that the dice rolls in seconds
    distance = speed * time # distance that the dice rolls
    direction = random.randint(1,2)# direction that the dice rolls 1 = index 0, 2 = index 1
    direction_of_direction = random.choice([1,-1]) # direction of direction 1 = forward, -1 = backward
    numbers = NUMBERS[direction-1] # numbers that the dice can roll
    numbers = numbers[::direction_of_direction] # reverse the numbers in direction
    start_num = random.choice(numbers) # start number of the dice
    pos_index = numbers.index(start_num) + 1 # index of the start number
    to_end = len(numbers) - pos_index # number of numbers to the end of the list
    distance -= to_end # new distance that the dice rolls
    distance = distance % len(numbers) # final distance that the dice rolls
    end_num = numbers[distance-1] # end number of the dice

    return end_num

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
