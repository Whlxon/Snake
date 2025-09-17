import random as rd

class snakeGame:# I create the class of the snake, to reUse it later, maybe..
    def __init__(self): # okay I mean, you know, I know, They know, this is just the constructor and I init all of the snake variables
        self.grid =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.cRowS = [6]
        self.cColS = [8]

        self.appleRow = 5
        self.appleCol = 5

        self.size = 1

        self.direction = "up"
    
    def move(self): # Okay here is the move function so I use a switcher to compress the tingy
        index = len(self.cColS)-1
        while index !=  0:
            self.cColS[index] = self.cColS[index-1]
            self.cRowS[index] = self.cRowS[index-1]
            index -= 1

        match self.direction:
            case "right":
                self.cColS[0] += 1
            case "left":
                self.cColS[0] -= 1
            case "up":
                self.cRowS[0] -= 1
            case "down":
                self.cRowS[0] += 1

        if(self.hitHimSelf()):
            return False

        self.doEat()
    
    def modDirection(self, direction): # Okay actually this function is to modify the direction of the snake, and to do this I just modify the value of the variable ^^
        rightDirection = ["right", "left", "up", "down"]

        if(direction in rightDirection):
            self.direction = direction

    def grow(self):# Okay this function is to add a new variable in the list
        self.cRowS.append(self.cRowS[len(self.cRowS)-1])
        self.cColS.append(self.cColS[len(self.cColS)-1])
        self.size += 1
    
    def hitHimSelf(self):# Okay here we verify if the snake hit himself and return True or False if he does
        for i in range(len(self.cColS)-1):
            match self.direction:
                case "right":
                    if(self.cColS[0]+1 == self.cColS[i] and self.cRowS[0] == self.cRowS[i]):
                        return True
                case "left":
                    if(self.cColS[0]-1 == self.cColS[i] and self.cRowS[0] == self.cRowS[i]):
                        return True
                case "up":
                    if(self.cColS[0] == self.cColS[i] and self.cRowS[0]-1 == self.cRowS[i]):
                        return True
                case "down":
                    if(self.cColS[0] == self.cColS[i] and self.cRowS[0]+1 == self.cRowS[i]):
                        return True
                

    def doEat(self):# here we verify if he touche the apple on the grid
        if(self.cColS[0] == self.appleCol and self.cRowS[0] == self.appleRow):
            self.grow()
            self.genAppleCo()
    
    def transformGrid(self):
        finalGrid = [[],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     []]

        for i in range(len(self.grid)-1):
            for j in range(len(self.grid[0])-1):
                finalGrid[i].append("⬜")
        
        for i in range(len(self.cColS)):
            finalGrid[self.cRowS[i-1]][self.cColS[i-1]] = "⬛"
        
        finalGrid[self.appleRow][self.appleCol] = "🟥"

        return finalGrid

    def genAppleCo(self):
        col = rd.randint(0, len(self.grid)-1)
        row = rd.randint(0, len(self.grid)-1)
        
        while col in self.cColS and row in self.cRowS:
            row = rd.randint(0, len(self.grid)-1)
            col = rd.randint(0, len(self.grid)-1)
        
        self.appleCol = col
        self.appleRow = row
