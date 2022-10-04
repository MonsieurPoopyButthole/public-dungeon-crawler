import random


OBSTACLE = '='
PLAYER = 'P'


class Player:
    def __init__(self, gridSize):
        self.xPos = random.randint(0,gridSize*2)
        self.yPos = random.randint(0,gridSize)
    
    def xDisplacement(self, xVector):
        self.xPos = self.xPos + xVector
    
    def yDisplacement(self, yVector):
        self.yPos = self.yPos + yVector
        
    def position(self):
        print(str(self.xPos) + "=x  " + str(self.yPos) + "=y")


gridSize = int(input("Enter grid size "))
grid = [["."] * gridSize*2 for i in range(gridSize)]
playerCharacter = Player(gridSize)

while(True):
    chanceOfObstacle = float(input("Enter a percentage chance of position to be an obstacle "))
    if(chanceOfObstacle <= 100 and chanceOfObstacle >= 0):
        break
    print("Wrong value, re-enter it")
    

#fill grid
for i in range(gridSize):
    for j in range(gridSize*2):
        chance = random.randint(0, 100) 
        if(chance < chanceOfObstacle):
            grid[i][j] = OBSTACLE
grid[playerCharacter.yPos][playerCharacter.xPos] = PLAYER


#print grid
for i in range(gridSize):
    for j in range(gridSize*2):
        print(grid[i][j], end="")
    print()

playerCharacter.position()
