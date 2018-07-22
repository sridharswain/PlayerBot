import pygame
import random

class Obstacle:
    def __init__(self,gameDisplay,clock):
        images = ["obstacle_small_1","obstacle_small_2","obstacle_small_3","obstacle_large_2","obstacle_large_3"]
        randomInt = random.randint(0,11)
        if(randomInt < 3):
            imgPath = 0
        elif(randomInt < 6):
            imgPath = 1
        elif(randomInt < 8):
            imgPath = 2
        elif(randomInt < 10):
            imgPath = 3
        else:
            imgPath = 4
        imgPath = "res/"+images[imgPath]+".png"
        self.obstacle = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.clock=clock
        self.rect = self.obstacle.get_rect()
        self.imageSize = self.rect.size

    def getBoundary(self):
        self.obstacle.get_rect()

    def addToDisplay(self,x,y):
        #gameDisplay.fill((255,255,255))
        self.gameDisplay.blit(self.obstacle,(x,y+(50-self.imageSize[1])))
        self.x = x
        self.y = y

    def moveLeftBy(self,rate):
        self.x-=rate
        self.gameDisplay.blit(self.obstacle,(self.x,self.y+(50-self.imageSize[1])))
        return self.x
