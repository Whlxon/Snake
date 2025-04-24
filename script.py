import time as t
import keyboard as kb
import os



print("Hello there ! Welcome to my snake made at home !")

t.sleep(2)

print("Lets begin !")

t.sleep(2)

snakeNumberPlate = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
]

line = ""
direction = "up"
index = [126]
running = True

while running:
    # affichage de l'écran de jeux
    os.system("cls")
    print("\n\n\n\n=====================================================Snake============================================")
    for i in range(len(snakeNumberPlate)):
        if(i in index):
            line = line + "⬛"
        elif(snakeNumberPlate[i] != -1):
            line = line + "⬜"
        else:
            print(line)
            line = ""
    
    print("======================================================================================================")

    
    
    if(kb.is_pressed("left") and (direction == "up" or direction == "down")):
        direction = "left"
    
    elif(kb.is_pressed("up") and (direction == "left" or direction == "right")):
        direction = "up"
    
    elif(kb.is_pressed("right") and (direction == "up" or direction == "down")):
            direction = "right"
    
    elif(kb.is_pressed("down") and (direction == "left" or direction == "right")):
        direction = "down"
    
    
    if(direction == "up"):
        index[0] -= 23
    
    elif(direction == "down"):
        index[0] += 23
    
    elif(direction == "left"):
        if(snakeNumberPlate[index[0] - 1] == 0):
            index[0] -= 1
        elif(snakeNumberPlate[index[0] - 1] == -1):
            index[0] += 21
    
    elif(direction == "right"):
        if(snakeNumberPlate[index[0] + 1] == 0):
            index[0] += 1
        elif(snakeNumberPlate[index[0] + 1] == -1):
            index[0] -= 21
            
    
    t.sleep(0.2)