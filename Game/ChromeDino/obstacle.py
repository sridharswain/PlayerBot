import pygame
import random

class Obstacle(object):
    def __init__(self,gameDisplay):
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
        self.rect = self.obstacle.get_rect()
        self.imageSize = self.rect.size
        pygame.draw.rect(self.obstacle, (255,0,0), self.rect, 1)

    def getBoundary(self):
        self.obstacle.get_rect()

    def addToDisplay(self,x,y):
        #gameDisplay.fill((255,255,255))
        self.x = x
        self.y = y+(50-self.imageSize[1])
        self.rect.x=x
        self.rect.y=y
        self.gameDisplay.blit(self.obstacle,self.rect)
        pygame.draw.rect(self.obstacle, (255,0,0), self.rect, 1)

    def moveLeftBy(self,rate):
        self.x-=rate
        #self.y = y+(50-self.imageSize[1])
        self.rect.x=self.x
        self.rect.y=self.y
        self.gameDisplay.blit(self.obstacle,self.rect)
        return self.x
