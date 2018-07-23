import pygame
import math

class Player(object):
    def __init__(self,imgPath,gameDisplay,clock):
        self.playerImage = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.clock=clock
        self.rect = self.playerImage.get_rect()

    def setPlayerAt(self,x,y):
        self.x=x
        self.y=y
        self.rect.x=x
        self.rect.y=y
        self.gameDisplay.blit(self.playerImage,self.rect)
        pygame.draw.rect(self.playerImage, (255,0,0), self.rect, 1)

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)
