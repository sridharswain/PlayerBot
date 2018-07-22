import pygame
import math

class Player:
    def __init__(self,imgPath,gameDisplay,clock):
        self.playerImage = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.clock=clock

    def setPlayerAt(self,x,y):
        self.gameDisplay.blit(self.playerImage,(x,y))
        self.x=x
        self.y=y

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)
