import pygame

class Spaceship:
    def __init__(self,gameDisplay,imgPath):
        self.player = pygame.image.load(imgPath)
        self.gameDisplay=self.gameDisplay

    def setPlayerAt(self,x,y):
        self.gameDisplay.blit(self.player,(x,y))
