import pygame
import math

class Player(object):
    def __init__(self,gameDisplay):
        self.playerImage = pygame.image.load("res/agent.png")
        self.duckImage = pygame.image.load("res/trex_duck.png")
        self.gameDisplay = gameDisplay
        self.rect = self.playerImage.get_rect()
        self.rect.width *= (3/4)
        self.rect.height *= (3/4)
        duckRect = self.duckImage.get_rect()
        duckRect.width *=(3/4)
        duckRect.height *=(3/4)
        pygame.draw.rect(self.playerImage, (255,0,0), self.rect, 1)
        pygame.draw.rect(self.duckImage, (255,0,0), duckRect, 1)
        self.isDucked = False

    def setPlayerAt(self,x,y,shouldDuck):
        self.x = x
        self.y = y
        self.isDucked = shouldDuck
        if(shouldDuck):
            self.y += 20
            self.rect = self.duckImage.get_rect()
        else:
            self.rect = self.playerImage.get_rect()
        self.rect.width *= (3/4)
        self.rect.height *= (3/4)
        self.rect.x = self.x
        self.rect.y = self.y
        self.gameDisplay.blit(self.duckImage if (shouldDuck) else self.playerImage,self.rect)

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)
