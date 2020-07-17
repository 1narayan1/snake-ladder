import random
import time

# Ladder will take player upwards from current position to ladder finish
ladder = {
    1:38,
    4:14,
    8:30,
    21:42,
    28:76,
    50:67,
    71:89,
    80:99
}

# Snake bite will lower down the players from current position to snake tail
snake = {
    32:10,
    34:6,
    48:26,
    62:18,
    88:24,
    95:56,
    97:78
}


Game_finish_point = 100
get = ""

########################################################################################################################
p1_init_pos = 0
p2_init_pos = 0

p1_final_pos = 0
p2_final_pos = 0

########################################################################################################################


# Welcome message to players

print("Welcome to snake ladder game!")
print("Please enter your nsme to enjoy this game ")
p1 = input("Player 1,Your name: ")
time.sleep(1.3)
p2 = input("Player 2, Your name: ")
time.sleep(1.3)

print("This amazing match will be played between",p1,"and",p2)

########################################################################################################################

print("")
print("Okay! Now,Lets roll the dice")
print("")

while 1 == 1:
    player1 = input(p1 + " Lets roll the dice: ")
    print("")

    p1_dice = random.randint(1,6)
    print("You Rolled, " + str(p1_dice))
    p1_final_pos = p1_init_pos + p1_dice

    print(p1 + " moved from "+ str(p1_init_pos)+ " to " + str(p1_final_pos))
    p1_init_pos = p1_final_pos
    p1_final_pos = 0
    print("")

    if p1_init_pos in snake:
        print("Snake Bite.............")
        deduct = random.randint(1,12)
        p1_final_pos = p1_init_pos - deduct
        print("")

        print(p1 + " went down from " + str(p1_init_pos)+ " to " + str(p1_final_pos))
        p1_init_pos = p1_final_pos
        p1_final_pos = 0

    elif p1_init_pos >= Game_finish_point:
        get = "a"
        break

    elif p1_init_pos in ladder:
        print("Woooohhh" or "You Got a Ladder" or "Yay ! A Ladder")
        add = random.randint(1,12)
        p1_final_pos = p1_init_pos + add
        print("")

        print(p1 + " went up from" + str(p1_init_pos) + " to " + str(p1_final_pos))
        p1_init_pos = p1_final_pos
        p1_final_pos = 0

    time.sleep(0.5)

    ####################################################################################################################

    player2 = input(p2 + "Lets roll the dice: ")
    print("")

    p2_dice = random.randint(1,6)
    print("You Rolled, " + str(p2_dice))
    p2_final_pos = p2_init_pos + p2_dice

    print(p2 + " moved from " + str(p2_init_pos) + " to " + str(p2_final_pos))
    p2_init_pos = p2_final_pos
    p2_final_pos = 0
    print("")

    if p2_init_pos in snake:
        print("Snake Bite.............")
        deduct = random.randint(1, 12)
        p2_final_pos = p2_init_pos - deduct
        print("")

        print(p2 + " went down from " + str(p2_init_pos) + " to " + str(p2_final_pos))
        p2_init_pos = p2_final_pos
        p2_final_pos = 0

    elif p2_init_pos >= Game_finish_point:
        get = "a"
        break

    elif p2_init_pos in ladder:
        print("Woooohhh" or "You Got a Ladder" or "Yay ! A Ladder")
        add = random.randint(1, 12)
        p2_final_pos = p2_init_pos + add
        print("")

        print(p2 + " went up from" + str(p2_init_pos) + " to " + str(p2_final_pos))
        p2_init_pos = p2_final_pos
        p2_final_pos = 0

    time.sleep(0.5)
########################################################################################################################

print("Game over")
print("")
if get == "a":
    print(p1 + "hoooooraaayyy Congratulations! You won the game")
else:
    print(p2 + "hoooooraaayyy Congratulations! You won the game")







