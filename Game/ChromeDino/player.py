import pygame
import math

class Player(object):
    def __init__(self,imgPath,gameDisplay):
        self.playerImage = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.rect = self.playerImage.get_rect()
        self.rect.width*=(3/4)
        self.rect.height*=(3/4)
        pygame.draw.rect(self.playerImage, (255,0,0), self.rect, 1)

    def setPlayerAt(self,x,y):
        self.x=x
        self.y=y
        self.rect.x=x
        self.rect.y=y
        self.gameDisplay.blit(self.playerImage,self.rect)

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)
