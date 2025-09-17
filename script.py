import time as t
import keyboard as kb
from Snake import snakeGame
import os
import random



print("Hello there ! Welcome to my snake made at home !")

t.sleep(2)

print("Lets begin !")

t.sleep(2)

snake = snakeGame()

running = True

while running:
    print("\n\n\n\n\n\n\n\n\n")
    grid = snake.transformGrid()
    
    if(kb.is_pressed("left") and (snake.direction == "up" or snake.direction == "down")):
        snake.modDirection("left")
    
    elif(kb.is_pressed("up") and (snake.direction == "left" or snake.direction == "right")):
        snake.modDirection("up")
    
    elif(kb.is_pressed("right") and (snake.direction == "up" or snake.direction == "down")):
        snake.modDirection("right")
    
    elif(kb.is_pressed("down") and (snake.direction == "left" or snake.direction == "right")):
        snake.modDirection("down")

    
    for i in range(len(grid)-1):
        line = ""
        for j in range(len(grid)-1):
            line += grid[i][j]
        
        print(line)

    if(snake.move() == False):
       print("fin")
       running = False

    t.sleep(0.5)